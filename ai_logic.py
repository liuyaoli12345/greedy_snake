# ai_logic.py
import random

UP = (0, -10)
DOWN = (0, 10)
LEFT = (-10, 0)
RIGHT = (10, 0)

def ai_stupid(snake_pos, food_pos):
    # 愚蠢的敌人AI逻辑，随机移动
    return random.choice([UP, DOWN, LEFT, RIGHT])

def ai_simple(snake_pos, food_pos):
    # 简单的敌人AI逻辑，朝向食物的方向移动
    x_diff = food_pos[0] - snake_pos[0]
    y_diff = food_pos[1] - snake_pos[1]

    # 添加随机性
    if random.random() < 0.4:  # 40% 的概率随机选择方向
        return random.choice([UP, DOWN, LEFT, RIGHT])

    if abs(x_diff) > abs(y_diff):
        return RIGHT if x_diff > 0 else LEFT
    else:
        return DOWN if y_diff > 0 else UP


def ai_advanced(snake_pos, food_pos):
    # 高级的敌人AI逻辑，尝试找到更短路径到达食物
    pass  # 这里需要填充更复杂的寻路算法
