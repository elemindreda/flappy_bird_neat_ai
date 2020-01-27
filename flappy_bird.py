import pygame
from random import randint
import math



WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 360
OBSTACLE_SPACE = 30
x = 30
y = 30

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    is_blue = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if is_blue:
        color = (0,128,255)
    else:
        color = (255,100,0)

    clock.tick(60)
    screen.fill((0,0,0))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    pygame.display.flip()


pygame.quit()