import pygame
from game import Game
import jeu
import cadenas
import gameOver
pygame.init()

screen = pygame.display.set_mode((1024, 768))
backgroundPremierEtage = pygame.image.load('assets/premier_etage.png')
backgroundPremierEtage = pygame.transform.scale(backgroundPremierEtage, (1024, 768))
screen.blit(backgroundPremierEtage, (0, 0))
game = Game()
screen.blit(game.pepe.image, game.pepe.rect)

def couloirPremierEtage():
    backgroundPremierEtage = pygame.image.load('assets/premier_etage.png')
    backgroundPremierEtage = pygame.transform.scale(backgroundPremierEtage, (1024, 768))
    running = True
    colorBlack = (0, 0, 0)
    colorGray = (113, 102, 100)
    while running:
        if game.pepe.health > 0:
            # appliquer l'arrière plan du jeu
            screen.blit(backgroundPremierEtage, (0, 0))

            # police de caractere pour la barre de point de vie
            jeu.ecrireTexte("PV: ", 'fonts/Minecraft.ttf', 25, "#000000", screen, 30, 30)

            # applique l'inventaire
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

            # recuperper les projectiles du joueur
            for weapon in game.pepe.all_weapons:
                weapon.move(game.pepe.direction)

            # appliquer l'ensemble des images de mon groupe de prjectiles
            game.pepe.all_weapons.draw(screen)

            # appliquer image petit monstre
            #screen.blit(game.little_monster.image, game.little_monster.rect)

            # appliquer image monstre moyen
            #screen.blit(game.meduim_monster.image, game.meduim_monster.rect)

            # appliquer image monstre grand
            #screen.blit(game.big_monster.image, game.big_monster.rect)
            # appliquer l'image du joueur

            # screen.blit(game.weapon.image, game.weapon.rect)
            screen.blit(game.pepe.image, game.pepe.rect)

            # reagrder si le joueur souhaite faire une interaction
            game.interagir()

            # vérifier si le joueur souhaite se déplacer (droite/gauche/haut/bas) et bloque aux bordures
            # aller à droite
            game.deplacement()

            # appliquer barre de vie
            game.pepe.update_health_bar(screen)

            #les montres attaquent
            #game.monstersAttack()

            #rect invisible des toilettes
            entreToilette = pygame.Rect(950, 175, 100, 50)
            entreSecurite = pygame.Rect(50, 175, 50, 50)
            entreProchainEtage = pygame.Rect(500, 175, 50, 50)
            
                
                
            if game.pepe.rect.colliderect(entreToilette):

                pygame.mixer.music.load("bruitages/porte.mp3") #bruitage de la porte
                pygame.mixer.music.play()
                toilette()
            #entrer dans la salle de securité
            elif game.pepe.rect.colliderect(entreSecurite):
                pygame.mixer.music.load("bruitages/porte.mp3") #bruitage de la porte
                pygame.mixer.music.play()
                security()
            #aller au prochain etage
            elif game.pepe.rect.colliderect(entreProchainEtage):
                pygame.mixer.music.load("bruitages/porte.mp3") #bruitage de la porte
                pygame.mixer.music.play()
                # a remplace par le l'appel du prochain etage
                cadenas.cadenas()

            # mettre à jour l'écran
            #pygame.display.flip()

        else:
            gameOver.gameOver()
            # game.menu()
            # si le jouer ferme la fenetre
        for event in pygame.event.get():
            # vérifier que event est fermeture de fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")  # juste pour voir si ça marche, on suppr cette ligne plus tard
            # detecter si le joueur lache une touche de clavier
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                if event.key == pygame.K_SPACE and game.inventory.stone > 0:
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
        pygame.display.flip()


def toilette():
    backgroundToilette = pygame.image.load('assets/toilettes.png')
    backgroundToilette = pygame.transform.scale(backgroundToilette, (1024, 768))

    # appliquer l'arrière plan du jeu
    running = True
    colorBlack = (0, 0, 0)
    colorGray = (113, 102, 100)
    game.pepe.rect.x = 80
    game.pepe.rect.y = 400
    while running:
        if game.pepe.health > 0:

            screen.blit(backgroundToilette, (0, 0))
            # police de caractere pour la barre de point de vie
            jeu.ecrireTexte("PV: ", 'fonts/Minecraft.ttf', 25, "#000000", screen, 30, 30)

            # inventaire

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

            # recuperper les projectiles du joueur
            for weapon in game.pepe.all_weapons:
                weapon.move(game.pepe.direction)

            # appliquer l'ensemble des images de mon groupe de prjectiles
            game.pepe.all_weapons.draw(screen)

            # appliquer image petit monstre
            #screen.blit(game.little_monster.image, game.little_monster.rect)

            # appliquer image monstre moyen
            # screen.blit(game.meduim_monster.image, game.meduim_monster.rect)

            # appliquer image monstre grand
            # screen.blit(game.big_monster.image, game.big_monster.rect)
            # appliquer l'image du joueur

            # screen.blit(game.weapon.image, game.weapon.rect)
            screen.blit(game.pepe.image, game.pepe.rect)

            # reagrder si le joueur souhaite faire une interaction
            game.interagir()

            # vérifier si le joueur souhaite se déplacer (droite/gauche/haut/bas) et bloque aux bordures
            # aller à droite
            game.deplacementToilette() 
 
                       
            # rect invisible des toilettes
            sortieToilette = pygame.Rect(50, 670, 150, 50)

            # entrez dans les toilettes
            if game.pepe.rect.colliderect(sortieToilette):
              pygame.mixer.music.load("bruitages/porte.mp3") #bruitage de la porte
              pygame.mixer.music.play()
              couloirPremierEtage()


            # mettre à jour l'écran
            pygame.display.flip()

        else:
            gameOver.gameOver()
            # game.menu()
            # si le jouer ferme la fenetre
        for event in pygame.event.get():
            # vérifier que event est fermeture de fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")  # juste pour voir si ça marche, on suppr cette ligne plus tard
            # detecter si le joueur lache une touche de clavier
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                if event.key == pygame.K_SPACE and game.inventory.stone > 0:
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

def security():

    backgroundSecurity = pygame.image.load('assets/securite.png')
    backgroundSecurity = pygame.transform.scale(backgroundSecurity, (1024, 768))

    # appliquer l'arrière plan du jeu
    running = True
    colorBlack = (0, 0, 0)
    colorGray = (113, 102, 100)

    game.pepe.rect.x = 500
    game.pepe.rect.y = 500
    while running:
        if game.pepe.health > 0:

            screen.blit(backgroundSecurity, (0, 0))
            # police de caractere pour la barre de point de vie
            jeu.ecrireTexte("PV: ", 'fonts/Minecraft.ttf', 25, "#000000", screen, 30, 30)

            # inventaire

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

            # recuperper les projectiles du joueur
            for weapon in game.pepe.all_weapons:
                weapon.move(game.pepe.direction)

            # appliquer l'ensemble des images de mon groupe de prjectiles
            game.pepe.all_weapons.draw(screen)

            # appliquer image petit monstre
            #screen.blit(game.little_monster.image, game.little_monster.rect)

            # appliquer image monstre moyen
            # screen.blit(game.meduim_monster.image, game.meduim_monster.rect)

            # appliquer image monstre grand
            # screen.blit(game.big_monster.image, game.big_monster.rect)
            # appliquer l'image du joueur

            # screen.blit(game.weapon.image, game.weapon.rect)
            screen.blit(game.pepe.image, game.pepe.rect)

            # reagrder si le joueur souhaite faire une interaction
            game.interagir()

            # vérifier si le joueur souhaite se déplacer (droite/gauche/haut/bas) et bloque aux bordures
            # aller à droite
            game.deplacementSecurite()
            # appliquer barre de vie
         
            game.pepe.update_health_bar(screen)
              
               

            # les montres attaquent
            # game.monstersAttack()

            # rect invisible des toilettes
            sortieSecurite = pygame.Rect(500, 700, 50, 50)  
            #le jouer ferme la fenetre
            # entrez dans les toilettes
            if game.pepe.rect.colliderect(sortieSecurite):
              pygame.mixer.music.load("bruitages/porte.mp3") #bruitage de la porte
              pygame.mixer.music.play() 
              couloirPremierEtage()


            # mettre à jour l'écran
            pygame.display.flip()

        else:
            gameOver.gameOver()
            # game.menu()
            # si le jouer ferme la fenetre
        for event in pygame.event.get():
            # vérifier que event est fermeture de fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")  # juste pour voir si ça marche, on suppr cette ligne plus tard
            # detecter si le joueur lache une touche de clavier
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                if event.key == pygame.K_SPACE and game.inventory.stone > 0:
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