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
        self.detection_clic_sur_raquette = False 
        [self.xmin,self.xmax,self.ymin,self.ymax] = [0,0,0,0]

    def Clic(self,event):
        X = event.self.coord_x
        Y = event.self.coord_y
        if self.xmin < X < self.xmax and self.ymin < Y < self.ymax: 
            self.detection_clic_sur_raquette = True 

