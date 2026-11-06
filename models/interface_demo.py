from abc import ABC, abstractmethod

class Vehicule(ABC):
    def __init__(self, marque):
        self._marque = marque

    @abstractmethod
    def demarrer(self):
        pass

    @property
    def marque(self):
        return self._marque

    @property
    @abstractmethod
    def moteur(self):
        pass



class VoitureThermique(Vehicule, ABC):

    @property
    def moteur(self):
        return f"GROS MOTEUR THERMIQUE"

    def demarrer(self):
        print('La voiture demare VROUM VROUM')

    @property
    @abstractmethod
    def nb_tour_minutes(self):
        pass


class VoitureEssence(VoitureThermique):
    @property
    def nb_tour_minutes(self):
        return 8


class VoitureDiesel(VoitureThermique):
    @property
    def nb_tour_minutes(self):
        5

voiture = VoitureEssence('Mercedes')

print(voiture)

voiture.demarrer()

print(voiture.marque)


class VoitureElectrique(Vehicule):
    def demarrer(self):
        print('Demmarage de la voiture electrique BIIIP')

    @property
    def moteur(self):
        return 'MOTEUR ELECTRIQUE'

voiture_electrique = VoitureElectrique('Tesla')

voiture_electrique.demarrer()
