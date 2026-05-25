import pygame


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
            cor,
            (x1, y1 + i),
            (x2, y2 + i),
            1
        )