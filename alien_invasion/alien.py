import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人"""

    def __init__(self, ai_game):
        """初始外星人"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人
        self.image = pygame.image.load('alien_invasion/images/enemy.bmp')
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人水平位置
        self.x = float(self.rect.x)
