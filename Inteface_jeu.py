from tkinter import Tk, Label, Button, BooleanVar, Checkbutton, Entry, messagebox, Toplevel, LabelFrame, Frame, GROOVE, \
    IntVar
from joueur import Joueur
from partie import Partie
from combinaison import Combinaison

nom1 =''
nom2 =''
nom3 =''

class mon_interface(Tk):
     def __init__(self):
         super().__init__()
         self.wait = BooleanVar()
         self.wait.set(False)
         self.relance_de = []
         self.frame_player1 = LabelFrame(self, text="Player 1", padx=20, pady=20)
         self.frame_player1.grid(row=1, column=1)
         self.player1 = Label(self.frame_player1,
                                       text="combinaison:\nLancer_restant:\nresultat:\npourcentage de parti gagnee:\nparti jouer:",
                                       justify="left")
         self.player1.grid()
         self.frame_player2 = LabelFrame(self, text="Player 2", padx=20, pady=20)
         self.frame_player2.grid(row=2, column=1)
         self.player2 = Label(self.frame_player2,
                                       text="combinaison:\nLancer_restant:\nresultat:\npourcentage de parti gagnee:\nparti jouer:",
                                       justify="left")
         self.player2.grid()
         self.frame_player3 = LabelFrame(self, text="Player 3", padx=20, pady=20)
         self.frame_player3.grid(row=3, column=1)
         self.player3 = Label(self.frame_player3,
                                       text="combinaison:\nLancer_restant:\nresultat:\npourcentage de parti gagnee:\nparti jouer:",
                                       justify="left")
         self.player3.grid()

         self.joueur_interface = [(self.frame_player1, self.player1), (self.frame_player2, self.player2),(self.frame_player3, self.player3)]

         self.tour_a = Label(self,text="C'est au tour de ",justify="center")
         self.tour_a.grid(row=1, column=2, columnspan=5)

         frame1 = Frame(self, borderwidth=2, relief=GROOVE).grid(row=2, column=2)
         self.de_1 = Button(frame1, text="0", width=2, height=2, command= lambda: self.buttom_action(0) ,padx=5, pady=5)
         self.de_1.grid(row=2, column=3)
         self.de_2 = Button(frame1, text="1", width=2, height=2, command= lambda: self.buttom_action(1),padx=5, pady=5)
         self.de_2.grid(row=2, column=4)
         self.de_3 = Button(frame1, text="2", width=2, height=2, command= lambda: self.buttom_action(2),padx=5, pady=5)
         self.de_3.grid(row=2, column=5)
         self.de_4 = Button(frame1, text="3", width=2, height=2, command= lambda: self.buttom_action(3),padx=5, pady=5)
         self.de_4.grid(row=2, column=6)
         self.de_5 = Button(frame1, text="4", width=2, height=2, command= lambda: self.buttom_action(4),padx=5, pady=5)
         self.de_5.grid(row=2, column=7)
         self.de_buttom = [self.de_1,self.de_2,self.de_3,self.de_4,self.de_5]
         Button(self, text="Nouvelle Partie",command=self.nouvelle_partie).grid(row=4, column=6, columnspan=4)
         Button(self, command=self.relance,text="Garder/Lancer dés").grid(row=3, column=2, columnspan=3)
         self.tour = Button(self, text="Tour suivant", command=self.next_game)
         self.tour.grid(row=4, column=2, columnspan=3)

         Button(self, text="Sauvegarde", command=self.sauvegarde).grid(row=3, column=6, columnspan=4)

         self.menu = menu(self)
     def next_game(self):
         self.partie = Partie(self.list_obj_joueur, self.master)
         self.tour.config(state="disabled")
         self.partie.jouer_partie()
         self.tour.config(state="normal")
     def sauvegarde(self):
         pass
     def relance(self):
         self.wait.set(False)

         self.update()
     def nouvelle_partie(self):
         Menu = menu(self)
     def terminer_partie(self):
        pass

     def buttom_action(self,index):
         if index in self.relance_de:
            self.de_buttom[index].config(text=self.partie.joueur_actif.combinaison.des[index])
            self.relance_de.remove(index)
         else:
            self.de_buttom[index].config(text="")
            self.relance_de.append(index)

class menu(Toplevel):


    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.transient(master)
        self.grab_set()
        self.nom_joueur1 = Entry(self)
        self.nom_joueur1.grid(row=2,column=3)
        joueur1= Label(self,text="Joueur 1").grid(row=1,column=3)
        self.nom_joueur2 = Entry(self)
        self.nom_joueur2.grid(row=2,column=4)
        joueur2= Label(self,text="Joueur 2").grid(row=1,column=4)
        self.nom_joueur3 = Entry(self)
        self.nom_joueur3.grid(row=2,column=5)
        joueur3= Label(self,text="Joueur 3").grid(row=1,column=5)
        self.joker_d_as = IntVar()
        self.check = Checkbutton(self,text="As en tant que joker",variable = self.joker_d_as)
        self.check.grid(row=4,column=5)
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
        list_joueur = []
        est_joker = self.joker_d_as.get()

        if(self.nom_joueur3.get() == ""):
            self.master.frame_player3.destroy()
            list_joueur.append(self.nom_joueur1.get())
            list_joueur.append(self.nom_joueur2.get())
        else:
            list_joueur.append(self.nom_joueur1.get())
            list_joueur.append(self.nom_joueur2.get())
            list_joueur.append(self.nom_joueur3.get())
            self.master.list_obj_joueur = []
        for i in list_joueur:
            joueur = Joueur(i)
            self.master.list_obj_joueur.append(joueur)
        self.master.partie = Partie(self.master.list_obj_joueur,self.master)
        self.grab_release()
        self.master.focus_set()
        self.destroy()
        self.master.tour.config(state="disabled")
        self.master.partie.jouer_partie()
        self.master.tour.config(state="normal")

        # On sauvegarde le résultat.

        # On redonne le contrôle au parent.

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
            messagebox.showerror("Fichier non disponible","Le fichier de sauvegarde n'est pas disponible")
            self.master.partie = Partie("test", self.master)
            self.master.partie.restaure()
            self.grab_release()
            self.master.focus_set()
            self.destroy()
            self.master.partie.restaure_partie()
if __name__ == '__main__':
    # Instanciation de la fenêtre et démarrage de sa boucle principale.
    fenetre = mon_interface()
    fenetre.mainloop()