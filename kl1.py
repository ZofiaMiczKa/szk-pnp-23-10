# klasa - wyznacza cechy i funkcje dla obiektu / wprowadzony standard
# szablon - moze okreslac pola i funkcje
# instancja klasy jest obiekt
# obiekt - elelemn zvudiwany wg wytycznych zawartych w klasie
# programowanie obiektowe

class Human:
    """
    Klasa opisujaca Człowieka w Pythonie
    """
    imie =""
    wiek = None
    plec= 'k'

    def powitanie(self):
        print(f'Nazywam sie {self.imie}')

    def podaj_wiek(self):
        print(f'Wiek:{self.wiek}')

print(Human.__doc__)
print(print.__doc__)

cz1 = Human()
print(cz1)
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz1.imie = "Ania"
cz1.wiek = "45"

print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz2 = Human()
cz2.imie = "Witek"
cz2.wiek = "20"
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)

cz2.powitanie()
cz1.podaj_wiek()

