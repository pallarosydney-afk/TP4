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
        self.vitesse_init_balle=8

        self.dimx = dimx
        self.dimy = dimy

        self.taille_balle = 30
        self.rayon = self.taille_balle/2

        self.x=self.x_init_balle #coordonnée horizontale de la balle à chaque instant
        self.y=self.y_init_balle #coordonnée verticale de la balle à chaque instant
        
        self.vitesse_x=np.random.choice([-1, 1])*self.vitesse_init_balle
        self.vitesse_y=np.random.choice([-1, 1])*self.vitesse_init_balle
        self.angle=np.pi/4 

        self.dx = np.cos(self.angle)*self.vitesse_x
        self.dy = np.sin(self.angle)*self.vitesse_y

    def deplacement(self):
        """
        Input : - 
        Output : Les coordonées de la balle déplacée
        Do : Fait bouger les coordonnées de la balle
        """
        #rebond à droite ou à gauche 
        if self.x + self.rayon + self.dx > self.dimx or self.x - self.rayon + self.dx < 0: 
            self.vitesse_x = -self.vitesse_x
            self.dx = np.sin(self.angle)*self.vitesse_x

        #rebond en haut 
        if self.y - self.rayon + self.dy < 0 : 
            self.vitesse_y = -self.vitesse_y
            self.dy = np.sin(self.angle)*self.vitesse_y

        self.x+=self.dx
        self.y+=self.dy
        return [self.dx,self.dy]