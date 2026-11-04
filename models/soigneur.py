from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.elephant import Elephant

class Soigneur:
    def __init__(self, nom, dob):
        self.nom = nom
        self.dob = dob

        self._xp = 0
        self.nb_animaux_responsable = 0

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, new_nom: str):
        new_nom = new_nom.strip()
        if type(new_nom) != str:
            raise TypeError("Le type du nom de du soigneur doit être un string!")
        if len(new_nom) < 2:
            raise ValueError("Le nom doit contenir au moins 2 charactères!")
        if new_nom.lower() == 'gemini' or new_nom.lower() == 'grok':
            raise ValueError("T'abuses frero...")
        if not new_nom.isalpha():
            raise ValueError('Pas de numeriques dans le nom!')
        self._nom = new_nom

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, new_dob):
        if type(new_dob) != int:
            raise TypeError('Dob en int uniquement')
        if new_dob <= 0:
            raise ValueError('Le dob ne peut pas être negatif')
        self._dob = new_dob

    def nourrir(self, elephant: "Elephant"):
        if self != elephant.soigneur:
            raise ValueError('Pas le bon soigneur!!!')
        elephant.manger()
        self._xp += 15

    def entretenir(self, elephant: "Elephant"):
        if self != elephant.soigneur:
            raise ValueError('Pas le bon soigneur!!!')
        elephant.satisfaction = 100
        self._xp += 5
    