"""飞船"""

import pygame


class Spaceship():
    """对飞船初始化以及管理飞船位置移动的类"""

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(r'alien_invasion\images\spaceship2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.spaceship_speed
            # 如果用elif的话，当左右键同时按下时，
            # 只有右键被响应，会一直向右，而用两个
            # if的话则左右键都被响应，即保持不动
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.spaceship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.spaceship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.spaceship_speed

        # 根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_spaceship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
