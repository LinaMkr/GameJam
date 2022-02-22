import pygame
import random

pygame.init()

class Monster(pygame.sprite.Sprite):

    def __init__(self, game, c_name, c_health, c_maxHealth, c_attack, c_velocity, c_rect_x, c_rect_y, c_image):
        super().__init__()
        self.game = game
        self.name = c_name
        self.health = c_health
        self.max_health = c_maxHealth
        self.attack = c_attack
        self.velocity = c_velocity
        self.image = c_image
        self.rect = self.image.get_rect()
        self.rect.x = c_rect_x  # 700
        self.rect.y = c_rect_y  # 590
        # taille du petit monstre
        # self.image = c_image
        # self.image = pygame.transform.scale(self.image, ((120, 150)))

    #def taille(self, c_image):
      

    
    def damage(self, amount):
        # infliger les dégats
        self.health -= amount

        # verifier si son nouveau nombre de pv est inf ou egal à 0
        if self.health <= 0:
            # Réapparition du monstre
            self.rect.x = 10024 + random.randint(0, 300)
            self.health = self.max_health


    def update_health_bar(self, surface):
        # definir une couleur pour notre jauge de vie (rouge #EE0000)
        bar_color = (238, 0, 0)
        # definir la couleur de l'arrière plan de la jauge (gris foncé)
        back_bar_color = (60,63,60)

        # definir la position de notre jauge de vie et sa longeur et son épaisseur
        bar_position = [self.rect.x + 40, self.rect.y, self.health, 5]  # w largeur et h la hauteur
        #definir la position de l'arrière plan de la jauge de vie
        back_bar_position = [self.rect.x + 40, self.rect.y, self.max_health, 5]  # w largeur et h la hauteur

        # dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        # le deplacement ne se fait que si y'a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_pepe):
            # le monstre suit le joueur
            if self.rect.x < (self.game.pepe.rect.x):
                self.rect.x += self.velocity

            elif self.rect.x > (self.game.pepe.rect.x):
                self.rect.x -= self.velocity

            if self.rect.y < (self.game.pepe.rect.y):
                self.rect.y += self.velocity

            elif self.rect.y > (self.game.pepe.rect.y):
                self.rect.y -= self.velocity 