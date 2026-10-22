import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

width = 640
height = 480
x = width//2 
y = height//2 

x_pink = randint(40, 600)
y_pink = randint(50, 430)

points = 0
font = pygame.font.SysFont('lucidasans', 35, True, False)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('passarinho')
clock = pygame.time.Clock()

while True:
    clock.tick(50)
    screen.fill((0,0,0))
    message = f'Pontos: {points}'
    text_format = font.render(message, False, (204, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    if pygame.key.get_pressed()[K_a]:
        x = x - 15
    if pygame.key.get_pressed()[K_d]:
            x = x + 15
    if pygame.key.get_pressed()[K_w]:
            y = y - 15
    if pygame.key.get_pressed()[K_s]:
            y = y + 15

    ret_purple = pygame.draw.rect(screen, (100, 0, 200), (x, y, 50, 40))
    ret_pink = pygame.draw.rect(screen, (255, 102, 178), (x_pink, y_pink, 40, 40))

    if ret_purple.colliderect(ret_pink):
        x_pink = randint(40, 600)
        y_pink = randint(50, 430)
        points = points + 1
        
    screen.blit(text_format, (380, 40))

    pygame.display.update()

