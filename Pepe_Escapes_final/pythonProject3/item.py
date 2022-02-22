import pygame
pygame.init()

class Item:
    def __init__(self, c_nom, c_category, c_interaction, c_image, c_rect_x, c_rect_y):
        self.nom = c_nom
        self.category = c_category
        self.interaction = c_interaction
        self.image = pygame.image.load(c_image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = c_rect_x
        self.rect.y = c_rect_y
        # self.imageFood = pygame.image.load(c_image)
        # self.imageStone = pygame.image.load(c_image)
        # self.imageNote = pygame.image.load(c_image)
        #
        # self.imageFood = pygame.transform.scale(self.imageFood, (50,50))
        # self.rectFood = self.imageFood.get_rect()
        # self.rectFood.x = c_rect_x
        # self.rectFood.y = c_rect_y
        #
        # self.imageStone = pygame.transform.scale(self.imageStone, (50,50))
        # self.rectStone = self.imageStone.get_rect()
        # self.rectStone.x = c_rect_x
        # self.rectStone.y = c_rect_y
        #
        #pour changer la taille de la cle dans le jeu
        self.imageKey = pygame.image.load(c_image)
        self.imageKey = pygame.transform.scale(self.imageKey, (10, 5))
        self.rectKey = self.imageKey.get_rect()
        self.rectKey.x = c_rect_x
        self.rectKey.y = c_rect_y

        # pour changer la taille de la cle dans l'inventaire
        self.imageKeyInventaire = pygame.image.load(c_image)
        self.imageKeyInventaire = pygame.transform.scale(self.imageKeyInventaire, (50, 25))
        self.rectKeyInventaire = self.imageKeyInventaire.get_rect()
        self.rectKeyInventaire.x = c_rect_x
        self.rectKeyInventaire.y = c_rect_y
        #
        # self.imageNote = pygame.transform.scale(self.imageNote, (20, 50))
        # self.rectNote = self.imageNote.get_rect()
        # self.rectNote.x = c_rect_x
        # self.rectNote.y = c_rect_y
