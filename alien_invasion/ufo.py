"""UFO"""

import pygame
from pygame.sprite import Sprite


class Ufo(Sprite):
    """表示单个外星飞船的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星飞船图像并获取其外接矩形
        self.image = pygame.image.load(r"alien_invasion\images\ufo.bmp")
        self.rect = self.image.get_rect()

        # 每艘外星飞船最初都在屏幕左上角附近,不等
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果外星飞船位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左或向右移动外星飞船"""
        self.x += (
            self.ai_settings.ufo_speed * self.ai_settings.fleet_direction)
        self.rect.x = self.x