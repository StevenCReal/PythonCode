"""外星人入侵游戏"""

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStatus
from scoreboard import Scoreboard
from button import Button
from spaceship import Spaceship
import game_function as gf


def run_game():
    """游戏主程序"""

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(screen, "Play")

    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStatus(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星飞船编组
    spaceship = Spaceship(ai_settings, screen)
    bullets = Group()
    ufos = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, spaceship, ufos)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, spaceship,
                        ufos, bullets)

        if stats.game_active:
            spaceship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, spaceship, ufos,
                              bullets)
            gf.update_ufos(ai_settings, stats, screen, spaceship, ufos,
                           bullets)

        gf.update_screen(ai_settings, screen, stats, sb, spaceship, ufos,
                         bullets, play_button)


run_game()
