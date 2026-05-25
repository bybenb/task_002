import pygame

from config import *

pygame.font.init()

fonte = pygame.font.SysFont("Arial", 24)
fonte_titulo = pygame.font.SysFont("Arial", 30, bold=True)


def texto(tela, mensagem, x, y, cor=PRETO):

    superficie = fonte.render(
        mensagem,
        True,
        cor
    )

    tela.blit(superficie, (x, y))


def titulo(tela, mensagem, x, y):

    superficie = fonte_titulo.render(
        mensagem,
        True,
        PRETO
    )

    tela.blit(superficie, (x, y))


def botao(
        tela,
        rect,
        cor,
        texto_botao):

    pygame.draw.rect(
        tela,
        cor,
        rect,
        border_radius=10
    )

    txt = fonte.render(
        texto_botao,
        True,
        BRANCO
    )

    tela.blit(
        txt,
        (
            rect.x + 20,
            rect.y + 10
        )
    )