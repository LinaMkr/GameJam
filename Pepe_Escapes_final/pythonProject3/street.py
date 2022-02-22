import pygame
import entry
from game import Game
pygame.init()
pygame.mixer.init()

def street():
  
  #générer la fenêtre du jeu
  pygame.display.set_caption("Pepe Escapes")
  screen = pygame.display.set_mode((1024, 768))
  
  #charger le jeu
  game = Game()
  
  running = True
  
  # boucle tant que la page est en route
  while running:
  
    # importer l'arrière plan du jeu
    background = pygame.image.load('assets/city_bg.jpg')
    background = pygame.transform.scale(background, (1380, 768))
  
    game.handle_input()
    # appliquer l'arrière plan du jeu
    screen.blit(background, (0, 0))
  
    # appliquer le bouton credits
    #screen.blit(game.button.image, game.button.rect)
  
    # appliquer l'image du joueur
    screen.blit(game.pepe.image, game.pepe.rect)
  
    # actualiser l'image du joueur
    game.update(screen)
  
    # rectangle pour entrer dans le centre commercial
    # pygame.draw.rect(screen, "blue", (280, 470, 5, 250))
    outside_mall_door = pygame.Rect(0, 0, 5, 250)
  
    # recupere les projectiles du joueur
    for weapon in game.pepe.all_weapons:
        weapon.move(game.pepe.direction)
  
    # appliquer l'ensemble des images de mon groupe de prjectiles
    game.pepe.all_weapons.draw(screen)
    game.interagir()
    # appliquer image petit monstre
    # screen.blit(game.little_monster.image, game.little_monster.rect)
    #
    # # appliquer image monstre moyen
    # screen.blit(game.meduim_monster.image, game.meduim_monster.rect)
    #
    # # appliquer image monstre grand
    # screen.blit(game.big_monster.image, game.big_monster.rect)
  
    # appliquer l'ensmble des images de mon groupe de monstres
    game.all_monsters.draw(screen)
  
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
    elif game.pressed.get(pygame.K_UP) and game.pepe.rect.y > 0:
      game.pepe.move_up()
      game.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_N_0.png')
      game.pepe.image = pygame.transform.scale(game.pepe.image, (74, 148))
    # aller en bas
    elif game.pressed.get(pygame.K_DOWN) and game.pepe.rect.y + game.pepe.rect.height + 50 < screen.get_height():
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
  
  
    # mettre à jour l'écran
    pygame.display.flip()
  
  
    #si le jouer ferme la fenetre
    for event in pygame.event.get():
      #vérifier que event est fermeture de fenetre
      if event.type == pygame.QUIT:
        running = False
        pygame.quit()
        print("Femeture du jeu") #juste pour voir si ça marche, on suppr cette ligne plus tard
      # detecter si le joueur lache une touche de clavier
      elif event.type == pygame.KEYDOWN:
        game.pressed[event.key] = True
  
        # detecter si la touche espace est pressé pour lancer un weapon
        if event.key == pygame.K_SPACE:
          game.pepe.launch_weapon()
  
      elif event.type == pygame.KEYUP:
        game.pressed[event.key] = False
      # elif event.type == pygame.MOUSEBUTTONUP:
      #   game.button.check_position()
  
    if outside_mall_door.collidepoint((outside_mall_door.x, game.pepe.rect.x)):
        pygame.mixer.music.load("bruitages/porte.mp3")
        pygame.mixer.music.play()
        entry.entry()
