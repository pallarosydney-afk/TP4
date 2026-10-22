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
        self.dimx = 900
        self.dimy = 900
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

        self.plateforme_jeu = tk.Canvas(self.jeu, bg="#9AC387", width=self.dimx, height=self.dimy)

        self.balle=tp4_balle.balle(self.dimx,self.dimy)
        self.plateforme_jeu.create_oval(self.balle.x_init_balle - self.balle.taille_balle / 2, self.balle.y_init_balle - self.balle.taille_balle / 2, 
                                        self.balle.x_init_balle + self.balle.taille_balle / 2, self.balle.y_init_balle + self.balle.taille_balle / 2, 
                                        fill="#7414EA", outline="#FEFBFD", width=2, tag='balle')

        position_brique_restante={}
        for i in range(self.nb_carreaux_ligne-1):
            for j in range(self.nb_carreaux_colonne):
                brique=tp4_brique.brique(self.dimx, self.dimy, self.nb_carreaux_ligne, self.nb_carreaux_colonne)
                self.briques_restantes[(i,j)]=1
                self.plateforme_jeu.create_rectangle(
                    brique.ecart + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.ecart + j * (brique.largeur_rectangle + brique.ecart), 
                    brique.longueur_rectangle + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.largeur_rectangle + j * (brique.largeur_rectangle + brique.ecart),
                    fill="#D508A9", outline="white", width=2, tag=f'brique{i}{j}')
        self.plateforme_jeu.pack()  

        self.raquette = tp4_raquette.raquette(self.dimx, self.dimy)
        self.plateforme_jeu.create_rectangle(self.raquette.x1,self.raquette.y1,self.raquette.x2,self.raquette.y2,fill="#FD7EDB", outline="white", width=2, tag='raquette')
        self.jeu.bind("<Left>", self.mouv_raquette)
        self.jeu.bind("<Right>", self.mouv_raquette)
        self.jeu.focus_set()

        self.bouton_jouer = tk.Button(self.jeu, text="Jouer", command=self.lancer_jeu, bg="#C5D6C4", fg="#207B6E",
                                      activebackground="#25BDB8", activeforeground="white")  
        self.bouton_jouer.pack(side=tk.LEFT, padx=10)

        self.bouton_quitter = tk.Button(self.jeu, text='🚫', command=self.fermer_fenetre, bg="#C5D6C4", fg="#207B6E",
                                                activebackground="#437541", activeforeground="white")  
        self.bouton_quitter.pack(side=tk.RIGHT, padx=10)
        self.jeu.mainloop()

    def fermer_fenetre(self):
        """
        Input : - 
        Output : Ferme la fenêtre du jeu.
        Do : Ferme la fenêtre du jeu. 
        """
        print("La fenêtre du jeu se ferme.")
        self.jeu.destroy()

    def lancer_jeu(self):
        """
        Input : - 
        Output : Lance le jeu.
        Do : Met la balle en mouvement. 
        """
        [dx, dy] = self.balle.deplacement()
        self.plateforme_jeu.move('balle', dx, dy)
        self.jeu.after(30, self.lancer_jeu) 

    def mouv_raquette(self, event):
        """
        Input : - 
        Output : Fait bouger la raquette avec le clavier
        Do : 
        """
        vitesse_raquette = self.raquette.vitesse_raquette  
        
        if event.keysym == 'Left':
            if self.raquette.x1 - vitesse_raquette >= 0:
                self.raquette.deplacer(-vitesse_raquette, self.dimx)
                self.plateforme_jeu.move('raquette', -vitesse_raquette, 0)
        elif event.keysym == 'Right':
            if self.raquette.x2 + vitesse_raquette <= self.dimx:
                self.raquette.deplacer(vitesse_raquette, self.dimx)
                self.plateforme_jeu.move('raquette', vitesse_raquette, 0)
        
jeu=fenetre_jeu()


