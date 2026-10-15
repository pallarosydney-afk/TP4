"""
Objectif du fichier : Faire les fonctions du TP4
Date : 08/10/2026
Utilisateur :  Sydney Pallaro / Charline Talon 
ToDo : ...
"""

import tkinter as tk 

class fenetre_jeu:
    def __init__(self):
        self.jeu = tk.Tk()
        self.jeu.title("Casse brique")
        self.dimx = 900
        self.dimy = 900
        self.jeu.geometry(f"{self.dimx}x{self.dimy}")
        self.jeu.config(cursor="circle")

        self.taille_balle = 30
        self.nb_carreaux_ligne = 8
        self.nb_carreaux_colonne = 6
        
        self.longueur_rectangle = self.dimx / self.nb_carreaux_ligne
        self.largeur_rectangle = (self.dimy / 2) / self.nb_carreaux_colonne
        self.ecart = self.longueur_rectangle / 8

        self.x_init_balle = self.dimx/2
        self.y_init_balle = self.dimy - self.dimy/6

        self.plateforme_jeu = tk.Canvas(self.jeu, bg='black', width=self.dimx, height=self.dimy)
        self.plateforme_jeu.create_oval(self.x_init_balle - self.taille_balle / 2, self.y_init_balle - self.taille_balle / 2, 
                                        self.x_init_balle + self.taille_balle / 2, self.y_init_balle + self.taille_balle / 2, 
                                        fill="#EFA2D6", outline="#E7219C", width=2, tag='balle')
        
        for i in range(self.nb_carreaux_ligne-1):
            for j in range(self.nb_carreaux_colonne):
                self.plateforme_jeu.create_rectangle(
                    self.ecart + i * (self.longueur_rectangle + self.ecart), 
                    self.ecart + j * (self.largeur_rectangle + self.ecart), 
                    self.longueur_rectangle + i * (self.longueur_rectangle + self.ecart), 
                    self.largeur_rectangle + j * (self.largeur_rectangle + self.ecart),
                    fill="#C97EFD", outline="white", width=2, tag=f'brique{i}{j}')
        self.plateforme_jeu.pack()  

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

print(jeu.dimx)
