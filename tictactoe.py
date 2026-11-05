
import pygame

pygame.init()

# Cores do jogo
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
cinza = (180, 180, 180)

# Setup da tela
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Jogo da Velha")

# Fontes
fonte = pygame.font.SysFont("Arial", 28)
fonte_menor = pygame.font.SysFont("Arial", 24)

# Variáveis do jogo
position = [0] * 9
x_ou_o = 1

fim = False
vencedor = None
empate = False

clock = pygame.time.Clock()

# Combinações vencedoras
combinacoes = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

# Posições centrais das casas
centros = [
    (125, 125), (286, 125), (446, 125),
    (125, 286), (286, 286), (446, 286),
    (125, 447), (286, 447), (446, 447)
]


# Verifica se existe um vencedor
def verificar_vitoria():
    for combinacao in combinacoes:
        a, b, c = combinacao

        if position[a] == position[b] == position[c] != 0:
            return position[a], combinacao

    return None, None


# Desenha o tabuleiro
def desenhar_tabuleiro():
    window.fill(branco)

    pygame.draw.line(window, preto, (205, 50), (205, 521), 10)
    pygame.draw.line(window, preto, (365, 50), (365, 521), 10)
    pygame.draw.line(window, preto, (50, 205), (521, 205), 10)
    pygame.draw.line(window, preto, (50, 365), (521, 365), 10)

    # Desenha X e O
    for i in range(9):
        x, y = centros[i]

        if position[i] == 1:
            pygame.draw.line(
                window, vermelho,
                (x - 25, y - 25),
                (x + 25, y + 25), 10
            )

            pygame.draw.line(
                window, vermelho,
                (x + 25, y - 25),
                (x - 25, y + 25), 10
            )

        elif position[i] == 2:
            pygame.draw.circle(window, azul, (x, y), 25, 10)


# Desenha a mensagem do jogo
def mostrar_mensagem():
    if not fim:
        jogador = "X" if x_ou_o == 1 else "O"
        mensagem = f"Vez do jogador: {jogador}"

    elif vencedor is not None:
        jogador = "X" if vencedor == 1 else "O"
        mensagem = f"Jogador: {jogador} venceu!!"

    else:
        mensagem = "Empate! Ninguem venceu."

    texto = fonte.render(mensagem, True, preto)

    pos_x = (600 - texto.get_width()) // 2

    window.blit(texto, (pos_x, 10))


# Desenha a linha vencedora
def desenhar_vitoria(combinacao):
    inicio = centros[combinacao[0]]
    final = centros[combinacao[2]]

    pygame.draw.line(window, verde, inicio, final, 10)


# Desenha o botão Restart
def desenhar_botao():
    botao = pygame.Rect(200, 545, 200, 40)

    pygame.draw.rect(
        window, azul, botao,
        border_radius=10
    )

    texto = fonte_menor.render("RESTART", True, branco)

    pos_x = (600 - texto.get_width()) // 2

    window.blit(texto, (pos_x, 552))

    return botao


def reiniciar_jogo():
    global position, x_ou_o, fim, vencedor, empate

    position = [0] * 9
    x_ou_o = 1

    fim = False
    vencedor = None
    empate = False


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            mouse = event.pos

            botao = pygame.Rect(200, 545, 200, 40)

            if fim and botao.collidepoint(mouse):
                reiniciar_jogo()

            elif not fim:

                x, y = mouse

                if 50 <= x <= 521 and 50 <= y <= 521:

                    # Descobre a linha e a coluna
                    if x < 205:
                        coluna = 0
                    elif x < 365:
                        coluna = 1
                    else:
                        coluna = 2

                    if y < 205:
                        linha = 0
                    elif y < 365:
                        linha = 1
                    else:
                        linha = 2

                    pos = linha * 3 + coluna

                    # Verifica se a posição está livre
                    if position[pos] == 0:

                        position[pos] = x_ou_o

                        # Verifica vitória
                        vencedor, combinacao = verificar_vitoria()

                        if vencedor is not None:
                            fim = True

                        # Verifica empate
                        elif 0 not in position:
                            empate = True
                            fim = True

                        # Alterna o jogador
                        else:
                            x_ou_o = 2 if x_ou_o == 1 else 1

    desenhar_tabuleiro()
    mostrar_mensagem()

    if vencedor is not None:
        desenhar_vitoria(combinacao)

    if fim:
        desenhar_botao()

    pygame.display.update()

    clock.tick(60)
