# -*- coding: utf-8 -*-

import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 定义窗口尺寸
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 定义方向常量
UP = (-10, 0)
DOWN = (10, 0)
LEFT = (0, -10)
RIGHT = (0, 10)

# 贪吃蛇移动的方向
direction = RIGHT
change_to = direction

# 贪吃蛇的初始位置和长度
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# 食物的初始位置
food_pos = [random.randrange(1, width//10) * 10,
            random.randrange(1, height//10) * 10]
food_spawn = True

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = UP
            if event.key == pygame.K_DOWN:
                change_to = DOWN
            if event.key == pygame.K_LEFT:
                change_to = LEFT
            if event.key == pygame.K_RIGHT:
                change_to = RIGHT

    new_pos = [snake_pos[0] + change_to[0], snake_pos[1] + change_to[1]]
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()
    if not food_spawn:
        food_pos = [random.randrange(1, width//10) * 10,
                    random.randrange(1, height//10) * 10]
    food_spawn = True

    snake_pos = list(new_pos)

    screen.fill((0, 0, 0))
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    pygame.display.flip()
