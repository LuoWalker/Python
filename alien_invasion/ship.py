import pygame
from settings import Settings


class Ship:
    """管理飞机"""

    def __init__(self, ai_game):
        """初始化飞船"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()  # 屏幕的surface
        self.settings = ai_game.settings

        # 加载飞船及其外接矩形
        self.image = pygame.image.load('alien_invasion/images/me.bmp')
        self.rect = self.image.get_rect()  # 飞机的surface

        # 飞机重置在底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitem(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
