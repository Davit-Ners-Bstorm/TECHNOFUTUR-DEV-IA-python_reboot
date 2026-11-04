from models.animal import Animal

class Girafe(Animal):
    def __init__(self, nom, soigneur, longueur_cou):
        super().__init__(nom, soigneur)
        self.longueur_cou = longueur_cou

    @property
    def longueur_cou(self):
        return self._longueur_cou

    @longueur_cou.setter
    def longueur_cou(self, new):
        # checks
        self._longueur_cou = new

    def manger(self):
        print('Il mange des feuilles')

