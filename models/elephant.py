class Elephant:
    def __init__(self, nom, soigneur):
        self.nom = nom
        self.soigneur = soigneur

        self.hp = 100
        self.appetit = 0
        self.satisfaction = 100

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

el1 = Elephant('Dumbo', 'Fabian')

el1.hp = 0

el1.manger()

    