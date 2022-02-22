import pygame
pygame.init()

class Weapon(pygame.sprite.Sprite):

  #constructeur de la classe
    def __init__(self, c_name, c_attack, c_image, c_velocity, pepe):
        super().__init__()
        self.name = c_name
        self.attack = c_attack
        self.image = pygame.image.load(c_image)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = pepe.rect.x + 20
        self.rect.y = pepe.rect.y + 60
        self.velocity = c_velocity
        self.pepe = pepe
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectile
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.pepe.all_weapons.remove(self)

    def move(self, direction):
        if direction == "right":
            self.rect.x += self.velocity
        elif direction == "left":
            self.rect.x -= self.velocity
        elif direction == "front":
            self.rect.y += self.velocity
        elif direction == "back":
            self.rect.y -= self.velocity
        # verifier si le projectile entre en collision avec un monstre
        for monster in self.pepe.game.check_collision(self, self.pepe.game.all_monsters):
          # supprimer le projectile
          self.remove()
          # infliger des dégats
          monster.damage(self.pepe.attack)
          self.velocity

        self.rotate()

        # verifier si le prjectile n'est plus present sur l'ecran
        if self.rect.x > 1024 or self.rect.x < -20 or self.rect.y > 768 or self.rect.y < -20:
            #supprimer le projectile
            self.remove()