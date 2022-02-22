import pygame

# definir une classe qui va s'occuper des animation
class AnimateSprite(pygame.sprite.Sprite):
    #definir les choses à faire à la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')

    # definir une fonction pour charger les images d'un sprite
    def load_animation_images(sprite_name):
        # charger toutes les images de ce sprite dans le dossier correspondant
        images = []
        # récuperer le chemin du dossier pour ce sprite
        path = f"assets/motions/{sprite_name}/{sprite_name}"

    #boucler sur chaque image dans le dossier

