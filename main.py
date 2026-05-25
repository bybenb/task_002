import pygame
import sys

from config import *
from renderer import *
from interface import *

pygame.init()

tela = pygame.display.set_mode(
    (LARGURA, ALTURA)
)

pygame.display.set_caption(TITULO)

clock = pygame.time.Clock()

# Configurações iniciais

espessura = 5
cor_atual = AZUL

desenhando = False
ponto_inicial = None
ponto_final = None

# Botões

botao_azul = pygame.Rect(40, 150, 200, 50)
botao_vermelho = pygame.Rect(40, 220, 200, 50)
botao_verde = pygame.Rect(40, 290, 200, 50)

while True:

    # Eventos

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Clique do rato

        if evento.type == pygame.MOUSEBUTTONDOWN:

            mouse = pygame.mouse.get_pos()

            # Escolher cor

            if botao_azul.collidepoint(mouse):
                cor_atual = AZUL

            elif botao_vermelho.collidepoint(mouse):
                cor_atual = VERMELHO

            elif botao_verde.collidepoint(mouse):
                cor_atual = VERDE

            else:
                desenhando = True
                ponto_inicial = mouse

        if evento.type == pygame.MOUSEBUTTONUP:

            desenhando = False

        # Movimento do rato

        if evento.type == pygame.MOUSEMOTION:

            if desenhando:
                ponto_final = pygame.mouse.get_pos()

        # Teclado

        if evento.type == pygame.KEYDOWN:

            # aumentar espessura

            if evento.key == pygame.K_UP:
                espessura += 1

            # diminuir espessura

            if evento.key == pygame.K_DOWN:

                if espessura > 1:
                    espessura -= 1

    # Fundo

    tela.fill(BRANCO)

    # Painel lateral

    pygame.draw.rect(
        tela,
        CINZA,
        (0, 0, LARGURA_MENU, ALTURA)
    )

    # Títulos

    titulo(
        tela,
        "CONTROLO",
        70,
        40
    )

    # Botões

    botao(
        tela,
        botao_azul,
        AZUL,
        "Azul"
    )

    botao(
        tela,
        botao_vermelho,
        VERMELHO,
        "Vermelho"
    )

    botao(
        tela,
        botao_verde,
        VERDE,
        "Verde"
    )

    # Informações

    texto(
        tela,
        f"Espessura: {espessura}",
        40,
        400
    )

    texto(
        tela,
        "SETA CIMA = +",
        40,
        450
    )

    texto(
        tela,
        "SETA BAIXO = -",
        40,
        490
    )

    texto(
        tela,
        "Desenhe com o rato",
        40,
        560
    )

    # Área de desenho

    pygame.draw.rect(
        tela,
        BRANCO,
        (
            LARGURA_MENU,
            0,
            LARGURA - LARGURA_MENU,
            ALTURA
        )
    )

    # Linha desenhada

    if ponto_inicial and ponto_final:

        desenhar_linha_grossa(
            tela,
            cor_atual,
            ponto_inicial,
            ponto_final,
            espessura
        )

    pygame.display.update()

    clock.tick(60)