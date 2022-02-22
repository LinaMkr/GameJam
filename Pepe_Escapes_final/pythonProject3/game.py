import pygame
import random
from pygame.locals import *
from pepe import Pepe
from monster import Monster
from inventory import Inventory
from dialog import Dialog
from weapon import Weapon
from item import Item
from enigma import Enigma
from Padlock import Padlock
import credits
import option
import pepe
import jeu

#import entry2

pygame.init()

# créer une classe qui représente le jeu
class Game:

    def __init__(self):
        self.pressed = {}
        # generer le joueur
        self.all_pepe = pygame.sprite.Group()
        self.pepe = Pepe(self)
        self.all_pepe.add(self.pepe)
        self.dialog_box = Dialog()
        # self.button = Credits()
        #groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()

        self.inventory = Inventory(10, 5)

        self.itemFood = Item("conserve", "food", "recuperer", 'assets/food.png', 50, 50)
        self.itemStone = Item("pierre", "stone", "recuperer", 'assets/stone1.png', 900, 50)
        self.itemNote = Item("note", "journal", "lire", 'assets/note.png', 50, 400)
        self.itemKey = Item("cle", "key", "recuperer", 'assets/cle.png', 900, 400)

        # # générer monstres __init__(self, c_name, c_health, c_maxHealth, c_attack, c_velocity, c_rect_x, c_rect_y, c_image)
        # self.little_monster = Monster("Petit Monstre", 10, 10, 5, 5, 700, 600, pygame.image.load('assets/monstre2.png'))
        # self.little_monster = pygame.transform.scale(self.little_monster, (103.2, 105.6))
        # #
        # self.meduim_monster = Monster("Monstre Moyen", 25, 25, 15, 5, 750, 550, pygame.image.load('assets/monstre1.png'))
        # self.meduim_monster = pygame.transform.scale(self.meduim_monster, (172, 176))
        # #
        # self.big_monster = Monster("Grand Monstre", 60, 60, 25, 3, 800, 470, pygame.image.load('assets/monstre1.png'))
        # self.big_monster = pygame.transform.scale(self.big_monster, (258, 264))

        self.enigma = Enigma("Post-it",'assets/post-it.png',500,570)
        self.enigma.size_bloc(10,20)
        self.enigma_2 = Enigma("Post-it 2",'assets/post-it_2.png',400,570)
        self.enigma_2.size_bloc(10,20)
        self.enigma_3 = Enigma("Post-it 3",'assets/post-it_3.png',160,270)
        self.enigma_3.size_bloc(10,20)

        self.padlock = Padlock  ("Cadena",'assets/cadenas.png',855,240)



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) # le mask c la hitbox

    def spawn_monster(self):
        monster = Monster(self, "Monstre Moyen", 25, 25, 15, 3, 750 + random.randint(10,300), 550, pygame.image.load('assets/monstre2.png'))
        monster.image = pygame.transform.scale(monster.image, (172, 176))
        monster.rect = monster.image.get_rect(center=monster.rect.center)
        self.all_monsters.add(monster)

    def handle_input(self):
      pressed = pygame.key.get_pressed()

    def update(self, screen):
      #appliquer l'image du joueur
      screen.blit(self.pepe.image, self.pepe.rect)

    def deplacement(self):
        if self.pressed.get(pygame.K_RIGHT) and self.pepe.rect.x + self.pepe.rect.width < 954:
            self.pepe.move_right()
            self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_E_0.png')
            self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
            print("je vais a droite")
            # aller à gauche
        elif self.pressed.get(pygame.K_LEFT) and self.pepe.rect.x > 70:
            self.pepe.move_left()
            self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_W_0.png')
            self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
            print("je vais a gauche")
            # aller en haut
        elif self.pressed.get(pygame.K_UP) and self.pepe.rect.y > 200:
            self.pepe.move_up()
            self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_N_0.png')
            self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
            print("je vais en haut")
            # aller en bas
        elif self.pressed.get(pygame.K_DOWN) and self.pepe.rect.y + self.pepe.rect.height < 668:
            self.pepe.move_down()
            self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_S_0.png')
            self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
            print("je vais en bas")

    def deplacementToilette(self):
        if self.pressed.get(pygame.K_RIGHT):

            if self.pepe.rect.y < 200 and self.pepe.rect.x < 180 and self.pepe.rect.x + self.pepe.rect.width > 50 or self.pepe.rect.y > 500 and self.pepe.rect.x < 180 and self.pepe.rect.x + self.pepe.rect.width > 50:
                self.pepe.move_right()
                self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_E_0.png')
                self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
                print("je vais a droite j'y arrive")
            elif self.pepe.rect.y > 200 and self.pepe.rect.y < 508 and self.pepe.rect.x + self.pepe.rect.width < 954:
                self.pepe.move_right()
                self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_E_0.png')
                self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
                print("je vais a droite")
        # aller à gauche
        elif self.pressed.get(pygame.K_LEFT) and self.pepe.rect.x > 70:
            self.pepe.move_left()
            self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_W_0.png')
            self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
            print("je vais a gauche")
        # aller en haut
        elif self.pressed.get(pygame.K_UP):
            if self.pepe.rect.x > 50 and self.pepe.rect.x < 200 and self.pepe.rect.y > 190 or self.pepe.rect.y > 250:
                self.pepe.move_up()
                self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_N_0.png')
                self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
                print("je vais en haut")
        # aller en bas
        elif self.pressed.get(pygame.K_DOWN):
            if self.pepe.rect.x > 50 and self.pepe.rect.x < 180 and self.pepe.rect.y + self.pepe.rect.height < 680 or self.pepe.rect.y + self.pepe.rect.height < 508:
                self.pepe.move_down()
                self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_S_0.png')
                self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
                print("je vais en bas")

    def deplacementSecurite(self):
        if self.pressed.get(pygame.K_RIGHT) and self.pepe.rect.x + self.pepe.rect.width < 820:
            self.pepe.move_right()
            self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_E_0.png')
            self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
            print("je vais a droite")
            # aller à gauche
        elif self.pressed.get(pygame.K_LEFT) :
            if self.pepe.rect.x > 320 and self.pepe.rect.y > 330 or self.pepe.rect.x > 410 and self.pepe.rect.y > 240 :
                self.pepe.move_left()
                self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_W_0.png')
                self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
                print("je vais a gauche")
            # aller en haut
        elif self.pressed.get(pygame.K_UP):
            if self.pepe.rect.y > 290 and self.pepe.rect.x > 390 or self.pepe.rect.x > 290 and self.pepe.rect.y > 340:
                self.pepe.move_up()
                self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_N_0.png')
                self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
                print("je vais en haut")
            # aller en bas
        elif self.pressed.get(pygame.K_DOWN) and self.pepe.rect.y + self.pepe.rect.height < 700:
            self.pepe.move_down()
            self.pepe.image = pygame.image.load('assets/motions/pepe/Pepe_S_0.png')
            self.pepe.image = pygame.transform.scale(self.pepe.image, (74, 148))
            print("je vais en bas")

    def enigme(self):
        if self.player.rect.colliderect(self.enigma):
            self.dialog_box.show_enigm_2()
        elif self.player.rect.colliderect(self.enigma_2):
            self.dialog_box.show_enigm_3()
        elif self.player.rect.colliderect(self.enigma_3):
            self.dialog_box.show_enigm_4()

    def interagir(self):
        # Ramasser la clé
        if self.pepe.rect.colliderect(self.itemKey) and self.pressed.get(pygame.K_i) and self.inventory.key == False:
            self.inventory.ramasserKey()
        # ramasser de la nourriture
        elif self.pepe.rect.colliderect(self.itemFood) and self.pressed.get(pygame.K_i):
            self.inventory.ramasserFood()
        # lire une note
        elif self.pepe.rect.colliderect(self.itemNote) and self.pressed.get(pygame.K_i):
            self.inventory.lireNote()
        # ramasser une pierre
        elif self.pepe.rect.colliderect(self.itemStone) and self.pressed.get(pygame.K_i):
            self.inventory.ramasserStone()

    def monstersAttack(self):
        if self.little_monster.rect.colliderect(self.pepe.rect):
            if self.pepe.health > 0:
                self.pepe.health = self.pepe.health - self.little_monster.attack

        elif self.meduim_monster.rect.colliderect(self.pepe.rect):
            self.pepe.health = self.pepe.health - self.meduim_monster.attack
        elif self.big_monster.rect.colliderect(self.pepe.rect):
            self.pepe.health = self.pepe.health - self.big_monster.attack

    def option(self):
        option.main()

    def credits(self):
        credits.main()









