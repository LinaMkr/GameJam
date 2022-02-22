import pygame
import jeu

from pygame.locals import *

pygame.init()
pygame.display.set_caption('Credits')
screen = pygame.display.set_mode((1024, 768))
screen_r = screen.get_rect()
font = pygame.font.Font('fonts/Minecraft.ttf', 30)
clock = pygame.time.Clock()

def main():
    mainClock = pygame.time.Clock()
    pygame.display.set_caption('Options')
    screen = pygame.display.set_mode((1024, 768))
    running = True
    while running:
        screen.fill((0, 0, 0))
        jeu.ecrireTexte("Options", 'fonts/Minecraft.ttf', 100, "#FFFFFF", screen, 500, 100)

        iButton = pygame.image.load('assets/buttons/i_button.png')
        iButton = pygame.transform.scale(iButton, (90, 90))
        screen.blit(iButton, (400, 250))

        jeu.ecrireTexte("Interagir", 'fonts/Minecraft.ttf', 50, "#FFFFFF", screen, 200, 300)

        arrowButton = pygame.image.load('assets/buttons/arrows_button.png')
        arrowButton = pygame.transform.scale(arrowButton, (300, 200))
        screen.blit(arrowButton, (650, 350))

        jeu.ecrireTexte("Se deplacer", 'fonts/Minecraft.ttf', 50, "#FFFFFF", screen, 800, 300)

        kButton = pygame.image.load('assets/buttons/k_button.png')
        kButton = pygame.transform.scale(kButton, (90, 90))
        screen.blit(kButton, (400, 350))

        jeu.ecrireTexte("Utiliser cle", 'fonts/Minecraft.ttf', 50, "#FFFFFF", screen, 210, 400)

        mButton = pygame.image.load('assets/buttons/m_button.png')
        mButton = pygame.transform.scale(mButton, (90, 90))
        screen.blit(mButton, (400, 450))

        jeu.ecrireTexte("Manger", 'fonts/Minecraft.ttf', 50, "#FFFFFF", screen, 185, 500)
        jeu.ecrireTexte("Lancer", 'fonts/Minecraft.ttf', 50, "#FFFFFF", screen, 185, 600)

        spaceButton = pygame.image.load('assets/buttons/espace_button.png')
        spaceButton = pygame.transform.scale(spaceButton, (200, 90))
        screen.blit(spaceButton, (400, 550))

        menuButton = pygame.image.load('assets/buttons/Menu_button.png')
        menuButton = pygame.transform.scale(menuButton, (400, 100))
        screen.blit(menuButton, (300, 500))
        menuButton = pygame.Rect(300, 500, 400, 100)
        click = False
        while running:
            if menuButton.collidepoint(pygame.mouse.get_pos()):
                if click:
                    menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()
        mainClock.tick(60)
