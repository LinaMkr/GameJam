import pygame
from game import Game
import epicerie
import jeu
pygame.init()


def entry():

    #générer la fenêtre du jeu
    pygame.display.set_caption("Pepe Escapes")
    screen = pygame.display.set_mode((1024, 768))

    #importer l'arrière plan du jeu
    background = pygame.image.load('assets/RDC.png')
    background = pygame.transform.scale(background, (1024, 768))

    #charger le jeu
    game = Game()

    running = True

    game.pepe.rect.x += 90

    colorBlack = (0,0,0)
    colorGray = (113,102,100)
    # boucle tant que  la page est en route
    while running:

        game.handle_input()
        # appliquer l'arrière plan du jeu
        screen.blit(background, (0, 0))

        # appliquer le bouton credits
        # screen.blit(game.button.image, game.button.rect)
        # inventaire
        # police de caractere pour la barre de point de vie
        jeu.ecrireTexte("PV: ", 'fonts/Minecraft.ttf', 25, "#000000", screen, 30, 30)
        pygame.draw.rect(screen, colorBlack, [450, 25, 300, 50])
        pygame.draw.rect(screen, colorGray, [450, 25, 300, 50])
        pygame.draw.line(screen, colorBlack, [550, 25], [550, 74])
        pygame.draw.line(screen, colorBlack, [650, 25], [650, 74])
        screen.blit(game.itemFood.image, (465, 25))
        screen.blit(game.itemStone.image, (565, 25))
        screen.blit(game.itemKey.imageKeyInventaire, (665, 40))

        jeu.ecrireTexte("x" + str(game.inventory.food), 'fonts/Minecraft.ttf', 20, "#000000", screen,
                        525, 65)
        jeu.ecrireTexte("x" + str(game.inventory.stone), 'fonts/Minecraft.ttf', 20, "#000000", screen,
                        625, 65)

        if game.inventory.key:
            jeu.ecrireTexte("x1", 'fonts/Minecraft.ttf', 20, "#000000", screen, 725, 65)
        else:
            jeu.ecrireTexte("x0", 'fonts/Minecraft.ttf', 20, "#000000", screen, 725, 65)
        jeu.ecrireTexte("Vos objets : ", 'fonts/Minecraft.ttf', 25, "#000000", screen, 530, 15)

        # appliquer l'image du joueur
        screen.blit(game.pepe.image, game.pepe.rect)

        # actualiser l'image du joueur
        game.update(screen)

        # rectangle pour entrer dans le centre commercial
        # pygame.draw.rect(screen, "blue", (340, 340, 80, 5))
        entree_epicerie = pygame.Rect(340, 340, 80, 5)

        # recuperper les projectiles du joueur
        for weapon in game.pepe.all_weapons:
            weapon.move(game.pepe.direction)

        # appliquer l'ensemble des images de mon groupe de prjectiles
        game.pepe.all_weapons.draw(screen)

        # vérifier si le joueur souhaite se déplacer (droite/gauche/haut/bas) et bloque aux bordures
        # aller à droite
        if game.pressed.get(pygame.K_RIGHT) and game.pepe.rect.x + game.pepe.rect.width < screen.get_width():
            game.pepe.move_right()
            game.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_E_0.png')
            game.pepe.image = pygame.transform.scale(game.pepe.image, (74, 148))
        # aller à gauche
        elif game.pressed.get(pygame.K_LEFT) and game.pepe.rect.x > 0:
            game.pepe.move_left()
            game.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_W_0.png')
            game.pepe.image = pygame.transform.scale(game.pepe.image, (74, 148))
        # aller en haut
        elif game.pressed.get(pygame.K_UP) and game.pepe.rect.y > 370 - game.pepe.rect.height:
            game.pepe.move_up()
            game.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_N_0.png')
            game.pepe.image = pygame.transform.scale(game.pepe.image, (74, 148))
        # aller en bas
        elif game.pressed.get(pygame.K_DOWN) and game.pepe.rect.y + game.pepe.rect.height < screen.get_height():
            game.pepe.move_down()
            game.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_S_0.png')
            game.pepe.image = pygame.transform.scale(game.pepe.image, (74, 148))

        game.interagir()


        # appliquer barre de vie
        game.pepe.update_health_bar(screen)

        # les monstres attaquent
        #game.monstersAttack()

        # # attaque monstre
        # if game.all_monsters.rect.colliderect(game.pepe.rect):
        #   if game.pepe.health > 0:
        #     game.pepe.health = game.pepe.health - game.all_monsters.attack

        # elif game.meduim_monster.rect.colliderect(game.pepe.rect):
        #   game.pepe.health = game.pepe.health - game.meduim_monster.attack
        # elif game.big_monster.rect.colliderect(game.pepe.rect):
        #   game.pepe.health = game.pepe.health - game.big_monster.attack

        # mettre à jour l'écran
        pygame.display.flip()

        # si le jouer ferme la fenetre
        for event in pygame.event.get():
            # vérifier que event est fermeture de fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Femeture du jeu")  # juste pour voir si ça marche, on suppr cette ligne plus tard
            # detecter si le joueur lache une touche de clavier
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                # detecter si la touche espace est pressé pour lancer un weapon
                if event.key == pygame.K_SPACE :
                    game.pepe.launch_weapon()

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     game.button.check_position()

        if entree_epicerie.collidepoint((entree_epicerie.y, game.pepe.rect.y+120)) and entree_epicerie.collidepoint((entree_epicerie.x, game.pepe.rect.x-10)):
            pygame.mixer.music.load("bruitages/porte.mp3")
            pygame.mixer.music.play()
            epicerie.epicerie()
