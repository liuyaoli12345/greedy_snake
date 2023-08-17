# -*- coding: utf-8 -*-

import single_player
import ai_battle
import menu

# 定义方向常量
UP = (0, -10)
DOWN = (0, 10)
LEFT = (-10, 0)
RIGHT = (10, 0)
    
    # 菜单循环
while True:
    selected_mode = menu.main_menu()
    # 识别不同的对战模式，调用相应的游戏代码
    if selected_mode == "single_player":
        print("单人模式")
        single_player.start_game()
    elif selected_mode[0] == "ai_battle":
        print("AI对战模式")
        print("AI对战模式的难度:", selected_mode[1])
        ai_battle.start_ai_battle(selected_mode[1])
