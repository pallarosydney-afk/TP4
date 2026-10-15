"""
Objectif du fichier : Faire la classe de l'affichage du TP4
Date : 08/10/2026
Utilisateur :  Sydney Pallaro / Charline Talon 
ToDo : ...
"""

import tkinter as tk 
import numpy as np 
import TP4_classe_brique as tp4_brique
import TP4_classe_balle as tp4_balle
import TP4_classe_raquette as tp4_raquette 

class fenetre_jeu:
    def __init__(self):
        self.jeu = tk.Tk()
        self.jeu.title("Casse brique")
        self.dimx = 700
        self.dimy = 700
        self.jeu.geometry(f"{self.dimx}x{self.dimy}")
        self.jeu.config(cursor="circle")
        self.nb_carreaux_ligne = 8
        self.nb_carreaux_colonne = 6
        self.nb_vie_restantes = 3 
        self.score = 0

        self.points = tk.Label(self.jeu, text=f" Vies : {self.nb_vie_restantes}")
        self.points.pack()

        self.points = tk.Label(self.jeu, text=f"Score : {self.score}")
        self.points.pack()

        self.plateforme_jeu = tk.Canvas(self.jeu, bg='black', width=self.dimx, height=self.dimy)

        self.balle=tp4_balle.balle(self.dimx,self.dimy)
        self.plateforme_jeu.create_oval(self.balle.x_init_balle - self.balle.taille_balle / 2, self.balle.y_init_balle - self.balle.taille_balle / 2, 
                                        self.balle.x_init_balle + self.balle.taille_balle / 2, self.balle.y_init_balle + self.balle.taille_balle / 2, 
                                        fill="#EFA2D6", outline="#E7219C", width=2, tag='balle')
        
        for i in range(self.nb_carreaux_ligne-1):
            for j in range(self.nb_carreaux_colonne):
                brique=tp4_brique.brique(self.dimx, self.dimy, self.nb_carreaux_ligne, self.nb_carreaux_colonne)
                self.plateforme_jeu.create_rectangle(
                    brique.ecart + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.ecart + j * (brique.largeur_rectangle + brique.ecart), 
                    brique.longueur_rectangle + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.largeur_rectangle + j * (brique.largeur_rectangle + brique.ecart),
                    fill="#C97EFD", outline="white", width=2, tag=f'brique{i}{j}')
        self.plateforme_jeu.pack()  

        self.raquette=tp4_raquette.raquette(self.dimx, self.dimy)
        self.plateforme_jeu.create_rectangle(
            self.raquette.x_init_raquette-self.raquette.longueur_raquette, 
            self.raquette.y_init_raquette-self.raquette.largeur_raquette,                 
            self.raquette.x_init_raquette+self.raquette.longueur_raquette, 
            self.raquette.y_init_raquette+self.raquette.largeur_raquette,
            fill="#A47EFD", outline="black", width=2, tag=self.raquette)

        def fermer_fenetre():
            print("La fenêtre du jeu se ferme.")
            self.jeu.destroy()

        self.bouton_jouer = tk.Button(self.jeu, text="Jouer", command=fermer_fenetre, bg="#C5D6C4", fg="#207B6E",
                                      activebackground="#25BDB8", activeforeground="white")  
        self.bouton_jouer.pack(side=tk.LEFT, padx=10)
        self.bouton_quitter = tk.Button(self.jeu, text='🚫', command=fermer_fenetre, bg="#C5D6C4", fg="#207B6E",
                                        activebackground="#437541", activeforeground="white")  
        self.bouton_quitter.pack(side=tk.RIGHT, padx=10)
        self.jeu.mainloop()

jeu=fenetre_jeu()


