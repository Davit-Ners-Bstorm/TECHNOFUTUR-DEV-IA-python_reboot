class Elephant:
    def __init__(self, nom, soigneur):
        self.nom = nom
        self.soigneur = soigneur

        self.hp = 100
        self.appetit = 0
        self.satisfaction = 100

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, new_nom: str):
        new_nom = new_nom.strip()
        if type(new_nom) != str:
            raise TypeError("Le type du nom de l'elephant doit être un string!")
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
    
    def manger(self):
        if self.hp > 0:
            if self.appetit > 42:
                print("L'elephant mange")
                self.appetit = 0
                self.hp = min(self.hp + 5, 100)
            else:
                print('Il est au régime!')
        else:
            print('Il est dead, il peut pas manger!')

el1 = Elephant('Dumbo', 'grok')
print(el1.en_vie)
el1.en_vie = False
    