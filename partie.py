import yaml

from joueur import Joueur
from combinaison import Combinaison
from random import shuffle


class Partie:
    """Représente une partie du jeu de Poker d'As
    Attributes:
        joueurs (list): La liste des joueurs.
    """

    def __init__(self, joueurs, interface):
        """Initialise une partie avec la liste de joueurs
        Args:
            joueurs (list): La liste des joueurs.
        """

        self.joueurs = joueurs
        self.interface = interface
        self.max_lancers = 3
        self.nb_tours = 0
        for joueur in joueurs:
            joueur.termine = False
        self.restore = False

    def restaure_partie(self):
        """
        Permet de restaurer une partie qui a déjà été exécutée
        :return: aucun paramètre
        """
        for i in range(0, len(self.ordre)):
            index = self.ordre[i]
            joueur = self.joueurs[index]
            self.update_interface_joueur(index,joueur)
            if joueur.termine == True:
                pass

    def update_interface_joueur(self,index,joueur):
        """
        met à jour l'interface du joueur
        :param index: la position dans le tableau
        :param joueur: le joueur actif
        :return: aucun paramètre retourné
        """
        self.interface.joueur_interface[index][0].config(text=joueur.nom)
        try:
            if joueur.est_joker == False:
                result = str(joueur.combinaison.determiner_type_combinaison_sans_joker())
            else:
                result = str(joueur.combinaison.determiner_type_combinaison())
            cbn =""
            for i in joueur.combinaison.retourne_combinaison():
                cbn += i + " "
                try:
                    pourcent = joueur.nb_victoires * 100 / joueur.nb_parties_jouees
                    label = "combinaison: " + cbn + "\nresultat: " + result + "\nnombre de parti gagnee: " + str(joueur.nb_victoires)  +"\nparti jouer: " + str(joueur.nb_parties_jouees)+"\npourcentage: " + str(round(pourcent,2)) + " %"
                except:
                    label = "combinaison: " + cbn + "\nresultat: " + result + "\nnombre de parti gagnee: " + str(joueur.nb_victoires) + "\nparti jouer: " + str(joueur.nb_parties_jouees)
        except AttributeError or IndexError:
            try:
                pourcent = joueur.nb_victoires * 100 / joueur.nb_parties_jouees
                label = "combinaison: \nresultat: \nnombre de parti gagnee: " + str(joueur.nb_victoires)  +"\nparti jouer: " + str(joueur.nb_parties_jouees)+"\npourcentage: " + str(round(pourcent,2)) + " %"
            except:
                label = "combinaison: \nresultat: \nnombre de parti gagnee: " + str(joueur.nb_victoires)  +"\nparti jouer: " + str(joueur.nb_parties_jouees)

        self.interface.joueur_interface[index][1].config(text=label)

    def jouer_partie(self):
        """ Joue une partie entre tous les joueurs et détermine le gagnant.
        Le compteur du nombre de parties est incrémenté pour chacun des joueurs.
        Le compteur de victoires est incrémenté pour le joueur gagnant (si la partie n'est pas nulle).
        Le joueur gagnant est affiché à l'écran (ou un message indiquant que la partie est nulle, s'il y a lieu).
        """
        if self.restore == False:
            self.ordre = self._determiner_ordre()

        for i in range(0, len(self.ordre)):
            index = self.ordre[i]

            self.joueur_actif = self.joueurs[self.ordre[i]]
            if self.restore == False:
                try:
                    self.joueur_actif.combinaison = 1
                except AttributeError:
                    pass
            self.update_interface_joueur(index, self.joueur_actif)

        self.max_lancers = 3
        resultats = []

        for i in range(0, len(self.ordre)):
            self.interface.sauvegarde.config(state="normal")
            index = self.ordre[i]

            self.joueur_actif = self.joueurs[index]
            try:
                if type(self.joueur_actif.combinaison.des) != list:
                    pass
            except AttributeError:
                self.joueur_actif.nb_parties_jouees += 1

            self.interface.tour_a.config(text="C'est au tour de {}\n".format(self.joueur_actif))
            self.update_interface_joueur(index, self.joueur_actif)


            resultat, self.nb_tours = self.joueur_actif.jouer_tour(self.max_lancers)
            if i == 0:
                self.max_lancers = self.nb_tours

            self.update_interface_joueur(index, self.joueur_actif)

            resultats.append((self.joueur_actif, resultat))

        meilleur_joueur, _  = Combinaison.determiner_meilleur_combinaison(resultats)
        if meilleur_joueur is None:
            self.interface.tour_a.config(text="La partie est nulle.")
        else:
            self.interface.tour_a.config(text="{} a gagné".format(meilleur_joueur))
            meilleur_joueur.nb_victoires += 1

    def _determiner_ordre(self):
        """Détermine l'ordre dans lequel les joueurs vont jouer.
        Return (list): La liste des index des joueurs indiquant l'ordre.
        Exemple:
            [2, 1, 0] indique que joueur 3 joue, suivi du joueur 2, puis du
            joueur 1.
        """
        ordre = list(range(0, len(self.joueurs)))
        shuffle(ordre)
        return ordre

    def sauvegarde(self):
        """
        Sauvegarde les paramètres de la partie sous un fichier yaml.
        :return: aucun paramètre
        """
        save = {}
        etat =0
        save["joueur"] = {}
        for joueur in self.joueurs:
            save["joueur"][joueur.nom] = {}
            save["joueur"][joueur.nom]['emplacement'] = etat
            save["joueur"][joueur.nom]["parti_jouer"] = joueur.nb_parties_jouees
            save["joueur"][joueur.nom]["nombre_victoire"] = joueur.nb_victoires
            save["joueur"][joueur.nom]["est_joker"] = joueur.est_joker
            try:
                save["joueur"][joueur.nom]["combinaison"] = str(joueur.combinaison.des)
                save["joueur"][joueur.nom]["fin_tour"] = joueur.termine
                save["joueur"][joueur.nom]["nombre de lancer"] = joueur.combinaison.nb_lancers
            except AttributeError:
                save["joueur"][joueur.nom]["fin_tour"] = False

            etat += 1
        save["partie"] = {}
        save["partie"]["ordre"] = self.ordre
        save["partie"]["limite"] = self.max_lancers
        with open('save.yml', 'w') as yaml_file:
            yaml.dump(save, yaml_file, default_flow_style=False)
        #print(yaml.dump(save, default_flow_style=False ))

    def restaure(self):
        """
        restaure le fichier yaml de parties et charge les paramètres dans la partie.
        :return: aucun paramètre
        """
        with open("save.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        joueurs_restaure = []
        for joueur in cfg['joueur']:
            joueurs_restaure.append(joueur)

        for joueur in cfg['joueur']:

            joueurs_restaure[cfg['joueur'][joueur]['emplacement']] = Joueur(joueur,self.interface,cfg['joueur'][joueur]['est_joker'])
            joueurs_restaure[cfg['joueur'][joueur]['emplacement']].nb_parties_jouees = cfg['joueur'][joueur]['parti_jouer']
            joueurs_restaure[cfg['joueur'][joueur]['emplacement']].nb_victoires = cfg['joueur'][joueur]['nombre_victoire']
            joueurs_restaure[cfg['joueur'][joueur]['emplacement']].termine = cfg['joueur'][joueur]['fin_tour']

            try:
                joueurs_restaure[cfg['joueur'][joueur]['emplacement']].restaure_combinaison(cfg['joueur'][joueur]['combinaison'])
                joueurs_restaure[cfg['joueur'][joueur]['emplacement']].combinaison.nb_lancers = cfg['joueur'][joueur]['nombre de lancer']
            except KeyError:
                joueurs_restaure[cfg['joueur'][joueur]['emplacement']].nb_lancers = 0
            self.ordre = cfg["partie"]["ordre"]
            self.max_lancers = cfg["partie"]["limite"]
        self.joueurs = joueurs_restaure
        self.interface.list_obj_joueur = self.joueurs


if __name__ == "__main__":
    joueurs = [Joueur("a"), Joueur("b"), Joueur("c")]

    partie = Partie(joueurs)

    # Teste que tous les joueurs vont jouer une et une seule fois
    ordre = partie._determiner_ordre()
    assert len(ordre) == 3
    assert 0 in ordre
    assert 1 in ordre
    assert 2 in ordre

    partie.restaure()
