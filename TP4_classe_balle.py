"""
Objectif du fichier : Faire la classe de la balle du TP4
Date : 05/10/2026
Utilisateur :  Sydney Pallaro / Charline Talon 
ToDo : ...
"""

import tkinter as tk 


class balle:
    def __init__(self, dimx, dimy):
        self.x_init_balle = dimx/2
        self.y_init_balle = dimy - dimy/6
        self.taille_balle = 30