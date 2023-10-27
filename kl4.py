class Dom:
    """
    Klasa opisująca dom w Pythonie
    """

    def __init__(self, metraz, kolor, liczba_okien): #inicjalizator, konstruktor
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def podaj_kolor(self):
        print(f'Mam kolor {self.__kolor}')

    def podaj_metraz(self):
        print(f'Mam metraz {self.__metraz}')

    def podaj_okna(self):
        print(f'Mam okien {self.__liczba_okien}')

    def zmien_metraz(self):
        wybor = int(input("Podaj metraz: "))
        self.__metraz = wybor
        self.podaj_metraz()

    def zmien_kolor(self):
        wybor2 = (input("Podaj kolor: "))
        self.__kolor = wybor2
        self.podaj_kolor()

    def zmien_okna(self):
        wybor3 = int(input("Podaj ilosc okien: "))
        self.__liczba_okien = wybor3
        self.podaj_okna()
        
dom1 = Dom(200, "szary",12)
dom1.podaj_okna()
dom1.podaj_metraz()
dom1.podaj_kolor()

# Mam okien 12
# Mam metraz 200
# Mam kolor szary

dom1.zmien_metraz()
dom1.zmien_kolor()
dom1.zmien_okna()

dom2 = Dom(100, "biały", 0)
dom1.podaj_kolor()
dom2.podaj_kolor()
