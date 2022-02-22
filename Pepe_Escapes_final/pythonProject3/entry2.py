import pygame
from game import Game
import etage1
pygame.init()


def entry2():

    #générer la fenêtre du jeu
    pygame.display.set_caption("Pepe Escapes")
    screen = pygame.display.set_mode((1024, 768))

    #importer l'arrière plan du jeu
    background = pygame.image.load('assets/RDC.png')
    background = pygame.transform.scale(background, (1024, 768))

    #charger le jeu
    game = Game()

    running = True

    game.pepe.rect.x = 350
    game.pepe.rect.y = 250

    nuit = pygame.Surface((1024, 768))
    nuit.fill(pygame.Color('black'))
    nuit.set_alpha(100)
    # boucle tant que  la page est en route
    while running:
        # faire un filtre sur background

        # mettre un filtre
        # appliquer l'arrière plan du jeu
        screen.blit(background, (0, 0))

        screen.blit(nuit, (0, 0))
        game.handle_input()
        # appliquer l'image du joueur
        screen.blit(game.pepe.image, game.pepe.rect)

        # actualiser l'image du joueur
        game.update(screen)

        # rectangle pour entrer dans le centre commercial
        # pygame.draw.rect(screen, "blue", (340, 340, 80, 5))
        escalier1 = pygame.Rect(340, 340, 80, 5)
        # pygame.draw.rect(screen, "red", (470, 400, 50, 5))
        # escalier1 = pygame.Rect(470, 400, 50, 5)

        # recuperper les projectiles du joueur
        for weapon in game.pepe.all_weapons:
            weapon.move(game.pepe.direction)

        # appliquer l'ensemble des images de mon groupe de projectiles
        game.pepe.all_weapons.draw(screen)

        # appliquer l'ensmble des images de mon groupe de monstres
        game.all_monsters.draw(screen)
        game.interagir()
        # récuperer les monstres du jeu
        for monster in game.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

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

        # attaque monstre
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

                if event.key == pygame.K_SPACE:
                    game.inventory.stone = game.inventory.stone - 1
                    game.pepe.launch_weapon()
                elif game.pressed.get(pygame.K_m) and game.inventory.food > 0:

                    if game.pepe.health < game.pepe.max_health - 9:
                        game.inventory.utiliserFood()
                        game.pepe.health = game.pepe.health + 10
                    elif game.pepe.health < game.pepe.max_health and game.pepe.health > 90:
                        game.pepe.health = game.pepe.health + (game.pepe.max_health - game.pepe.health)
                        game.inventory.utiliserFood()
                    else:
                        print("ma santé est au top du top")

                    print("ma sante est de : ")
                    print(game.pepe.health)

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     game.button.check_position()

        if escalier1.collidepoint((escalier1.y, game.pepe.rect.y+120)) and escalier1.collidepoint((escalier1.x, game.pepe.rect.x-130)):
            pygame.mixer.music.load("bruitages/porte.mp3")
            pygame.mixer.music.play()
            etage1.couloirPremierEtage()
