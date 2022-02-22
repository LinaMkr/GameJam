import pygame
pygame.init()

class Enigma():

    def __init__(self,c_title,c_post_it,c_rect_x,c_rect_y):
        self.title = c_title
        self.post_it = pygame.image.load(c_post_it)
        self.rect = self.post_it.get_rect()
        self.rect.x = c_rect_x
        self.rect.y = c_rect_y

    def size_bloc(self,c_x,c_y):
        self.post_it = pygame.transform.scale(self.post_it, (c_x, c_y))







