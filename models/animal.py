from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.soigneur import Soigneur

class Animal:
    def __init__(self, nom: str, soigneur: "Soigneur"):
        self.nom = nom
        self.soigneur = soigneur

        self.hp = 100
        self._appetit = 0
        self.satisfaction = 100

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, new_nom: str):
        new_nom = new_nom.strip()
        if type(new_nom) != str:
            raise TypeError("Le type du nom de l'animal doit être un string!")
        if len(new_nom) < 2:
            raise ValueError("Le nom doit contenir au moins 2 charactères!")
        if new_nom.lower() == 'gemini' or new_nom.lower() == 'grok':
            raise ValueError("T'abuses frero...")
        if not new_nom.isalpha():
            raise ValueError('Pas de numeriques dans le nom!')
        self._nom = new_nom

    @property
    def en_vie(self):
        return self.hp > 0

    @property
    def appetit(self):
        return self._appetit

    @property
    def satisfaction(self):
        return self._satisfaction

    @satisfaction.setter
    def satisfaction(self, new):
        if type(new) != int:
            raise TypeError('satisfaction en int uniquement')
        if new <= 0:
            raise ValueError('La satisfaction ne peut pas être negatif')
        if new > 100:
            raise ValueError('La satisfaction ne peut pas être au dessus de 100')
        self._satisfaction = new

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, new_hp):
        if type(new_hp) != int:
            raise TypeError('Hp en int uniquement')
        if new_hp <= 0:
            raise ValueError('Le hp ne peut pas être negatif')
        if new_hp > 100:
            raise ValueError('Le hp ne peut pas être au dessus de 100')
        self._hp = new_hp

    @property
    def soigneur(self):
        return self._soigneur

    @soigneur.setter
    def soigneur(self, new_soigneur: "Soigneur"):
        if not isinstance(new_soigneur, Soigneur):
            raise TypeError('Le soigneur doit être de type soigneur!')
        self._soigneur = new_soigneur
        #TODO monter le nb d'anmiaux responsable coté soigneur!!!
    
    def manger(self):
        if self.hp > 0:
            if self.appetit > 42:
                print("L'animal mange")
                self.appetit = 0
                self.hp = min(self.hp + 5, 100)
            else:
                print('Il est au régime!')
        else:
            print('Il est dead, il peut pas manger!')

    def __str__(self):
        return f"Animal : nom = {self.nom} - {self.hp} hp"

    def __repr__(self):
        return f"DEBUUUUUUUG Animal({self.nom})"

class AnimalExample:
    def __init__(self, nom):
        self.nom = nom

    def avancer(self):
        print("J'avance!")

class Chien(AnimalExample):
    def avancer(self):
        print("Wouf wouf j'avance")

    def parler(self):
        print('Wouf wouf')

class Chat(AnimalExample):
    def __init__(self, nom, collier_de_chat):
        super().__init__(nom)
        self.collier_de_chat = collier_de_chat

    def ronroner(self):
        print('ronrone...')

    def parler(self):
        print('Miaou')

# chien1 = Chien('jeko')
# chat1 = Chat('Garfield', 'collier')

# chien1.avancer()
# chat1.avancer()

# print(isinstance(chien1, Chat))

# animal_tab = [chien1, chat1]

# for animal in animal_tab:
#     animal.parler()
