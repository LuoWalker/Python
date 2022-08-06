import sys
import pygame

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏，创建游戏资源"""
        pygame.init() # 利用pygame初始化一个窗口

        self.screen = pygame.display.set_mode((1000,600)) # 创建主窗口的surface，经过一次循环后重画
        pygame.display.set_caption("打飞机")
        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 获取键鼠
            for event in pygame.event.get(): # 重画窗口之前的所有操作
                if event.type == pygame.QUIT: # QUIT -> 关闭按钮
                    sys.exit()
            
            # 让最近绘制的屏幕可见
            pygame.display.flip() # 每次循环重画，只保留最新的

if __name__ == '__main__':
    """"创建游戏实例并运行"""
    ai = AlienInvasion()
    ai.run_game()