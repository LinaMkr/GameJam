import pygame
from weapon import Weapon

pygame.init()

#classe Pepe
class Pepe(pygame.sprite.Sprite):

    def __init__(self, game):
      super().__init__()
      self.game = game
      self.health = 50
      self.max_health = 100
      self.attack = 5
      self.velocity = 10
      self.direction = "right"
      self.all_weapons = pygame.sprite.Group()
      self.image = pygame.image.load('assets/motions/pepe/Pepe_S_0.png')
      self.image = pygame.transform.scale(self.image, (74, 148))
      self.rect = self.image.get_rect()
      self.rect.x = 400
      self.rect.y = 580
      
    def launch_weapon(self):
      pygame.mixer.music.load("bruitages/lancer.mp3")
      pygame.mixer.music.play()
      # creer un instance de la classe Weapon
      self.all_weapons.add(Weapon("stone", 15, 'assets/stone1.png', 20, self))

    def move_right(self):
      # si le joueur n'est pas en collision avec un monstre
      if not self.game.check_collision(self, self.game.all_monsters):
        self.rect.x += self.velocity
        self.direction = "right"

    def move_left(self):
      self.rect.x -= self.velocity
      self.direction = "left"
  
    def move_up(self):
      if not self.game.check_collision(self, self.game.all_monsters):
        self.rect.y -= self.velocity
        self.direction = "back"
  
    def move_down(self):
      self.rect.y += self.velocity
      self.direction = "front"

    def update_health_bar(self, surface):
        colorBlack = (0,0,0)
        colorRed = (238,0,0)
        pygame.draw.rect(surface, colorBlack, [50, 25, self.max_health, 10])
        pygame.draw.rect(surface, colorRed, [50, 25, self.health, 10])
