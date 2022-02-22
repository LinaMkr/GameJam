import pygame
from game import Game
import entry
import credits
pygame.init()

def cadenas():

      DARK = (0, 0, 0)
      GREEN = (40, 230, 120)

      #générer la fenêtre du jeu
      pygame.display.set_caption("Pepe Escapes")
      screen = pygame.display.set_mode((1024, 768))

      #importer l'arrière plan du jeu
      # à changer TRES IMPORTANT
      background = pygame.image.load('assets/dernier_etage.png')
      background = pygame.transform.scale(background, (1024, 768))

      #carré noire supporte le input de l'user + txt
      cade = pygame.Surface((200, 368))
      cade = pygame.transform.scale(cade,(350,250))
      cade.fill(pygame.Color('black'))
      cade.set_alpha(100)

      #position du text que user entre
      center_x, center_y = 440, 390



      #charger le jeu
      game = Game()

      running = True

      game.pepe.rect.x = 845
      game.pepe.rect.y = 571

      # boucle tant que  la page est en route
      while running:

          # appliquer l'arrière plan du jeu
          screen.blit(background, (0, 0))

          # appliquer l'image du joueur
          screen.blit(game.pepe.image, game.pepe.rect)

          # actualiser l'image du joueur
          game.update(screen)

          # rectangle pour show le input
          touch_cadenas = pygame.Rect(855,240, 90, 105)
          #read_cadenas.set_alpha(100)

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
          elif game.pressed.get(pygame.K_UP) and game.pepe.rect.y > 300 - game.pepe.rect.height:
              game.pepe.move_up()
              game.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_N_0.png')
              game.pepe.image = pygame.transform.scale(game.pepe.image, (74, 148))
          # aller en bas
          elif game.pressed.get(pygame.K_DOWN) and game.pepe.rect.y + game.pepe.rect.height < screen.get_height():
              game.pepe.move_down()
              game.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_S_0.png')
              game.pepe.image = pygame.transform.scale(game.pepe.image, (74, 148))

          # # attaque monstre
          # if game.all_monsters.rect.colliderect(game.pepe.rect):
          #   if game.pepe.health > 0:
          #     game.pepe.health = game.pepe.health - game.all_monsters.attack

          # elif game.meduim_monster.rect.colliderect(game.pepe.rect):
          #   game.pepe.health = game.pepe.health - game.meduim_monster.attack
          # elif game.big_monster.rect.colliderect(game.pepe.rect):
          #   game.pepe.health = game.pepe.health - game.big_monster.attack
          game.deplacement()
          rectControle = pygame.Rect(100,200, 100, 50)
          if game.pepe.rect.colliderect(rectControle):
                credits.main()

          # mettre à jour l'écran
          pygame.display.flip()
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


          # # si le jouer ferme la fenetre
          # for event in pygame.event.get():
          #     # vérifier que event est fermeture de fenetre
          #     if event.type == pygame.QUIT:
          #         running = False
          #         pygame.quit()
          #         print("Femeture du jeu")  # juste pour voir si ça marche, on suppr cette ligne plus tard
          #     # detecter si le joueur lache une touche de clavier
          #     elif event.type == pygame.KEYDOWN:
          #         game.pressed[event.key] = True
          #
          #         if event.key in (pygame.K_RETURN,pygame.K_KP_ENTER):
          #             break
          #         elif event.key == pygame.K_BACKSPACE:
          #             user_input_value = user_input_value[:1]
          #         else:
          #             user_input_value += event.unicode
          #         user_input = font.render(user_input_value,True,GREEN)
          #         user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
          #
          #
          #         # detecter si la touche espace est pressé pour lancer un weapon
          #         if event.key == pygame.K_SPACE:
          #             game.pepe.launch_weapon()
          #
          #     elif event.type == pygame.KEYUP:
          #         game.pressed[event.key] = False
          #     # elif event.type == pygame.MOUSEBUTTONUP:
          #     #     game.button.check_position()
          #
          # if game.pepe.rect.colliderect(touch_cadenas):
          #       credits.main()

def read_cadena():
    DARK = (0, 0, 0)
    GREEN = (40, 230, 120)
    click_cadenas = False
    background = pygame.image.load('assets/dernier_etage.png')
    background = pygame.transform.scale(background, (1024, 768))
    cade = pygame.Surface((200, 368))
    cade = pygame.transform.scale(cade, (350, 250))
    cade.fill(pygame.Color('black'))
    cade.set_alpha(100)
    # pygame.display.flip()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 28)
    prompt = font.render('Entrez le code secret : ', True, DARK)
    #position du text que user entre
    center_x, center_y = 440, 390
    prompt_rect = prompt.get_rect(center=(center_x, center_y))

    user_input_value = ""
    user_input = font.render(user_input_value, True, GREEN)
    user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
    while True:
        #carré noire supporte le input de l'user + txt
        cade = pygame.Surface((200, 368))
        cade = pygame.transform.scale(cade,(350,250))
        cade.fill(pygame.Color('black'))
        cade.set_alpha(100)


        clock = pygame.time.Clock()
        font = pygame.font.SysFont('Arial', 28)
        prompt = font.render('Entrez le code secret : ', True, DARK)
        prompt_rect = prompt.get_rect(center=(center_x, center_y))

        user_input_value = ""
        user_input = font.render(user_input_value, True, GREEN)
        user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

        #ds la boucle
        # rectangle pour entrer dans le centre commercial
        pygame.draw.rect(screen, "blue", (750, 780, 180, 5))
        read_cadenas = pygame.Rect(750, 780, 180, 5)
             #read_cadenas.set_alpha(100)

        if event.key in (pygame.K_RETURN,pygame.K_KP_ENTER):
            break
        elif event.key == pygame.K_BACKSPACE:
            user_input_value = user_input_value[:1]


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     game.button.check_position()


            if sortie_epicerie.collidepoint((read_cadenas.y, game.pepe.rect.y +200)):
             entry2.entry2()
        else:
                user_input_value += event.unicode
                user_input = font.render(user_input_value, True, GREEN)
                user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
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

                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        user_input_value = user_input_value[:1]
                    else:
                        user_input_value += event.unicode
                    user_input = font.render(user_input_value, True, GREEN)
                    user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

                    # detecter si la touche espace est pressé pour lancer un weapon
                    if event.key == pygame.K_SPACE:
                        game.pepe.launch_weapon()

                elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False
                # elif event.type == pygame.MOUSEBUTTONUP:
                #     game.button.check_position()