from tkinter import Tk,Label,Button,Checkbutton,Entry,messagebox,Toplevel
from joueur import Joueur
from partie import Partie
from combinaison import Combinaison

nom1 =''
nom2 =''
nom3 =''
def __init__(self):
    self.fenetre = Tk()
    self.root = Tk()

def nouvelle_partie(self):
    pass
    #fenetre.destroy()
def partie_graphique(self):
    pass
    #Partie.joueurs.append(nom_joueur1.get(),nom_joueur2.get(),nom_joueur3.get())
    #Partie.jouer_partie(Partie)
    joueur=Label(self.fenetre,text="Test").grid(row=1,column=1)
    nb_tours_restant = Label(self.fenetre,text="2 tours restants").grid(row=1,column=8)
    relancer_des = Button(self.fenetre,text="Lancer dés",command=Combinaison.relancer_des(Combinaison,Combinaison.index_a_relancer)).grid(row=4,column=6)
    terminer_tour = Button(self.fenetre,text="Terminer").grid(row=4,column=7)
    sauvegarde = Button(self.fenetre,text="Sauvegarde",command=Partie.sauvegarde).grid(row=9,column=3)
    #textvariable=Combinaison.des[0]
    de_1= Button(self.fenetre,text="0",command=Combinaison.ajouter_des_a_index(Combinaison,1,Combinaison.index_a_relancer)).grid(row=2,column=1)
    de_2 = Button(self.fenetre,text="1",command=Combinaison.ajouter_des_a_index(Combinaison,2,Combinaison.index_a_relancer)).grid(row=2,column=2)
    de_3 = Button(self.fenetre,text="2",command=Combinaison.ajouter_des_a_index(Combinaison,3,Combinaison.index_a_relancer)).grid(row=2, column=3)
    de_4 = Button(self.fenetre, text="3",command=Combinaison.ajouter_des_a_index(Combinaison,4,Combinaison.index_a_relancer)).grid(row=2, column=4)
    de_5 = Button(self.fenetre, text="4",command=Combinaison.ajouter_des_a_index(Combinaison,5,Combinaison.index_a_relancer)).grid(row=2, column=5)
    reset = Button(self.fenetre,text="Nouvelle Partie").grid(row=4,column=8)
    self.root.destroy()
def charger_partie(self):
        try:
            Partie.restaure(Partie)
        except:
            messagebox.showerror("Erreur chargement","Le fichier de sauvegarde n'est pas disponible")
def lire_regles(self):
    messagebox.showinfo("Règles du jeu","Le but du jeu est d'obtenir la combinaison ayant la plus grande valeur."
    "La combinaison valant le plus est le Quinton, soit lui avec 5 figures similaires, le carré avec 4 figures similaires."
    "Le full avec 3 figures similaires et suivis de 2 autre figures similaire,le brelan avec 3 figures similaires."
    "La séquence avec toutes les figures suivis l'une de l'autre, le double carré avec deux paires de figures "
    "et le carré avec une paire de figures. Chacun des joueurs à le droit 3 lancers sauf si le joueur précédent a"
    "a réussi en moins de coups, donc le nombre de coups réussis est le nouveau total")
def main(self):
    nom_joueur1 = Entry(self.root,textvariable=nom1).grid(row=2,column=3)
    joueur1= Label(self.root,text="Joueur 1").grid(row=1,column=3)
    nom_joueur2 = Entry(self.root,textvariable=nom2).grid(row=2,column=4)
    joueur2= Label(self.root,text="Joueur 2").grid(row=1,column=4)
    nom_joueur3 = Entry(self.root,textvariable=nom3).grid(row=2,column=5)
    joueur3= Label(self.root,text="Joueur 3").grid(row=1,column=5)
    joker_d_as = False
    Checkbutton(self.root,text="As en tant que joker",variable = joker_d_as).grid(row=4,column=5)
    commencer_partie = Button(self.root,text="Commencer",command = partie_graphique).grid(row=4,column=2)
    regles = Button(self.root,text="Lire règles",command=lire_regles).grid(row=4,column=3)
    quitter = Button(self.root,text="Quitter",command=self.root.quit).grid(row=5,column=3)
    restaurer = Button(self.root,text="Restaurer",command=charger_partie).grid(row=5,column=2)
    self.root.mainloop()

