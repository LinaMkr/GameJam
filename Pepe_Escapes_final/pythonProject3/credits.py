import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Credits')
screen = pygame.display.set_mode((1024, 768))
screen_r = screen.get_rect()
font = pygame.font.Font('fonts/Minecraft.ttf', 30)
clock = pygame.time.Clock()

def main():

    credit_list = ["CREDITS",
                   " ", " ",
                   "GAME CONCEPT",
                   "Asmaa Bel Hadj",
                   "Marion Falcy",
                   "Lina Makri",
                   "Zoe Roelandt",
                   "IUT2 - Grenoble",
                   " ",
                   "PROGRAMMATION",
                   "Asmaa Bel Hadj",
                   "Marion Falcy",
                   "Lina Makri",
                   " ",
                   "GRAPHISMES",
                   "Design du heros - Zoe Roelandt",
                   "Design des decorations - Zoe Roelandt",
                   "Jaquette - Zoe Roelandt",
                   "Design des boutons - Lina Makri",
                   "Illustrations additionnelles - les refs des autres",
                   "City background - Persegan ",
                   "Monstre - LuizMelo",
                   " ",
                   "SCENARIO",
                   "Asmaa Bel Hadj",
                   "Marion Falcy",
                   "Lina Makri",
                   "Zoe Roelandt",
                   " ",
                   "MUSIQUE",
                   "Greg Dombrowski - The Expanse",
                   " ",
                   "BRUITAGES",
                   "LaSonotheque",
                   " ", " ", " ",
                   "MERCI D'AVOIR JOUE A PEPE ESCAPES",
                   "A BIENTOT !",
                   " ", " "
                   ]

    texts = []
    for i, line in enumerate(credit_list):
        surface = font.render(line, 1, (255, 255, 255))
        # on donne la position de départ du text
        rect = surface.get_rect(centerx=screen_r.centerx, y=screen_r.bottom + i * 50)
        texts.append((rect, surface))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        # couleur de fond (blanc)
        screen.fill((0, 0, 0))

        for rect, surface in texts:
            # on déplace chaque rect d'un pixel par image
            rect.move_ip(0, -1)
            # on apllique le texte
            screen.blit(surface, rect)

        # si tous les rects sont sortis de l'ecran, on sort de la page
        if not screen_r.collidelistall([rect for (rect, _) in texts]):
            return

        # mettre a jour l'ecran
        pygame.display.flip()

        # limiter la vitesse du texte à 100 FPS
        clock.tick(100)

