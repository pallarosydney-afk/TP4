"""
Objectif du fichier : Faire la classe de l'affichage du TP4
Date : 08/10/2026
Utilisateur :  Sydney Pallaro / Charline Talon 
ToDo : ...
"""
import tkinter as tk 
from tkinter import messagebox
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
        self.jeu.config(cursor="heart")
        self.nb_carreaux_ligne = 15
        self.nb_carreaux_colonne = 12
        self.score = 0
        self.augmentation_vitesse=(self.nb_carreaux_ligne*self.nb_carreaux_colonne)/1000

        self.label_score = tk.Label(self.jeu, text=f"Score : {self.score}")
        self.label_score.pack()

        self.plateforme_jeu = tk.Canvas(self.jeu, bg="#9AC387", width=self.dimx, height=self.dimy)

        self.balle = tp4_balle.balle(self.dimx, self.dimy)
        self.plateforme_jeu.create_oval(self.balle.x_init_balle - self.balle.taille_balle / 2, self.balle.y_init_balle - self.balle.taille_balle / 2, 
                                        self.balle.x_init_balle + self.balle.taille_balle / 2, self.balle.y_init_balle + self.balle.taille_balle / 2, 
                                        fill="#7414EA", outline="#FEFBFD", width=2, tag='balle')

        for i in range(self.nb_carreaux_ligne):
            for j in range(self.nb_carreaux_colonne):
                brique = tp4_brique.brique(self.dimx, self.dimy, self.nb_carreaux_ligne, self.nb_carreaux_colonne)
                self.plateforme_jeu.create_rectangle(
                    brique.ecart + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.ecart + j * (brique.largeur_rectangle + brique.ecart), 
                    brique.longueur_rectangle + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.largeur_rectangle + j * (brique.largeur_rectangle + brique.ecart),
                    fill="#C51AA0", outline="#9D0183", width=2, tag=f'brique{i}{j}')
        self.plateforme_jeu.pack()  

        self.raquette = tp4_raquette.raquette(self.dimx, self.dimy)
        self.plateforme_jeu.create_rectangle(self.raquette.x1, self.raquette.y1, self.raquette.x2, self.raquette.y2, fill="#FD7EDB", outline="white", width=2, tag='raquette')
        
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
        Do : Met la balle en mouvement et gère les collisions. 
        """
        coords_balle = self.plateforme_jeu.coords('balle')
        
        if coords_balle:
            x_balle_1, y_balle_1, x_balle_2, y_balle_2 = coords_balle
            
            if y_balle_2 >= self.dimy:
                reponse = messagebox.askyesno("Fin de partie", "Vous avez perdu. Voulez-vous rejouer ?")
                if reponse == True:
                    self.recommencer_partie() 
                else:
                    self.fermer_fenetre()
                return

            coords_raquette = self.plateforme_jeu.coords('raquette')
            if coords_raquette:
                x_raquette_1, y_raquette_1, x_raquette_2, y_raquette_2 = coords_raquette
                if (x_balle_2 >= x_raquette_1 and x_balle_1 <= x_raquette_2 and y_balle_2 >= y_raquette_1 and y_balle_1 <= y_raquette_2):                    
                    self.balle.dy = -self.balle.dy

            toutes_briques_detruites = True
            for i in range(self.nb_carreaux_ligne):
                for j in range(self.nb_carreaux_colonne):
                    brique = f'brique{i}{j}'      
                    coords_brique = self.plateforme_jeu.coords(brique) 
                    
                    if coords_brique:   
                        toutes_briques_detruites = False
                        x_brique_1, y_brique_1, x_brique_2, y_brique_2 = coords_brique
                        if (x_balle_2 >= x_brique_1 and x_balle_1 <= x_brique_2 and y_balle_2 >= y_brique_1 and y_balle_1 <= y_brique_2):
                            self.score += 10
                            self.label_score.config(text=f"Score : {self.score}")
                            self.plateforme_jeu.delete(brique)
                            self.balle.dy = -self.balle.dy 
                            self.balle.vitesse_x+=self.augmentation_vitesse
                            self.balle.vitesse_y+=self.augmentation_vitesse
                            break

        if toutes_briques_detruites:
                reponse = messagebox.askyesno("Victoire !", "Bravo, vous avez gagné ! Voulez-vous rejouer ?")
                if reponse == True:
                    self.recommencer_partie()
                else:
                    self.fermer_fenetre()
                return
        
        [dx, dy] = self.balle.deplacement()
        self.plateforme_jeu.move('balle', dx, dy)
        self.jeu.after(30, self.lancer_jeu)

    def afficher_fenetre_defaite(self):
        """
        Input : -
        Output : -
        Do :  Ouvre une fenetre avec les options quitter et rejouer.
        """
        fenetre_perdu = tk.Toplevel(self.jeu)
        fenetre_perdu.title("Fin de partie")
        fenetre_perdu.geometry("300x200")
        fenetre_perdu.config(bg="#9AC387")
        label_perdu = tk.Label(fenetre_perdu, text="Vous avez perdu. Dommage, revenez jouer quand vous serez moins nul !", font=("Arial", 20, "bold"), bg="#9AC387", fg="#D508A9")
        label_perdu.pack(pady=20)
        bouton_rejouer = tk.Button(fenetre_perdu, text="Rejouer", 
                                   command=lambda: [fenetre_perdu.destroy(), self.recommencer_partie()],
                                   bg="#C5D6C4", fg="#207B6E")
        bouton_rejouer.pack(pady=5)
        bouton_quitter = tk.Button(fenetre_perdu, text="Quitter", command=self.fermer_fenetre, bg="#C5D6C4", fg="#207B6E")
        bouton_quitter.pack(pady=5)

    def recommencer_partie(self):
        """
        Input : -
        Output : -
        Do :  Relance une partie (Sert pour le bouton rejouer)
        """
        self.score = 0
        self.label_score.config(text=f"Score : {self.score}")
        
        self.plateforme_jeu.delete('balle')
        self.balle = tp4_balle.balle(self.dimx, self.dimy)
        self.plateforme_jeu.create_oval(
            self.balle.x_init_balle - self.balle.taille_balle / 2, 
            self.balle.y_init_balle - self.balle.taille_balle / 2, 
            self.balle.x_init_balle + self.balle.taille_balle / 2, 
            self.balle.y_init_balle + self.balle.taille_balle / 2, 
            fill="#7414EA", outline="#FEFBFD", width=2, tag='balle')
        
        for i in range(self.nb_carreaux_ligne):
            for j in range(self.nb_carreaux_colonne):
                tag_brique = f'brique{i}{j}'
                self.plateforme_jeu.delete(tag_brique) 
                
                brique = tp4_brique.brique(self.dimx, self.dimy, self.nb_carreaux_ligne, self.nb_carreaux_colonne)
                self.plateforme_jeu.create_rectangle(
                    brique.ecart + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.ecart + j * (brique.largeur_rectangle + brique.ecart), 
                    brique.longueur_rectangle + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.largeur_rectangle + j * (brique.largeur_rectangle + brique.ecart),
                    fill="#C51AA0", outline="#9D0183", width=2, tag=f'brique{i}{j}')
        self.lancer_jeu()

    def mouv_raquette(self, event):
        """
        Input : - 
        Output : Fait bouger la raquette avec le clavier 
        Do : Fait bouger la raquette avec le clavier
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

    def supprimer_brique(self, i, j):
        """
        Input : Les numéros d'une brique 
        Output : Suppression de la brique 
        Do : Supprime la brique numéro i,j
        """
        tag_brique = f'brique{i}{j}'
        self.plateforme_jeu.delete(tag_brique)

jeu = fenetre_jeu()