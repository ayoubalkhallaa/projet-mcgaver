"""Classes of the MCGAVER Labyrinth Game"""

import pygame
from pygame.locals import *
from constantes import *
from random import *


class Niveau:
    """Class to create a level"""

    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
        self.win = pygame.image.load(WIN).convert_alpha()
        self.lose = pygame.image.load(LOSE).convert_alpha()

    def generer(self):
        """Method for generating the level according to the file.
We create a general list, containing a list by line to display"""
        # Open the file
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            # We go through the lines of the file
            for ligne in fichier:
                ligne_niveau = []
                # We go through the sprites (letters) contained in the file
                for sprite in ligne:
                    # We ignore the end of line "\ n"
                    if sprite != '\n':
                        # We add the sprite to the list of the line
                        ligne_niveau.append(sprite)
                # Add the line to the level list
                structure_niveau.append(ligne_niveau)
            # We safeguard this structure
            self.structure = structure_niveau

    def afficher(self, fenetre):
        """Method for displaying the level according to
         of the structure list returned by generer()"""
        # Loading images (only incoming ones contain transparency)
        mur = pygame.image.load(image_mur).convert()
        depart = pygame.image.load(image_depart).convert()
        arrivee = pygame.image.load(image_arrivee).convert_alpha()

        # We go through the level list
        num_ligne = 0
        for ligne in self.structure:
            # We go through the lists of lines
            num_case = 0
            for sprite in ligne:
                # The actual position in pixels is calculated
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':  # m = Wall
                    fenetre.blit(mur, (x, y))
                elif sprite == 'd':  # d = Departure
                    fenetre.blit(depart, (x, y))
                elif sprite == 'a':  # a = Arrival
                    fenetre.blit(arrivee, (x, y))
                num_case += 1
            num_ligne += 1


class Perso:
    """Class to create a character"""

    def __init__(self, mg_img, niveau):
        # Sprites of the character
        self.mg = pygame.image.load(mg_img).convert_alpha()

        # Character position in boxes and pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Level in which the character is located
        self.niveau = niveau
        # Object counter picked up
        self.compteur = 0

    def deplacer(self, direction):
        """Method for moving the character"""

        if self.niveau.structure[self.case_y][self.case_x] == 'i':
            self.niveau.structure[self.case_y][self.case_x] = '0'
            self.compteur += 1
            print("An object has just been picked up")
            print("he owns : ", self.compteur)
        # Move to the right
        if direction == 'droite':
            # Not to exceed the screen
            if self.case_x < (nombre_sprite_cote - 1):
                # We check that the destination box is not a wall
                if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
                    # Moving a box
                    self.case_x += 1
                    # Calculation of the "real" position in pixel
                    self.x = self.case_x * taille_sprite
            # Image in the right direction


        # Move to the left
        if direction == 'gauche':
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite


        # Move up
        if direction == 'haut':
            if self.case_y > 0:
                if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite


        # Move down
        if direction == 'bas':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite



class Item:
    """Item managment, get random position"""

    def __init__(self, image, niveau):
        # Sprites of the character
        self.image = pygame.image.load(image).convert_alpha()
        # Character position in boxes and pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Level in which the character is located
        self.niveau = niveau

        while (self.niveau.structure[self.case_y][self.case_x] != '0'):
            self.case_x = randint(0, 14)
            self.case_y = randint(0, 14)
            self.x = self.case_x * 30
            self.y = self.case_y * 30
        self.niveau.structure[self.case_y][self.case_x] = 'i'
