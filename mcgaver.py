#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images

MCGAVER Labyrinth Game
Game in which we have to move MCGAVER through a labyrinth.

Python script
Files: MCGAVER.py, classes.py, constants.py, n1
"""

import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

# Opening the Pygame window (square: width = height)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
# Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
# title
pygame.display.set_caption(titre_fenetre)


# MAIN LOOP
continuer = 1
while continuer:
    # Loading and viewing the home screen
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0, 0))

    # refreshment
    pygame.display.flip()

    # These variables are reset to 1 at each loop turn
    continuer_jeu = 1
    continuer_accueil = 1

    # HOST LOOP
    while continuer_accueil:

        # Speed limitation of the loop
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # If the user leaves, we put the variables
            # loop to 0 to browse none and close
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                # Variable of choice of the level
                choix = 0

            elif event.type == KEYDOWN:
                # Launch of level 1
                if event.key == K_F1:
                    continuer_accueil = 0  # We leave home
                    choix = 'n1'  # We define the level to load
                # Launch of level 2
                elif event.key == K_F2:
                    continuer_accueil = 0
                    choix = 'n2'

    # we check that the player has made a choice of level
    # to not load when it leaves
    if choix != 0:
        # Loading the bottom
        fond = pygame.image.load(image_fond).convert()

        # Generating a level from a file
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(fenetre)

        # Mac Gyver creation
        mg = Perso(MG_IMG, niveau)

        # creating objects
        item1 = Item(image_item1, niveau)
        item2 = Item(image_item2, niveau)
        item3 = Item(image_item3, niveau)
    # GAME LOOP
    while continuer_jeu:

        # Speed limitation of the loop
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # If the user leaves, we put the variable that continues the game
            # AND the general variable to 0 to close the window
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0

            elif event.type == KEYDOWN:
                # If the user press Esc here, we just go back to the menu
                if event.key == K_ESCAPE:
                    continuer_jeu = 0

                # Keys of movement of MCGAVER
                elif event.key == K_RIGHT:
                    mg.deplacer('droite')
                elif event.key == K_LEFT:
                    mg.deplacer('gauche')
                elif event.key == K_UP:
                    mg.deplacer('haut')
                elif event.key == K_DOWN:
                    mg.deplacer('bas')

        # Displays at new positions
        fenetre.blit(fond, (0, 0))
        niveau.afficher(fenetre)
        # MC.direction = the image in the right direction
        fenetre.blit(mg.mg, (mg.x, mg.y))
        # Condition of image display
        if niveau.structure[item1.case_y][item1.case_x] == 'i':
            fenetre.blit(item1.image, (item1.x, item1.y))

        niveau.afficher(fenetre)
        # MC.direction = the image in the right direction
        fenetre.blit(mg.mg, (mg.x, mg.y))
        # Condition of image display
        if niveau.structure[item2.case_y][item2.case_x] == 'i':
            fenetre.blit(item2.image, (item2.x, item2.y))

        # MC.direction = the image in the right direction
        fenetre.blit(mg.mg, (mg.x, mg.y))
        # Condition of image display
        if niveau.structure[item3.case_y][item3.case_x] == 'i':
            fenetre.blit(item3.image, (item3.x, item3.y))

        pygame.display.flip()

        # Victory -> Back to home
        if niveau.structure[mg.case_y][mg.case_x] == 'a' and mg.compteur == 3:
            fenetre.blit(niveau.win, (0, 0))
            pygame.display.flip()
            # Put game in pause for two seconds
            pygame.time.delay(2000)
            continuer_jeu = 0
        # Defeat
        elif niveau.structure[mg.case_y][mg.case_x] == 'a' and mg.compteur != 3:
            fenetre.blit(niveau.lose, (0, 0))
            pygame.display.flip()
            # Put game in pause for two seconds
            pygame.time.delay(2000)
            continuer_jeu = 0
