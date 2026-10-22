"""
Objectif du fichier : Faire la classe de la raquette du TP4
Date : 15/10/2026
Utilisateur :  Sydney Pallaro / Charline Talon 
ToDo : ...
"""

import tkinter as tk 

class raquette:
    def __init__(self, dimx, dimy):
        self.longueur_raquette = dimx/15
        self.largeur_raquette = dimy/110
        self.x_init_raquette = dimx/2
        self.y_init_raquette = dimy - dimy/8
        self.coord_x=self.x_init_raquette #coordonnée horizontale de la raquette à chaque instant
        self.coord_y=self.y_init_raquette #coordonnée verticale de la raquette à chaque instant
        self.vitesse_raquette = dimx/30 #nb de pixels par clics

        [self.x1,self.y1,self.x2,self.y2]= [self.x_init_raquette - self.longueur_raquette, 
        self.y_init_raquette - self.largeur_raquette,
        self.x_init_raquette + self.longueur_raquette, 
        self.y_init_raquette + self.largeur_raquette]

    def deplacer(self, dx, dimx):
        """
        Déplace la raquette horizontalement de dx pixels,
        tout en restant dans les limites de la fenêtre (dimx).
        """
        # Empêcher de sortir à gauche
        if self.x1 + dx >= 0 and self.x2 + dx <= dimx:
            self.x1 += dx
            self.x2 += dx