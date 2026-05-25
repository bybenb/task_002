import pygame
from config import PRETO


pygame.font.init()

fonte = pygame.font.SysFont("Arial", 24)


def desenhar_texto(tela, texto, x, y):

    superficie = fonte.render(
        texto,
        True,
        PRETO
    )

    tela.blit(superficie, (x, y))