import pygame
pygame.init()


def ecrireTexte(text, font, taille, color, surface, x, y):
    fontName = pygame.font.Font(font, taille)
    textobj = fontName.render(text, True, pygame.Color(color))
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)



