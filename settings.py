#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullit_speed_factor = 1
        self.bullit_width = 300
        self.bullit_height = 150
        self.bullit_color = 60, 60, 60
        self.bullits_allowed = 5

        # 外星人的设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 100
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
