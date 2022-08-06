import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理子弹"""

    def __init__(self, ai_game):
        """在飞船位置创建子弹"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # 图像的rect：self.image.get_rect()，图形的rect：pygame.Rect()
        self.rect.midtop = ai_game.ship.rect.midtop  # 先创建再移动

        self.y = float(self.rect.y)

    def update(self):
        """子弹的移动，向上"""
        self.y -= self.settings.bullet_speed  # 浮点型
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
