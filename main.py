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

# Espessura inicial
espessura = 1

# Criar botões com identidade visual unificada
botao_aumentar = Botao(100, 550, 120, 50, "Aumentar", AUMENTAR, BRANCO)
botao_diminuir = Botao(250, 550, 120, 50, "Diminuir", DIMINUIR, BRANCO)

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

        # Mouse - Clique nos botões
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botão esquerdo do mouse
                if botao_aumentar.clique_em_cima(evento.pos):
                    espessura += 1

                elif botao_diminuir.clique_em_cima(evento.pos):
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

    # desenhar_texto(
    #     tela,
    #     "SETA CIMA = aumentar",
    #     650,
    #     50
    # )

    # desenhar_texto(
    #     tela,
    #     "SETA BAIXO = diminuir",
    #     650,
    #     90
    # )

    # desenhar_texto(
    #     tela,
    #     "ou clique nos botões abaixo:",
    #     650,
    #     130
    # )

    # Desenhar botões
    botao_aumentar.desenhar(tela)
    botao_diminuir.desenhar(tela)

    pygame.display.update()

    clock.tick(60)