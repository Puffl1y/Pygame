import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

width = 640
height = 480

x_snake = width // 2
y_snake = height // 2

velocity = 10
x_control = velocity
y_control = 0

x_apple = randint(40, 600)
y_apple = randint(50, 430)

points = 0
font = pygame.font.SysFont('lucidasans', 35, True, False)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('snake game')
clock = pygame.time.Clock()

snake_list = []
initial_length = 5


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(screen,(50, 255, 80),(XeY[0], XeY[1], 20, 20))


while True:
    clock.tick(30)
    screen.fill((0, 0, 0))

    message = f'Pontos: {points}'
    text_format = font.render(message, True, (204, 255, 255))

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:

            if event.key == K_a:
                if x_control == 0:
                    x_control = -velocity
                    y_control = 0

            elif event.key == K_d:
                if x_control == 0:
                    x_control = velocity
                    y_control = 0

            elif event.key == K_w:
                if y_control == 0:
                    y_control = -velocity
                    x_control = 0

            elif event.key == K_s:
                if y_control == 0:
                    y_control = velocity
                    x_control = 0

    x_snake += x_control
    y_snake += y_control

    snake = pygame.draw.rect(screen, (50, 255, 30),(x_snake, y_snake, 20, 20))

    apple = pygame.draw.rect(screen, (255, 0, 0),(x_apple, y_apple, 20, 20))

    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)

        points += 1
        initial_length += 1

    list_of_snake = []
    list_of_snake.append(x_snake)
    list_of_snake.append(y_snake)

    snake_list.append(list_of_snake)

    if len(snake_list) > initial_length:
        del snake_list[0]

    aumenta_cobra(snake_list)

    screen.blit(text_format, (380, 40))

    pygame.display.update()
