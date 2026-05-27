import pygame
from config import PRETO, CINZA_CLARO, VERMELHO, VERDE


pygame.font.init()

fonte = pygame.font.SysFont("Arial", 24)
fonte_botao = pygame.font.SysFont("Arial", 18, bold=True)


def desenhar_texto(tela, texto, x, y):

    superficie = fonte.render(
        texto,
        True,
        PRETO
    )

    tela.blit(superficie, (x, y))


class Botao:
    def __init__(self, x, y, largura, altura, texto, cor_fundo, cor_texto):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor_fundo = cor_fundo
        self.cor_texto = cor_texto
        self.clicado = False

    def desenhar(self, tela):
        # Desenha o botão
        pygame.draw.rect(tela, self.cor_fundo, self.rect)
        pygame.draw.rect(tela, PRETO, self.rect, 2)  # Borda

        # Desenha o texto
        superficie = fonte_botao.render(self.texto, True, self.cor_texto)
        texto_rect = superficie.get_rect(center=self.rect.center)
        tela.blit(superficie, texto_rect)

    def clique_em_cima(self, pos):
        return self.rect.collidepoint(pos)