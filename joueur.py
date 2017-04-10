from combinaison import Combinaison
import yaml

class Joueur:
    """Classe représentant un joueur.

    Attributes:
        nom (str): Le nom du joueur
        nb_victoires (int): Le nombre de parties remportées.
        nb_parties_jouees (int): Le nombre de parties jouées.
    """
    def __init__(self, nom):
        """
        Initialise un nouveau joueur avec son nom.

        Args:
            nom (str): Le nom du joueur.
        """
        self.nom = nom
        self.nb_victoires = 0
        self.nb_parties_jouees = 0
        self.restore = False
        self.termine = False

    def jouer_tour(self, limite_lancers,interface):
        """
        Joue le tour d'un joueur.
        Args:
            limite_lancers (int): Le nombre de lancers maximums.

        Returns (Combinaison): La combinaison obtenue

        """
        self.interface = interface
        if self.termine == True:
            pass
        elif self.restore == True:
            pass
        else:
            self.combinaison = Combinaison()


            while self.combinaison.nb_lancers < limite_lancers and not self.termine:
                print("Voici votre combinaison:")
                for i in range(0,len(self.combinaison.des)):
                    self.interface.de_buttom[i].config(text=self.combinaison.des[i])
                self.interface.relance_de = []
                self.interface.wait.set(True)
                self.interface.wait_variable(self.interface.wait)
                relance = self.interface.relance_de
                if relance == []:
                    self.termine = True
                else:
                    des_a_relancer = []
                    for de in relance:
                        des_a_relancer.append(de)
                    self.combinaison=self.combinaison.relancer_des(des_a_relancer)
            self.termine = True
            print("Voici votre combinaison:")
            print(str(self.combinaison))
            return self.combinaison, self.combinaison.nb_lancers

    def restaure_combinaison(self, combinaison):
        enlever =['>','<','[',']',' ','Carte.','NEUF','DIX','VALET','DAME','ROI','AS',':']
        de = []
        for t in enlever:
            combinaison = combinaison.replace(t,'')
        de_string = combinaison.split(',')
        for i in de_string:
            de.append(int(i))
        self.combinaison = Combinaison(de)

    def __str__(self):
        """
        Converti le joueur en une chaîne de caractères le représentant (le nom du joueur).
        Returns (str): La chaîne de caractères représentant le joueur.

        """
        return self.nom
