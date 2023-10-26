class Human:
    """
    Klasa czlowiek w Pythonie
    """

    def __init__(self, imie, wiek, plec ='k'): #inicjalizator, konstruktor
        self.imie = imie
        self.wiek = wiek
        self.plec = plec
    def powitanie(self):
        print(f"Mam na imie {self.imie}")

    def podaj_wiek(self):
        print(f'Wiek {self.wiek}')

    def podaj_plec(self):
        print(f'Plec {self.plec}')

cz1 = Human ("Ania",'39')
print(cz1.wiek)
print(cz1.plec)
print(cz1.imie)
cz1.powitanie()
cz1.podaj_wiek()
cz1.podaj_plec()
