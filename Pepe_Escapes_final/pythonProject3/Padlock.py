import pygame
pygame.init()

class Padlock:

    def __init__(self,c_nm,c_lock,c_rect_x,c_rect_y):
        self.nm = c_nm
        self.lock = pygame.image.load(c_lock)
        self.abierto = False
        self.rect = self.lock.get_rect()
        self.rect.x = c_rect_x
        self.rect.y = c_rect_y

    def size_padlock(self,c_x,c_y):
        self.lock = pygame.transform.scale(self.lock, (c_x, c_y))




