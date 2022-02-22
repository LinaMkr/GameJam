import pygame
pygame.init()

class Inventory:
    def __init__(self, nb_food, nb_stone):
        self.key = False
        self.food = nb_food
        self.maxFood = 12
        self.foodImage = pygame.image.load("assets/food.png")
        self.rectFood = self.foodImage.get_rect()
        self.stone = nb_stone
        self.maxStone = 10
        self.stoneImage = pygame.image.load("assets/stone1.png")
        self.rectStone = self.stoneImage.get_rect()

    def ramasserFood(self):
        if self.food < self.maxFood:
            self.food = self.food + 1
            print("j'ai ramassé de la nourriture")
        else:
            print("je n'ai plus de place")
        print(self.food)

    def ramasserStone(self):
        if self.stone < self.maxStone:
            self.stone = self.stone + 1
            print("j'ai ramassé une pierre")
        else:
            print("je n'ai plus de place")
        print(self.stone)

    def ramasserKey(self):
        self.key = True
        print("j'ai ramassé THE cle ")

    def lireNote(self):
        print("je lis une note")

    def utiliserFood(self):
        self.food = self.food - 1
        print("j'ai utilisé de la nourriture")
        print(self.food)

    def utiliserStone(self):
        self.stone = self.stone - 1
        print("j'ai utilisé une piere")

