import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人"""

    def __init__(self, ai_game):
        """初始外星人"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人
        self.image = pygame.image.load('alien_invasion/images/enemy.bmp')
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人水平位置
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """向右移动外星人"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
