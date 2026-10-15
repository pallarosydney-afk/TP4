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