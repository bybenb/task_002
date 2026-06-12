import pygame
import sys

from config import *
from renderer import *
from interface import *

pygame.init()

# Janela
tela = pygame.display.set_mode(
    (LARGURA, ALTURA)
)

pygame.display.set_caption(TITULO)

clock = pygame.time.Clock()

espessura = 1

botao_aumentar = Botao(100, 550, 120, 50, "Aumentar", AUMENTAR, BRANCO)
botao_diminuir = Botao(250, 550, 120, 50, "Diminuir", DIMINUIR, BRANCO)

while True:

    # Eventos
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

            # Aumentar espessura
            if evento.key == pygame.K_UP:
                espessura += 1

            # Diminuir espessura
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

    tela.fill(BRANCO)

    desenhar_linha_fina( tela, 100, 200, 900, 200 )

    desenhar_linha_grossa(tela, 100, 400, 900, 400, espessura )

    # Interface
    desenhar_texto( tela, "Linha fina", 100, 160 )

    desenhar_texto( tela, f"Linha grossa - Espessura: {espessura}", 100, 350 )

    
    botao_aumentar.desenhar(tela)
    botao_diminuir.desenhar(tela)

    pygame.display.update()

    clock.tick(60)