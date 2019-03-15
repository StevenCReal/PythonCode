"""实现游戏功能模块"""

import sys
from time import sleep

import pygame

from bullet import Bullet
from ufo import Ufo


def check_keydown_events(event, ai_settings, screen, spaceship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = True
    elif event.key == pygame.K_LEFT:
        spaceship.moving_left = True
    elif event.key == pygame.K_UP:
        spaceship.moving_up = True
    elif event.key == pygame.K_DOWN:
        spaceship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, spaceship, bullets)
    elif event.key == pygame.K_q:
        sys.exit(0)


def fire_bullet(ai_settings, screen, spaceship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建一颗子弹，并加入到编组bullets中
    if fire_bullet and len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, spaceship)
        bullets.add(new_bullet)


def check_keyup_events(event, spaceship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        spaceship.moving_right = False
    elif event.key == pygame.K_LEFT:
        spaceship.moving_left = False
    elif event.key == pygame.K_UP:
        spaceship.moving_up = False
    elif event.key == pygame.K_DOWN:
        spaceship.moving_down = False


def check_events(ai_settings, screen, stats, play_button, spaceship, ufos,
                 bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, spaceship,
                                 bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spaceship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button,
                              spaceship, ufos, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, spaceship, ufos,
                      bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 清空外星人列表和子弹列表
        ufos.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, spaceship, ufos)
        spaceship.center_spaceship()


def update_screen(ai_settings, screen, stats, sb, spaceship, ufos, bullets,
                  play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星飞船后面重绘所有子弹
    ufos.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.blitme()

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态， 就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    #让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, spaceship, ufos, bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置，并删除已消失的子弹
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

    check_bullet_ufo_collisions(ai_settings, screen, stats, sb, spaceship, ufos, bullets)


def check_bullet_ufo_collisions(ai_settings, screen, stats, sb, spaceship, ufos, bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, ufos, True, True)

    if collisions:
        for ufo in collisions.values():
            stats.score += ai_settings.ufo_points * len(ufos)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(ufos) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, spaceship, ufos)


def get_number_ufos_x(ai_settings, ufo_width):
    """计算每行可容纳多少外星飞船"""
    available_space_x = ai_settings.screen_width - 2 * ufo_width
    number_ufos_x = int(available_space_x / (2 * ufo_width))
    return number_ufos_x


def get_number_rows(ai_settings, spaceship_height, ufo_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (
        ai_settings.screen_height - (3 * ufo_height) - spaceship_height)
    number_rows = int(available_space_y / (2 * ufo_height))
    return number_rows


def create_ufo(ai_settings, screen, ufos, ufo_number, row_number):
    """创建一个外星飞船并将其放在当前行"""
    ufo = Ufo(ai_settings, screen)
    ufo_width = ufo.rect.width
    ufo.x = ufo_width + 2 * ufo_width * ufo_number
    ufo.rect.x = ufo.x
    ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
    ufos.add(ufo)


def create_fleet(ai_settings, screen, spaceship, ufos):
    """创建外星飞船群"""
    # 创建一个外星飞船，并计算每行可容纳多少个外星飞船
    ufo = Ufo(ai_settings, screen)
    number_ufos_x = get_number_ufos_x(ai_settings, ufo.rect.width)
    number_rows = get_number_rows(ai_settings, spaceship.rect.height,
                                  ufo.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for ufo_number in range(number_ufos_x):
            create_ufo(ai_settings, screen, ufos, ufo_number, row_number)


def check_fleet_edges(ai_settings, ufos):
    """有外星人到达边缘时采取相应措施"""
    for ufo in ufos.sprites():
        if ufo.check_edges():
            change_fleet_direction(ai_settings, ufos)
            break


def change_fleet_direction(ai_settings, ufos):
    """将整群外星人下移，并改变它们的方向"""
    for ufo in ufos.sprites():
        ufo.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def spaceship_hit(ai_settings, stats, screen, spaceship, ufos, bullets):
    """响应被外星人撞到的飞船"""
    if stats.spaceship_left > 0:
        # 将spaceship_left减一
        stats.spaceship_left -= 1

        # 清空外星人列表和子弹列表
        ufos.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, spaceship, ufos)
        spaceship.center_spaceship()

        #暂停
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_ufos_bottom(ai_settings, stats, screen, spaceship, ufos, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for ufo in ufos.sprites():
        if ufo.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            spaceship_hit(ai_settings, stats, screen, spaceship, ufos, bullets)
            break


def update_ufos(ai_settings, stats, screen, spaceship, ufos, bullets):
    """检查是否有外星飞船位于屏幕边缘，并更新外星飞船中所有外星飞船的位置"""
    check_fleet_edges(ai_settings, ufos)
    ufos.update()

    # 检测外星飞船和飞船之间的碰撞
    if pygame.sprite.spritecollideany(spaceship, ufos):
        spaceship_hit(ai_settings, stats, screen, spaceship, ufos, bullets)
    # 检查是否有外星人到达屏幕底端
    check_ufos_bottom(ai_settings, stats, screen, spaceship, ufos, bullets)

def check_high_score (stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()