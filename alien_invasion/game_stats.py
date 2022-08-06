class GameStats:
    """游戏统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """游戏中变化的信息"""
        self.ships_left = self.settings.ship_limit  # 飞机剩余次数
