from enums import Carte, TypeCombinaison
from random import choice, shuffle


class Combinaison:
    """Représente la combinaison d'un joueur
    Attributes:
        des (list): Liste des dés lancés.
        nb_lancers (int): Le nombre de lancés réalisés.
        types_cartes (list): Les différents types de cartes.
    """
    types_cartes = [
        Carte.AS, Carte.ROI, Carte.DAME, Carte.VALET, Carte.DIX, Carte.NEUF
    ]
    index_a_relancer = []
    def __init__(self, des = None,est_joker=True):
        """Initialise une combinaison"""
        self.nb_lancers = 1
        self.est_joker = est_joker
        if des is None:
            self.des = self._lancer_des(5)
        else:
            self.des = des

            if type(self.des[0]) == int:
                self.des = []
                for i in des:
                    self.des.append(self.types_cartes[i])


    def ajouter_des_a_index(self,numero,index_a_relancer):
        """
        Permet d'ajouter les dés sélectionnés à l'index
        :param numero: le numéro du dé sélectionné
        :param index_a_relancer: la liste de dés
        :return: l'index des dés à l'index à relancer
        """
        index_a_relancer.append(numero)
        return index_a_relancer

    def retourne_combinaison(self):
        """
        Convertit les éléments de la liste de dés en liste de chaînes de caractères
        :return: une combinaison d'éléments
        """
        chaine = []
        for elem in self.des:
            chaine.append(str(elem))
        return chaine


    def relancer_des(self, index_a_relancer):
        """Relance les dés spécifiés
        Args:
            index_a_relancer (list): Liste des index des dés à relancer.
        """
        if len(index_a_relancer) > 0:
            nouveaux_des = self._lancer_des(len(index_a_relancer))
            for i in range(0, len(index_a_relancer)):
                self.des[index_a_relancer[i]] = nouveaux_des[i]

            self.nb_lancers += 1
    def determiner_type_combinaison_sans_joker(self):
        """
        Détermine le type de la combinaison des dés en désactivant le paramètre As est un joker
        :return: le type de la combianison de dés
        """
        valeurs = []
        for elem in self.des:
            valeurs.append(elem.value)
        valeurs.sort()

        nb_identiques = []
        precedent = -1
        for elem in valeurs:
            if elem == precedent:
                nb_identiques[-1] += 1
            else:
                nb_identiques.append(1)
                precedent = elem


        nb_identiques.sort(reverse=True)
        if(Carte.AS in self.des and Carte.ROI in self.des and Carte.DAME in self.des and Carte.VALET in self.des and Carte.DIX in self.des) or (Carte.NEUF in self.des and Carte.ROI in self.des and Carte.DAME in self.des and Carte.VALET in self.des and Carte.DIX in self.des):
            return TypeCombinaison.SEQUENCE
        if nb_identiques[0] == 5:
            return TypeCombinaison.QUINTON
        if nb_identiques[0] == 4:
            return TypeCombinaison.CARRE
        if nb_identiques[0] == 3 and nb_identiques[1] == 2:
            return TypeCombinaison.FULL
        if nb_identiques[0] == 3:
            return TypeCombinaison.BRELAN
        if nb_identiques[0] == 2 and nb_identiques[1] == 2:
            return TypeCombinaison.DEUX_PAIRES
        if nb_identiques[0] == 2:
            return TypeCombinaison.UNE_PAIRE

        return TypeCombinaison.AUTRE

    def determiner_type_combinaison(self):
        """Détermine le type de la combinaison.
        Return (TypeCombinaison): Le type de la combinaison.
        """
        valeurs = []
        for elem in self.des:
            valeurs.append(elem.value)
        valeurs.sort()

        nb_identiques = []
        precedent = -1
        sequence = True
        nb_as = 0
        as_utilises_sequence = 0
        for elem in valeurs:
            if elem == Carte.AS.value:
                nb_as += 1
            elif precedent == elem:
                nb_identiques[-1] += 1
                sequence = False
            else:
                nb_identiques.append(1)
                if not (precedent == -1 or precedent == elem - 1):
                    if as_utilises_sequence >= nb_as:
                        sequence = False
                    else:
                        as_utilises_sequence += 1
            if elem != Carte.AS.value:
                precedent = elem

        nb_identiques.sort(reverse=True)

        if nb_as == 5 or nb_identiques[0] + nb_as == 5:
            return TypeCombinaison.QUINTON
        if nb_identiques[0] + nb_as == 4:
            return TypeCombinaison.CARRE
        if nb_identiques[0] + nb_as == 3 and nb_identiques[1] == 2:
            return TypeCombinaison.FULL
        if nb_identiques[0] + nb_as == 3:
            return TypeCombinaison.BRELAN
        if sequence:
            return TypeCombinaison.SEQUENCE
        if nb_identiques[0] == 2 and nb_identiques[1] == 2:
            return TypeCombinaison.DEUX_PAIRES
        if nb_identiques[0] + nb_as == 2:
            return TypeCombinaison.UNE_PAIRE

        return TypeCombinaison.AUTRE

    @staticmethod
    def determiner_meilleur_combinaison(combinaisons):
        """
        Méthode statique qui détermine la meilleure combinaison (et donc le meilleur joueur) parmi une liste.
        Args:
            combinaisons (list): Liste de combinaisons sous forme de liste de tuples (Joueur, Combinaison)
        Returns (tuple): Un tuple (Joueur, Combinaison) du meilleur joueur et de la meilleure combinaison ou (None, None)
                         en cas d'égalité. Il est à noter que le premier élément du tuple n'est pas nécessairement de
                         type Joueur. Ce peut être un objet quelconque (Joueur, entier, string, etc.), selon
                         l'utilisation souhaitée.
        """
        meilleur_valeur = -1
        meilleur_tuple = None
        egalite = False

        for joueur, combinaison in combinaisons:
            if joueur.est_joker == False:
                type = combinaison.determiner_type_combinaison_sans_joker()
            else:
                type = combinaison.determiner_type_combinaison()
            if type.value == meilleur_valeur:
                egalite = True
            elif type.value > meilleur_valeur:
                egalite = False
                meilleur_tuple = joueur, combinaison
                meilleur_valeur = type.value

        if egalite:
            return None, None
        return meilleur_tuple


    def _lancer_des(self, n):
        """Lance n dés.
        Args:
            n (int): Le nombre de dés à lancer.
        """
        resultats = []
        for _ in range(0, n):
            resultats.append(choice(self.types_cartes))
        return resultats

    def __str__(self):
        '''
        À vous de voir comment définir et utiliser
        :return: À définir selon vos besoins
        '''
        chaine = "Dés:    "
        for i in range(0, len(self.des)):
            chaine += "{:^3d}".format(i + 1)
        chaine += "\nValeur: "
        for elem in self.des:
            chaine += "{:^3s}".format(elem)
        return chaine + "\n"


if __name__ == "__main__":
    combinaison = Combinaison()
    # Test de init
    assert len(combinaison.des) == 5
    assert combinaison.nb_lancers == 1

    # Test de relancer_des
    combinaison.relancer_des([])
    assert combinaison.nb_lancers == 1
    anciens_des = list(combinaison.des)
    combinaison.relancer_des([3, 4])
    assert combinaison.nb_lancers == 2
    assert combinaison.des[0:2] == anciens_des[0:2]

    # Test de _lancer_des
    assert len(combinaison._lancer_des(5)) == 5
    assert len(combinaison._lancer_des(0)) == 0
    des = combinaison._lancer_des(5)
    for elem in des:
        assert isinstance(elem, Carte)

    # Test de str()
    combinaison.des = combinaison.types_cartes[0:5]
    assert "Dés:     1  2  3  4  5" in str(combinaison)
    assert "Valeur:  A  R  D  V  X" in str(combinaison)
    #test de type de fonction determiner_combinaison sans joker
    combinaisons = [
             # Combinaisons avec As
            ([Carte.AS, Carte.AS, Carte.AS, Carte.AS, Carte.AS],
             TypeCombinaison.QUINTON),
             ([Carte.ROI, Carte.AS, Carte.VALET, Carte.DIX, Carte.NEUF],
              TypeCombinaison.SEQUENCE),
             ([Carte.VALET] * 4 + [Carte.AS], TypeCombinaison.QUINTON),
             ([Carte.VALET] * 3 + [Carte.AS, Carte.ROI], TypeCombinaison.CARRE),
             ([Carte.VALET] * 2 + [Carte.ROI, Carte.AS, Carte.ROI],
              TypeCombinaison.FULL),
             ([Carte.VALET] * 2 + [Carte.ROI, Carte.AS, Carte.DAME],
              TypeCombinaison.BRELAN),
             ([Carte.ROI, Carte.DAME, Carte.AS, Carte.DIX, Carte.NEUF],
              TypeCombinaison.SEQUENCE),
             # Combinaisons sans As
             ([Carte.VALET] * 5, TypeCombinaison.QUINTON),
             ([Carte.VALET] * 4 + [Carte.ROI], TypeCombinaison.CARRE),
             ([Carte.VALET] * 3 + [Carte.ROI] * 2, TypeCombinaison.FULL),
             ([Carte.VALET] * 3 + [Carte.ROI, Carte.DAME], TypeCombinaison.BRELAN),
             ([Carte.AS, Carte.ROI, Carte.DAME, Carte.VALET, Carte.DIX],
              TypeCombinaison.SEQUENCE),
             ([Carte.ROI, Carte.DAME, Carte.VALET, Carte.DIX, Carte.NEUF],
              TypeCombinaison.SEQUENCE),
             ([Carte.ROI, Carte.ROI, Carte.VALET, Carte.VALET, Carte.NEUF],
              TypeCombinaison.DEUX_PAIRES),
             ([Carte.ROI, Carte.ROI, Carte.DIX, Carte.VALET, Carte.NEUF],
              TypeCombinaison.UNE_PAIRE)
             ]

    for des, vrai_type in combinaisons:
        shuffle(des)
        combinaison.des = des
        type = combinaison.determiner_type_combinaison()
        assert type == vrai_type
