from tkinter import Tk,Label,Button,Checkbutton,Entry,messagebox,Toplevel
from joueur import Joueur
from partie import Partie
from combinaison import Combinaison
nom1 =''
nom2 =''
nom3 =''
def partie_graphique():
    pass
    #Partie.joueurs.append(nom1,nom2,nom3)
    #Partie.jouer_partie(Partie)
    #fenetre = Toplevel()
    #joueur=Label(root,text="Test").grid(row=1,column=1)
    #lancer_des = Button(root,text="Lancer dés",command=Combinaison._lancer_des(Combinaison,5))
    #reset = Button(root,text="Redémarrer").grid(row=5,column=5)
    #fenetre.mainloop()
def charger_partie():
        try:
            pass
        except:
            messagebox.showerror("Erreur chargement","Le fichier de suavegarde n'est pas disponible")
def lire_regles():
    messagebox.showinfo("Règles du jeu","Le but du jeu est d'obtenir la combinaison ayant la plus grande valeur"
    "La combinaison valant le plus est le Quinton, soit lui avec 5 figures similaires, le carré avec 4 figures similaires"
    "Le full avec 3 figures similaires et suivis de 2 autre figures similaire,le brelan avec 3 figures similaires"
    "La séquence avec toutes les figures suivis l'une de l'autre, le double carré avec deux paires de figures "
    "et le carré avec une paire de figures. Chacun des joueurs à le droit 3 lancers sauf si le joueur précédent a"
    "a réussi en moins de coups, donc le nombre de coups réussis est le nouveau total")
root = Tk()
nom_joueur1 = Entry(root,textvariable=nom1).grid(row=2,column=3)
joueur1= Label(root,text="Joueur 1").grid(row=1,column=3)
nom_joueur2 = Entry(root,textvariable=nom2).grid(row=2,column=4)
joueur2= Label(root,text="Joueur 2").grid(row=1,column=4)
nom_joueur3 = Entry(root,textvariable=nom3).grid(row=2,column=5)
joueur3= Label(root,text="Joueur 3").grid(row=1,column=5)
joker_d_as = False
Checkbutton(root,text="As en tant que joker",variable = joker_d_as).grid(row=4,column=5)
commencer_partie = Button(root,text="Commencer",command = partie_graphique()).grid(row=4,column=2)
regles = Button(root,text="Lire règles",command=lire_regles).grid(row=4,column=3)
quitter = Button(root,text="Quitter",command=root.quit).grid(row=5,column=3)
restaurer = Button(root,text="Restaurer",command=charger_partie()).grid(row=5,column=2)
root.mainloop()
