from tkinter import Tk,Label,Button,Checkbutton,Entry,messagebox,Toplevel
from joueur import Joueur
from partie import Partie
from combinaison import Combinaison

nom1 =''
nom2 =''
nom3 =''

class mon_interface(Tk):

    def __init__(self):
        super().__init__()

        Label(self, text="Test").grid(row=1, column=1)
        nb_tours_restant = Label(self, text="2 tours restants").grid(row=1, column=8)
        relancer_des = Button(self, text="Lancer dés",
                              command=Combinaison.relancer_des(Combinaison, Combinaison.index_a_relancer)).grid(row=4,
                                                                                                                column=6)
        terminer_tour = Button(self, text="Terminer").grid(row=4, column=7)
        sauvegarde = Button(self, text="Sauvegarde", command=Partie.sauvegarde).grid(row=9, column=3)
        # textvariable=Combinaison.des[0]
        de_1 = Button(self, text="0",
                      command=Combinaison.ajouter_des_a_index(Combinaison, 1, Combinaison.index_a_relancer)).grid(row=2,
                                                                                                                  column=1)
        de_2 = Button(self, text="1",
                      command=Combinaison.ajouter_des_a_index(Combinaison, 2, Combinaison.index_a_relancer)).grid(row=2,
                                                                                                                  column=2)
        de_3 = Button(self, text="2",
                      command=Combinaison.ajouter_des_a_index(Combinaison, 3, Combinaison.index_a_relancer)).grid(row=2,
                                                                                                                  column=3)
        de_4 = Button(self, text="3",
                      command=Combinaison.ajouter_des_a_index(Combinaison, 4, Combinaison.index_a_relancer)).grid(row=2,
                                                                                                                  column=4)
        de_5 = Button(self, text="4",
                      command=Combinaison.ajouter_des_a_index(Combinaison, 5, Combinaison.index_a_relancer)).grid(row=2,
                                                                                                                  column=5)
        reset = Button(self, text="Nouvelle Partie").grid(row=4, column=8)
        self.menu = menu(self)

    def nouvelle_partie(self):
        pass
    #fenetre.destroy()








class menu(Toplevel):


    def __init__(self,master):

        super().__init__(master)

        self.master = master
        self.transient(master)
        self.grab_set()

        nom_joueur1 = Entry(self,textvariable=nom1).grid(row=2,column=3)
        joueur1= Label(self,text="Joueur 1").grid(row=1,column=3)
        nom_joueur2 = Entry(self,textvariable=nom2).grid(row=2,column=4)
        joueur2= Label(self,text="Joueur 2").grid(row=1,column=4)
        nom_joueur3 = Entry(self,textvariable=nom3).grid(row=2,column=5)
        joueur3= Label(self,text="Joueur 3").grid(row=1,column=5)
        joker_d_as = False
        Checkbutton(self,text="As en tant que joker",variable = joker_d_as).grid(row=4,column=5)
        commencer_partie = Button(self,text="Commencer",command = self.nouvelle_parti).grid(row=4,column=2)
        regles = Button(self,text="Lire règles",command=self.lire_regles).grid(row=4,column=3)
        quitter = Button(self,text="Quitter",command=self.quit).grid(row=5,column=3)
        restaurer = Button(self,text="Restaurer",command=self.charger_partie).grid(row=5,column=2)

    def nouvelle_parti(self):
        """Affecte l'attribut "valeur" à la valeur choisie, et fermer la fenêtre.

        """
        # TODO: Lorsque nous connaîtrons la gestion des erreurs,
        # TODO: nous pourrions valider le contenu de l'entrée
        # TODO: avant de fermer.

        # On sauvegarde le résultat.

        # On redonne le contrôle au parent.
        self.grab_release()
        self.master.focus_set()
        self.destroy()
    def lire_regles(self):
        messagebox.showinfo("Règles du jeu","Le but du jeu est d'obtenir la combinaison ayant la plus grande valeur."
        "La combinaison valant le plus est le Quinton, soit lui avec 5 figures similaires, le carré avec 4 figures similaires."
        "Le full avec 3 figures similaires et suivis de 2 autre figures similaire,le brelan avec 3 figures similaires."
        "La séquence avec toutes les figures suivis l'une de l'autre, le double carré avec deux paires de figures "
        "et le carré avec une paire de figures. Chacun des joueurs à le droit 3 lancers sauf si le joueur précédent a"
        "a réussi en moins de coups, donc le nombre de coups réussis est le nouveau total")
    def charger_partie(self):
        try:
            Partie.restaure(Partie)
        except:
            messagebox.showerror("Erreur chargement","Le fichier de sauvegarde n'est pas disponible")
if __name__ == '__main__':
    # Instanciation de la fenêtre et démarrage de sa boucle principale.
    fenetre = mon_interface()
    fenetre.mainloop()