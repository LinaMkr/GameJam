import pygame
import jeu
pygame.init()


def gameOver():
    click = False
    #running = True
    screen = pygame.display.set_mode((1024, 768))
    jeu.ecrireTexte("Game Over", 'fonts/Minecraft.ttf', 100, "#FFFFFF", screen, 500, 300)
    jeu.ecrireTexte("Adieu Pepe ... ", 'fonts/Minecraft.ttf', 50, "#FFFFFF", screen, 500, 500)
    # menuButton = pygame.image.load('Asset/buttons/buttons/Menu_button.png')
    # menuButton = pygame.transform.scale(menuButton, (400, 100))
    # screen.blit(menuButton, (300, 500))
    # menuButton = pygame.Rect(300, 500, 400, 100)


    # if menuButton.collidepoint(pygame.mouse.get_pos()):
    #     if click:
    #         self.menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #running = False
                pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        pygame.display.flip()