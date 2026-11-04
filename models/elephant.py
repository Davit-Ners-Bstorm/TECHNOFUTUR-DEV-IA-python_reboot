from models.soigneur import Soigneur
from models.animal import Animal

class Elephant(Animal):
    def __init__(self, nom, soigneur, longueur_defense):
        super().__init__(nom, soigneur)
        self.longueur_defense = longueur_defense

    @property
    def longueur_defense(self):
        return self._longueur_defense

    @longueur_defense.setter
    def longueur_defense(self, new):
        # après checks
        self._longueur_defense = new
