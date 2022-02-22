import pygame

class Dialog:

    def __init__(self):
        self.box = pygame.image.load('assets/Dialog_Box.png')
        self.box = pygame.transform.scale(self.box,(870, 180))
        self.texts = ["Je suis fatigué...Il faut que je reprenne des forces.",
                      "Voyons si je peux trouver de quoi me sustenter !",
                      "je vous conseille de retenir les touches suivantes pour jouer =)",
                      "touche z = voir 2ème indice   |   touche l = voir 3ème indice",
                      "touche c = pour voir ce que pepe a à dire  |  touche d = voir la note de JP",
                    "touche i = pepe recupère des items   |   espace = choisir arme de pepe",
                    "touche m = pepe mange & récupère des items   |   touche espace = attaque",
                    "touche k = ouvre la porte des toilettes",
                    "Première enigme : Combien y a t-il de plantes au premier étages ?",
                    "Deuxième enigme : 1 + 1 = ?",
                    "Troisième enigme : Je suis un nb premier situé entre 15 et 19 & un des chiffres qui me composent est par 3","Dernière enigme : Chiffre manquant = Un chiffre caché dans une des salles du centre commercial"]
        self.texts_index = 0
        self.letter_index = 0
        self.font = pygame.font.SysFont('Calisto MT',22)
        self.reading = False

    def begin(self):
        if self.reading:
            self.nxt_text()
        else:
            self.reading = True
            self.texts_index = 0

    def render(self,screen):
        if self.reading:
            self.letter_index += 1

            if self.letter_index >= len(self.texts[self.texts_index]):
                self.letter_index = self.letter_index

            screen.blit(self.box,(70,620))
            text = self.font.render(self.texts[self.texts_index][0:self.letter_index],False,(0,0,0))
            screen.blit(text,(120,650))

    def nxt_text(self):
        self.texts_index += 1
        self.letter_index = 0

        if self.texts_index == 7: #modife ca
            #fermer le dialog
            self.reading = False

    def show_enigm_2(self):
        if self.reading:
            self.texts_index = 8
            self.texts_index += 1
            self.letter_index = 0

            if self.texts_index >= 8:
                #fermer le dialog
                self.reading = False
        else:
            self.reading = True
            self.texts_index = 8

    def show_enigm_3(self):
        if self.reading:
            self.texts_index = 9
            self.texts_index += 1
            self.letter_index = 0

            if self.texts_index >= 9:
                #fermer le dialog
                self.reading = False
        else:
            self.reading = True
            self.texts_index = 9

    def show_enigm_4(self):
        if self.reading:
            self.texts_index = 10
            self.texts_index += 1
            self.letter_index = 0

            if self.texts_index >= 10:
                #fermer le dialog
                self.reading = False
        else:
            self.reading = True
            self.texts_index = 10

    def show_enigm_5(self):
        if self.reading:
            self.texts_index = 11
            self.texts_index += 1
            self.letter_index = 0

            if self.texts_index >= 11:
                #fermer le dialog
                self.reading = False
        else:
            self.reading = True
            self.texts_index = 11


