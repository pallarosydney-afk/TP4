"""
Objectif du fichier : Faire la classe de l'affichage du TP4
Date : 08/10/2026
Utilisateur :  Sydney Pallaro / Charline Talon 
ToDo : ...
"""
import tkinter as tk 
from tkinter import messagebox
import numpy as np 
import random
import TP4_classe_brique as tp4_brique
import TP4_classe_balle as tp4_balle
import TP4_classe_raquette as tp4_raquette 

import tkinter as tk 
from tkinter import messagebox
import numpy as np 
import random
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
        self.vies = 3
        self.augmentation_vitesse = (self.nb_carreaux_ligne * self.nb_carreaux_colonne) / 1000
        self.en_cours = False
        self.arcade_mode = False
        
        total_briques = self.nb_carreaux_ligne * self.nb_carreaux_colonne # 180 briques
        self.nb_briques_restantes = total_briques
        
        nb_jaunes = total_briques // 4
        toutes_positions = [(i, j) for i in range(self.nb_carreaux_ligne) for j in range(self.nb_carreaux_colonne)]
        speciales = random.sample(toutes_positions, 2 + 3 + nb_jaunes)
        
        self.brique_pour_rqt_grde = speciales[:2]
        self.brique_pour_rqt_petite = speciales[2:5]
        self.brique_changement_color = speciales[5:]

        self.label_vies = tk.Label(self.jeu, text=f"Nombre de vies : {self.vies}")
        self.label_vies.pack()

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
                
                # Attribution des couleurs et des tags selon le type de brique
                if (i, j) in self.brique_pour_rqt_grde:
                    fill_col = "#2ECC71"
                    outline_col = "#27AE60"
                    tag_brique = f'brique_pour_rqt_grde_{i}_{j}'
                elif (i, j) in self.brique_pour_rqt_petite:
                    fill_col = "#8E44AD"
                    outline_col = "#6C3483"
                    tag_brique = f'brique_pour_rqt_petite_{i}_{j}'
                elif (i, j) in self.brique_changement_color:
                    fill_col = "#F1750F"
                    outline_col = "#F39C12"
                    tag_brique = f'brique_jaune_{i}_{j}'
                else:
                    fill_col = "#C51AA0"
                    outline_col = "#9D0183"
                    tag_brique = f'brique_{i}_{j}'

                self.plateforme_jeu.create_rectangle(
                    brique.ecart + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.ecart + j * (brique.largeur_rectangle + brique.ecart), 
                    brique.longueur_rectangle + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.largeur_rectangle + j * (brique.largeur_rectangle + brique.ecart),
                    fill=fill_col, outline=outline_col, width=2, tag=tag_brique)
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
        if self.en_cours: 
            return
            
        self.en_cours = True
        self.boucle_jeu()

    def activer_mode_arcade(self):
        """
        Do : Active le mode arcade 
        """
        self.arcade_mode = True
        self.plateforme_jeu.config(bg="#91C691") # Fond vert
        self.plateforme_jeu.itemconfig('balle', fill="#424F43", outline="#424F43")
        self.plateforme_jeu.itemconfig('raquette', fill="#424F43", outline="#424F43")
        
        for i in range(self.nb_carreaux_ligne):
            for j in range(self.nb_carreaux_colonne):
                for type_brique in ['brique', 'brique_pour_rqt_grde', 'brique_pour_rqt_petite', 'brique_jaune']:
                    tag = f'{type_brique}_{i}_{j}'
                    if self.plateforme_jeu.coords(tag):
                        self.plateforme_jeu.itemconfig(tag, fill="#424F43", outline="#424F43")

    def boucle_jeu(self):
        coords_balle = self.plateforme_jeu.coords('balle')
        if not coords_balle: 
            return
            
        x_balle_1, y_balle_1, x_balle_2, y_balle_2 = coords_balle
            
        if y_balle_2 >= self.dimy:
            self.vies -= 1
            self.label_vies.config(text=f"Nombre de vies : {self.vies}")

            if self.vies <= 0: 
                self.en_cours = False
                reponse = messagebox.askyesno("Fin de partie", "Vous avez perdu. Voulez-vous rejouer ?")
                if reponse == True:
                    self.recommencer_partie() 
                else:
                    self.fermer_fenetre()
                return
            else:
                self.plateforme_jeu.delete('balle')
                self.balle = tp4_balle.balle(self.dimx, self.dimy)
                couleur_balle = "#000000" if self.arcade_mode else "#7414EA"
                self.plateforme_jeu.create_oval(
                    self.balle.x_init_balle - self.balle.taille_balle / 2, 
                    self.balle.y_init_balle - self.balle.taille_balle / 2, 
                    self.balle.x_init_balle + self.balle.taille_balle / 2, 
                    self.balle.y_init_balle + self.balle.taille_balle / 2, 
                    fill=couleur_balle, outline=couleur_balle if self.arcade_mode else "#FEFBFD", width=2, tag='balle')
                coords_balle = self.plateforme_jeu.coords('balle')
                x_balle_1, y_balle_1, x_balle_2, y_balle_2 = coords_balle

        coords_raquette = self.plateforme_jeu.coords('raquette')
        if coords_raquette:
            x_raquette_1, y_raquette_1, x_raquette_2, y_raquette_2 = coords_raquette
            if (x_balle_2 >= x_raquette_1 and x_balle_1 <= x_raquette_2 and y_balle_2 >= y_raquette_1 and y_balle_1 <= y_raquette_2):                    
                self.balle.dy = -self.balle.dy

        toutes_briques_detruites = True
        for i in range(self.nb_carreaux_ligne):
            for j in range(self.nb_carreaux_colonne):
                for type_brique in ['brique', 'brique_pour_rqt_grde', 'brique_pour_rqt_petite', 'brique_jaune']:
                    brique_tag = f'{type_brique}_{i}_{j}'      
                    coords_brique = self.plateforme_jeu.coords(brique_tag) 
                    
                    if coords_brique:   
                        toutes_briques_detruites = False
                        x_brique_1, y_brique_1, x_brique_2, y_brique_2 = coords_brique
                        if (x_balle_2 >= x_brique_1 and x_balle_1 <= x_brique_2 and y_balle_2 >= y_brique_1 and y_balle_1 <= y_brique_2):
                            self.score += 10
                            self.label_score.config(text=f"Score : {self.score}")
                            self.plateforme_jeu.delete(brique_tag)
                            self.nb_briques_restantes -= 1
                            
                            if self.nb_briques_restantes <= 50 and not self.arcade_mode:
                                self.activer_mode_arcade()

                            self.balle.dy = -self.balle.dy 
                            self.balle.vitesse_x += self.augmentation_vitesse
                            self.balle.vitesse_y += self.augmentation_vitesse
                            
                            if type_brique == 'brique_jaune':
                                if not self.arcade_mode:
                                    rand_color = f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"
                                    self.plateforme_jeu.itemconfig('balle', fill=rand_color, outline=rand_color)

                            if coords_raquette:
                                rx1, ry1, rx2, ry2 = coords_raquette
                                largeur = rx2 - rx1
                                centre = (rx1 + rx2) / 2
                                
                                if type_brique == 'brique_pour_rqt_grde':
                                    nouvelle_largeur = min(self.dimx, largeur + 60)
                                    rx1 = centre - nouvelle_largeur / 2
                                    rx2 = centre + nouvelle_largeur / 2
                                    if rx1 < 0: rx1 = 0; rx2 = nouvelle_largeur
                                    if rx2 > self.dimx: rx2 = self.dimx; rx1 = self.dimx - nouvelle_largeur
                                    self.plateforme_jeu.coords('raquette', rx1, ry1, rx2, ry2)
                                    self.raquette.x1 = rx1
                                    self.raquette.x2 = rx2
                                    
                                elif type_brique == 'brique_pour_rqt_petite':
                                    nouvelle_largeur = max(40, largeur - 60)
                                    rx1 = centre - nouvelle_largeur / 2
                                    rx2 = centre + nouvelle_largeur / 2
                                    self.plateforme_jeu.coords('raquette', rx1, ry1, rx2, ry2)
                                    self.raquette.x1 = rx1
                                    self.raquette.x2 = rx2
                            
                            break

        if toutes_briques_detruites:
            self.en_cours = False
            reponse = messagebox.askyesno("Victoire !", "Bravo, vous avez gagné ! Voulez-vous rejouer ?")
            if reponse == True:
                self.recommencer_partie()
            else:
                self.fermer_fenetre()
                return
        
        [dx, dy] = self.balle.deplacement()
        self.plateforme_jeu.move('balle', dx, dy)
        self.jeu.after(30, self.boucle_jeu)

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
                                   bg="#C5D6C4", fg="#06826F")
        bouton_rejouer.pack(pady=5)
        bouton_quitter = tk.Button(fenetre_perdu, text="Quitter", command=self.fermer_fenetre, bg="#C5D6C4", fg="#E30057")
        bouton_quitter.pack(pady=5)

    def recommencer_partie(self):
        self.en_cours = False 
        self.arcade_mode = False
        self.score = 0
        self.vies = 3
        self.balle.vitesse_x=self.balle.vitesse_init_balle
        self.balle.vitesse_y=self.balle.vitesse_init_balle
        total_briques = self.nb_carreaux_ligne * self.nb_carreaux_colonne
        self.nb_briques_restantes = total_briques
        
        self.label_score.config(text=f"Score : {self.score}")
        self.label_vies.config(text=f"Nombre de vies : {self.vies}")
        
        nb_jaunes = total_briques // 4
        toutes_positions = [(i, j) for i in range(self.nb_carreaux_ligne) for j in range(self.nb_carreaux_colonne)]
        speciales = random.sample(toutes_positions, 2 + 3 + nb_jaunes)
        self.brique_pour_rqt_grde = speciales[:2]
        self.brique_pour_rqt_petite = speciales[2:5]
        self.brique_changement_color = speciales[5:]
        
        self.plateforme_jeu.config(bg="#9AC387")
        
        self.plateforme_jeu.delete('balle')
        self.balle = tp4_balle.balle(self.dimx, self.dimy)
        self.plateforme_jeu.create_oval(
            self.balle.x_init_balle - self.balle.taille_balle / 2, 
            self.balle.y_init_balle - self.balle.taille_balle / 2, 
            self.balle.x_init_balle + self.balle.taille_balle / 2, 
            self.balle.y_init_balle + self.balle.taille_balle / 2, 
            fill="#7414EA", outline="#FEFBFD", width=2, tag='balle')
        
        self.plateforme_jeu.delete('raquette')
        self.raquette = tp4_raquette.raquette(self.dimx, self.dimy)
        self.plateforme_jeu.create_rectangle(self.raquette.x1, self.raquette.y1, self.raquette.x2, self.raquette.y2, fill="#FD7EDB", outline="white", width=2, tag='raquette')

        for i in range(self.nb_carreaux_ligne):
            for j in range(self.nb_carreaux_colonne):
                for type_brique in ['brique', 'brique_pour_rqt_grde', 'brique_pour_rqt_petite', 'brique_jaune']:
                    self.plateforme_jeu.delete(f'{type_brique}_{i}_{j}')
                
                brique = tp4_brique.brique(self.dimx, self.dimy, self.nb_carreaux_ligne, self.nb_carreaux_colonne)
                
                if (i, j) in self.brique_pour_rqt_grde:
                    fill_col = "#2ECC71"
                    outline_col = "#27AE60"
                    tag_brique = f'brique_pour_rqt_grde_{i}_{j}'
                elif (i, j) in self.brique_pour_rqt_petite:
                    fill_col = "#8E44AD"
                    outline_col = "#6C3483"
                    tag_brique = f'brique_pour_rqt_petite_{i}_{j}'
                elif (i, j) in self.brique_changement_color:
                    fill_col = "#F1750F"
                    outline_col = "#F39C12"
                    tag_brique = f'brique_jaune_{i}_{j}'
                else:
                    fill_col = "#C51AA0"
                    outline_col = "#9D0183"
                    tag_brique = f'brique_{i}_{j}'

                self.plateforme_jeu.create_rectangle(
                    brique.ecart + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.ecart + j * (brique.largeur_rectangle + brique.ecart), 
                    brique.longueur_rectangle + i * (brique.longueur_rectangle + brique.ecart), 
                    brique.largeur_rectangle + j * (brique.largeur_rectangle + brique.ecart),
                    fill=fill_col, outline=outline_col, width=2, tag=tag_brique)
                    
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
        for type_brique in ['brique', 'brique_pour_rqt_grde', 'brique_pour_rqt_petite', 'brique_jaune']:
            self.plateforme_jeu.delete(f'{type_brique}_{i}_{j}')

jeu = fenetre_jeu()
