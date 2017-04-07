import yaml

from joueur import Joueur
from combinaison import Combinaison
from random import shuffle


class Partie:
    """Représente une partie du jeu de Poker d'As

    Attributes:
        joueurs (list): La liste des joueurs.
    """

    def __init__(self, joueurs):
        """Initialise une partie avec la liste de joueurs

        Args:
            joueurs (list): La liste des joueurs.
        """
        self.joueurs = joueurs

    def jouer_partie(self):
        """ Joue une partie entre tous les joueurs et détermine le gagnant.
        Le compteur du nombre de partie est incrémenté pour chacun des joueurs.
        Le compteur de victoires est incrémenté pour le joueur gagnant (si la partie n'est pas nulle).
        Le joueur gagnant est affiché à l'écran (ou un message indiquant que la partie est nulle, s'il y a lieu).
        """
        self.ordre = self._determiner_ordre()
        print("\n\nL'ordre est tiré au hasard.")
        for i in range(0, len(self.ordre)):
            joueur = self.joueurs[self.ordre[i]]
            print("Le joueur {} est {}".format(i+1, joueur))

        print()

        self.max_lancers = 3
        resultats = []

        for i in range(0, len(self.ordre)):
            index = self.ordre[i]
            joueur = self.joueurs[index]
            joueur.nb_parties_jouees += 1

            print("C'est au tour de {}\n".format(joueur))
            resultat, self.nb_tours = joueur.jouer_tour(self.max_lancers)
            if i == 0:
                self.max_lancers = self.nb_tours

            print("{} a eu {}\n\n".format(joueur, resultat.determiner_type_combinaison()))

            resultats.append((joueur, resultat))

        meilleur_joueur, _  = Combinaison.determiner_meilleur_combinaison(resultats)
        if meilleur_joueur is None:
            print("La partie est nulle.")
        else:
            print("{} a gagné".format(meilleur_joueur))
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
        save = {}
        etat =0
        save["joueur"] = {}
        for joueur in self.joueurs:
            save["joueur"][joueur.nom] = {}
            save["joueur"][joueur.nom]['emplacement'] = etat
            save["joueur"][joueur.nom]["parti_jouer"] = joueur.nb_parties_jouees
            save["joueur"][joueur.nom]["nombre_victoire"] = joueur.nb_victoires
            save["joueur"][joueur.nom]["combinaison"] = str(joueur.combinaison.des)
            save["joueur"][joueur.nom]["fin_tour"] = joueur.termine
            save["joueur"][joueur.nom]["nombre de lancer"] = joueur.combinaison.nb_lancers
            etat += 1
        save["partie"] = {}
        save["partie"]["ordre"] = self.ordre
        save["partie"]["limite"] = self.max_lancers
        with open('save.yml', 'w') as yaml_file:
            yaml.dump(save, yaml_file, default_flow_style=False)
        #print(yaml.dump(save, default_flow_style=False ))
    def restaure(self):
        with open("save.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        print(cfg)
        joueurs_restaure = []
        for joueur in cfg['joueur']:

            if len(joueurs_restaure) < cfg['joueur'][joueur]['emplacement']:
                joueurs_restaure.insert(cfg['joueur'][joueur]['emplacement'], Joueur(joueur))
            else:
                joueurs_restaure.append(Joueur(joueur))
        print(joueurs_restaure[0].nom)


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