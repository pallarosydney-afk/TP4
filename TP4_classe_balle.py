"""
Objectif du fichier : Faire la classe de la balle du TP4
Date : 05/10/2026
Utilisateur :  Sydney Pallaro / Charline Talon 
ToDo : ...
"""

import tkinter as tk 
import numpy as np


class balle:
    def __init__(self, dimx, dimy):
        self.x_init_balle = dimx/2
        self.y_init_balle = dimy - dimy/6
        self.vitesse_init_balle=2

        self.taille_balle = 30
        
        self.x=self.x_init_balle #coordonnée horizontale de la balle à chaque instant
        self.y=self.y_init_balle #coordonnée verticale de la balle à chaque instant
        
        self.vitesse=self.vitesse_init_balle
        self.angle=3*np.pi/4 

        self.dx = np.cos(self.angle)
        self.dy = np.sin(self.angle)

        def deplacement(self):
            """
            Input : Les variables balle, raquette, brique sont globales
            Output : Renvoie les positions de la balles après un déplacement de celle-ci
            Do : Regarde si la balle touche un bord, la raquette ou une brique et fait le reond si c'est 
            le cas. Ne fait que avancer en diagonale sinon.
            """
            #global balle, raquette, brique
            #rebond bords :
            if balle.taille + balle.dx + balle.x > dimx or balle.x - balle.taille + balle.dx < 0 :
                balle.angle=balle.angle + np.pi/2
            if balle.taille + balle.dy + balle.y > dimy or balle.y - balle.taille + balle.dy < 0 :
                balle.angle=-balle.angle + np.pi/2
            #rebond raquette : 
            if balle.x-raquette.x < raquette.largeur_raquette/2 + balle.taille/2 : 
                balle.angle=-balle.angle + np.pi/2
            balle.dx = balle.x + balle.dx
            balle.dy = balle.y + balle.dy
            plateforme_jeu.coords(balle, balle.x - balle.taille/2,  balle.y - balle.taille/2,
                                        balle.x + balle.taille/2, balle.y + balle.taille/2)
            jeu.after(20,deplacement)