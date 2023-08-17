# -*- coding: utf-8 -*-

import pygame
import sys

# 初始化Pygame
pygame.init()

# 定义窗口尺寸
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏 - 菜单")
game_font = pygame.font.Font("./经典宋体简.ttf", 30)

# 定义颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        screen.fill(WHITE)
        font = game_font
        
        draw_text("贪吃蛇游戏", font, GREEN, screen, 240, 100)
        draw_text("1. 单人模式", font, RED, screen, 260, 200)
        draw_text("2. AI对战", font, RED, screen, 260, 250)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "single_player"
                if event.key == pygame.K_2:
                    ai_battle_mode = ai_battle_menu()
                    return "ai_battle", ai_battle_mode

def ai_battle_menu():
    while True:
        screen.fill(WHITE)
        font = game_font
        
        draw_text("选择AI对战模式", font, RED, screen, 240, 100)
        draw_text("1. 愚蠢的敌人", font, RED, screen, 260, 200)
        draw_text("2. 简单的敌人", font, RED, screen, 260, 250)
        draw_text("3. 高级的敌人", font, RED, screen, 260, 300)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "stupid"
                if event.key == pygame.K_2:
                    return "simple"
                if event.key == pygame.K_3:
                    return "advanced"

if __name__ == "__main__":
    selected_mode = main_menu()
    print("用户选择的模式:", selected_mode)
        
