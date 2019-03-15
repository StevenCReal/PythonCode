"""游戏设置"""


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (182, 184, 183)

        #飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #外星飞船设置
        self.fleet_drop_speed = 10

        # 加快游戏节奏速度
        self.speedup_scale = 1.1
        # 外星飞船点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.spaceship_speed = 1.5
        self.bullet_speed = 3
        self.ufo_speed = 1

        # fleet_direction为1表示向右移，-1表示向左移
        self.fleet_direction = 1

        #计分
        self.ufo_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.spaceship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ufo_speed *= self.speedup_scale

        self.ufo_points = int(self.ufo_points * self.score_scale)
