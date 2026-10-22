"""
Objectif du fichier : Faire les fonctions du TP4
Date : 15/10/2026
Utilisateur :  Sydney Pallaro / Charline Talon 
ToDo : ...
"""

import tkinter as tk 

class brique:
    def __init__(self, dimx, dimy, nb_carreaux_ligne, nb_carreaux_colonne):
        self.ecart = dimx/500 
        self.longueur_rectangle = (dimx - nb_carreaux_ligne*self.ecart)/ nb_carreaux_ligne 
        self.largeur_rectangle = (dimy / 2) / nb_carreaux_colonne
