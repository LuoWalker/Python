import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏，创建游戏资源"""
        pygame.init()  # 利用pygame初始化一个窗口
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # 创建主窗口的surface，经过一次循环后重画
        pygame.display.set_caption("打飞机")

        self.ship = Ship(self)
        self.stats = GameStats(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 获取键鼠
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):  # 方法中的方法，辅助方法
        for event in pygame.event.get():  # 重画窗口之前的所有操作
            if event.type == pygame.QUIT:  # QUIT -> 关闭按钮
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # 更新位置
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _create_alien(self, alien_number, margin, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = margin + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """更新外星人位置"""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _create_fleet(self):
        """创建外星人"""
        # 横向判断距离
        alien = Alien(self)
        alien_width, alien_heigh = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = 10  # available_space_x // (2 * alien_width)
        # 计算横边距
        margin = (self.settings.screen_width -
                  (2 * number_aliens_x - 1) * alien_width) / 2

        # 纵向距离
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - \
            (3 * alien_heigh) - ship_height
        number_rows = available_space_y // (2 * alien_heigh)

        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, margin, row_number)

    def _check_fleet_edges(self):
        """外星人到边"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """下移 变向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_bullet_alien_collisions(self):
        """判断碰撞 collisions={bullet: alien}, True: 确认删除"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        """飞机撞"""

        self.stats.ships_left -= 1

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        sleep(0.5)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)  # 使背景色填满
        self.ship.blitem()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()  # 每次循环重画，只保留最新的


if __name__ == '__main__':
    """"创建游戏实例并运行"""
    ai = AlienInvasion()
    ai.run_game()
