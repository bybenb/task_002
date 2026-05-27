import pygame
from config import LINHA_COR


def desenhar_linha_fina(tela, x1, y1, x2, y2):

    pygame.draw.line(
        tela,
        LINHA_COR,
        (x1, y1),
        (x2, y2),
        1
    )


def desenhar_linha_grossa(
        tela,
        cor,
        inicio,
        fim,
        espessura):

    x1, y1 = inicio
    x2, y2 = fim

    # Simulação com linhas paralelas

    for i in range(espessura):

        pygame.draw.line(
            tela,
            LINHA_COR,
            (x1, y1 + i),
            (x2, y2 + i),
            1
        )