
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# Configurações da tela
width = 640
height = 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Speed')
clock = pygame.time.Clock()

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL_CELESTE = (135, 206, 235)
ROXO = (100, 0, 200)
ROSA = (255, 102, 178)
CINZA = (180, 180, 180)
VERMELHO = (255, 70, 70)

font = pygame.font.SysFont('lucidasans', 30, True, False)
font_title = pygame.font.SysFont('lucidasans', 80, True, False)
font_subtitle = pygame.font.SysFont('lucidasans', 24, True, False)
font_small = pygame.font.SysFont('lucidasans', 18, False, False)
font_gameover = pygame.font.SysFont('lucidasans', 55, True, False)

speed = 10
points = 0
last_score = 0

game_state = 'menu'


def carregar_recorde():
    try:
        with open('recorde.txt', 'r') as arquivo:
            return int(arquivo.read())
    except (FileNotFoundError, ValueError):
        return 0


def salvar_recorde(recorde):
    with open('recorde.txt', 'w') as arquivo:
        arquivo.write(str(recorde))


high_score = carregar_recorde()


def iniciar_jogo():
    global x, y, x_pink, y_pink
    global points, speed, game_state

    x = width // 2
    y = height // 2

    x_pink = randint(40, 580)
    y_pink = randint(50, 420)

    points = 0
    speed = 10

    game_state = 'playing'


# Desenhar texto centralizado
def texto_centralizado(texto, fonte, cor, pos_y):
    texto_renderizado = fonte.render(texto, True, cor)

    pos_x = width // 2 - texto_renderizado.get_width() // 2

    screen.blit(texto_renderizado, (pos_x, pos_y))


def finalizar_jogo():
    global game_state, last_score, high_score

    game_state = 'game_over'
    last_score = points

    if last_score > high_score:
        high_score = last_score
        salvar_recorde(high_score)


while True:

    clock.tick(30)

    screen.fill(PRETO)

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:

            if game_state == 'menu':

                if event.key == K_SPACE:
                    iniciar_jogo()

            elif game_state == 'game_over':

                if event.key == K_r:
                    iniciar_jogo()

                elif event.key == K_m:
                    game_state = 'menu'


    if game_state == 'menu':

        texto_centralizado(
            'Speed', font_title, AZUL_CELESTE, 65
        )

        texto_centralizado(
            'COLETE. ACELERE. SOBREVIVA!',
            font_subtitle, BRANCO, 165
        )

        texto_centralizado(
            'Como jogar:', font, AZUL_CELESTE, 225
        )

        texto_centralizado(
            'Use W, A, S e D para movimentar o quadrado roxo.',
            font_small, BRANCO, 270
        )

        texto_centralizado(
            'Colete os quadrados rosas para ganhar pontos.',
            font_small, BRANCO, 300
        )

        texto_centralizado(
            'A cada ponto, sua velocidade aumenta!',
            font_small, BRANCO, 330
        )

        texto_centralizado(
            'Cuidado! Se tocar nas bordas, é GAME OVER.',
            font_small, ROSA, 360
        )

        texto_centralizado(
            f'Maior pontuação: {high_score}',
            font, AZUL_CELESTE, 405
        )

        texto_centralizado(
            'PRESSIONE ESPAÇO PARA COMEÇAR',
            font_subtitle, BRANCO, 445
        )



    elif game_state == 'playing':

        keys = pygame.key.get_pressed()

        if keys[K_a]:
            x -= speed

        if keys[K_d]:
            x += speed

        if keys[K_w]:
            y -= speed

        if keys[K_s]:
            y += speed

        ret_purple = pygame.Rect(x, y, 50, 40)
        ret_pink = pygame.Rect(x_pink, y_pink, 40, 40)

        if (
            x <= 0 or
            x + 50 >= width or
            y <= 0 or
            y + 40 >= height
        ):
            finalizar_jogo()

        else:

            if ret_purple.colliderect(ret_pink):

                x_pink = randint(40, 580)
                y_pink = randint(50, 420)

                points += 1
                speed += 1

        pygame.draw.rect(screen, ROXO, ret_purple)
        pygame.draw.rect(
            screen, ROSA, (x_pink, y_pink, 40, 40)
        )

        texto_centralizado(
            f'Pontos: {points}', font, BRANCO, 20
        )

        texto_centralizado(
            f'Velocidade: {speed}', font_small, AZUL_CELESTE, 60
        )

    elif game_state == 'game_over':

        texto_centralizado(
            'GAME OVER!', font_gameover, VERMELHO, 90
        )

        texto_centralizado(
            'Fim de jogo!', font_subtitle, BRANCO, 165
        )

        texto_centralizado(
            f'Ultima pontuacao: {last_score}',
            font, BRANCO, 225
        )

        texto_centralizado(
            f'Maior pontuacao: {high_score}',
            font, AZUL_CELESTE, 275
        )

        if last_score == high_score and last_score > 0:
            texto_centralizado(
                'NOVO RECORDE!',
                font_subtitle, ROSA, 325
            )

        texto_centralizado(
            'Pressione R para jogar novamente',
            font_small, BRANCO, 385
        )

        texto_centralizado(
            'Pressione M para voltar ao menu',
            font_small, CINZA, 420
        )

    pygame.display.update()
