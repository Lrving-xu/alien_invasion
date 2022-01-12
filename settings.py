#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullit_speed_factor = 1
        self.bullit_width = 3
        self.bullit_height = 1
        self.bullit_color = 60, 60, 60
        self.bullits_allowed = 10

        # 外星人的设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speed_scale = 1.1
        self.initialize_dynmaic_settings()

        # 外星人点数的提高速度
        self.score_scale = 1.5


    def initialize_dynmaic_settings(self):
        """初始化随着游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullit_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speed_scale
        self.bullit_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale