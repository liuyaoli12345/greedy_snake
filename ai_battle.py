# ai_battle.py
import pygame
import sys
import random
import ai_logic
import menu

# 初始化Pygame
pygame.init()

# 定义窗口尺寸
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")
game_font = pygame.font.Font("./经典宋体简.ttf", 30)

# 初始化食物的位置
food_pos = [random.randrange(1, width//10) * 10,
            random.randrange(1, height//10) * 10]
food_spawn = True

# 游戏主循环
def start_ai_battle(ai_difficulty):
    UP = (0, -10)
    DOWN = (0, 10)
    LEFT = (-10, 0)
    RIGHT = (10, 0)

    # 初始化玩家和敌人蛇的位置
    player_snake_pos = [100, 50]
    enemy_snake_pos = [500, 50]
    player_snake_body = [[100, 50], [90, 50], [80, 50]]
    enemy_snake_body = [[500, 50], [510, 50], [520, 50]]

    player_next_direction = RIGHT  # 默认初始方向

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_next_direction = UP
                if event.key == pygame.K_DOWN:
                    player_next_direction = DOWN
                if event.key == pygame.K_LEFT:
                    player_next_direction = LEFT
                if event.key == pygame.K_RIGHT:
                    player_next_direction = RIGHT

        # 获取敌人蛇的下一个移动方向
        if ai_difficulty == "stupid":
            enemy_next_direction = ai_logic.ai_stupid(enemy_snake_pos, food_pos)
        elif ai_difficulty == "simple":
            enemy_next_direction = ai_logic.ai_simple(enemy_snake_pos, food_pos)
        elif ai_difficulty == "advanced":
            enemy_next_direction = ai_logic.ai_advanced(enemy_snake_pos, food_pos)

        # 更新玩家和敌人蛇的位置
        player_snake_pos, player_snake_body = update_snake(player_snake_pos, player_next_direction, player_snake_body)
        enemy_snake_pos, enemy_snake_body = update_snake(enemy_snake_pos, enemy_next_direction, enemy_snake_body)

        # 检测玩家和敌人蛇是否碰撞到边界或碰撞到自己的身体
        if (player_snake_pos[0] >= width or player_snake_pos[0] < 0 or
            player_snake_pos[1] >= height or player_snake_pos[1] < 0):
            # 处理碰撞逻辑（游戏结束等）
            pass

        # 绘制游戏画面
        screen.fill((0, 0, 0))
        for pos in player_snake_body:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
        for pos in enemy_snake_body:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        pygame.display.flip()
        pygame.time.delay(100)
        

# 更新蛇的位置
def update_snake(snake_pos, direction, snake_body):
    global food_pos, food_spawn
    # 计算新的蛇头位置
    new_pos = [snake_pos[0] + direction[0], snake_pos[1] + direction[1]]

    # 在更新蛇的位置之前
    if new_pos[0] >= width:
        new_pos[0] = 0
    if new_pos[0] < 0:
        new_pos[0] = width
    if new_pos[1] >= height:
        new_pos[1] = 0
    if new_pos[1] < 0:
        new_pos[1] = height

    # 插入新的蛇头位置
    snake_body.insert(0, list(snake_pos))

    # 如果蛇吃到食物，不删除蛇尾
    if snake_pos == food_pos:
        food_spawn = False
        food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10] 
    else:
        snake_body.pop()

    return new_pos, snake_body
