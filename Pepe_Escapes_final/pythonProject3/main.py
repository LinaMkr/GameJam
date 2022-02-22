import pygame

from game import Game
import jeu
import rdc
import cadenas
import entry2
import street
import etage1

pygame.init()
pygame.mixer.init()

# générer la fenêtre du jeu
pygame.display.set_caption("Pepe Escapes")
screen = pygame.display.set_mode((1024, 768))

# musique d'ambiance du jeu
pygame.mixer.Channel(0).play(pygame.mixer.Sound('bruitages/The_Expanse.mp3'), -1)

# importer l'arrière plan du jeu
background = pygame.image.load('assets/RDC.png')
background = pygame.transform.scale(background, (1024, 768))

# charger le jeu
game = Game()


def menu():
    click = False
    screen = pygame.display.set_mode((1024, 768))
    backgroundMenu = pygame.image.load('assets/fondMenu.jpg')
    backgroundMenu = pygame.transform.scale(backgroundMenu, (1024, 768))
    screen.blit(backgroundMenu, (0, 0))
    jeu.ecrireTexte("Pepe Escapes", 'fonts/Minecraft.ttf', 100, "#FFFFFF", screen, 500, 150)

    startButton = pygame.image.load('assets/buttons/start_button.png')
    startButton = pygame.transform.scale(startButton, (400, 100))
    screen.blit(startButton, (300, 300))

    optionButton = pygame.image.load('assets/buttons/options_button.png')
    optionButton = pygame.transform.scale(optionButton, (400, 100))
    screen.blit(optionButton, (300, 425))

    creditsButton = pygame.image.load('assets/buttons/credits_button.png')
    creditsButton = pygame.transform.scale(creditsButton, (400, 100))
    screen.blit(creditsButton, (300, 550))
    pepeMenu = pygame.image.load('assets/motions/pepe/Pepe_S_0.png')
    pepeMenu = pygame.transform.scale(pepeMenu, (148, 296))
    screen.blit(pepeMenu, (800, 375))
    mainClock = pygame.time.Clock()
    # mx, my = pygame.mouse.get_pos()
    # print(pygame.mouse.get_pressed())
    while True:
        startButton = pygame.Rect(300, 300, 400, 100)
        optionButton = pygame.Rect(300, 425, 400, 100)
        creditsButton = pygame.Rect(300, 550, 400, 100)

        if startButton.collidepoint(pygame.mouse.get_pos()):
            if click:
                # mettre premier decors
                pygame.mixer.music.load("bruitages/clique.mp3")
                pygame.mixer.music.play()
                #etage1.couloirPremierEtage()
                street.street()
        elif optionButton.collidepoint(pygame.mouse.get_pos()):
            if click:
                pygame.mixer.music.load("bruitages/clique.mp3")
                pygame.mixer.music.play()
                game.option()
        elif creditsButton.collidepoint(pygame.mouse.get_pos()):
            if click:
                pygame.mixer.music.load("bruitages/clique.mp3")
                pygame.mixer.music.play()
                game.credits()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.flip()
        mainClock.tick(60)





menu()
# je sais pas si je dois le mettre la ????
# nope je oense qu'y faudra l'appeler en condition dans le 2 eme etage
# cadenas()
