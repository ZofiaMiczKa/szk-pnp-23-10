#Klasa abstrakcyjna - klasa dla ktorej nie mozna stworzyc obiektow

from abc import ABC, abstractmethod

class Ptak(ABC):
    """
    klasa opisujaca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lece z szybkoscia", self.szybkosc)

    @abstractmethod #metoda staje sie abstraklcyjna i nie bedzie mozna stworzyc obiektow dla tej klasy
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek,0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko")

class Orzel(Ptak):
    def wydaj_odglos(self):
        print("yeeeehhhh")

#po dodaniu @abstractmethod klasa stala sie abstrakcyjna
#nie mozna utworzyc obiektu takiej klasy

# orzel = Ptak("Orzel", 48)
# orzel.latam()
#
# kur = Ptak("Kura", 0)
# kur.latam()

kur2 = Kura("Kurczak")
kur2.latam()

kur2.wydaj_odglos()

or2 = Orzel("Orzel", 48)
or2.latam()
or2.wydaj_odglos()
