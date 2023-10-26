class Car:
    """
    Klasa opisująca samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
    #pole prywatne
        self.__predkosc =0

    def gaz(self):
        self.__predkosc+=10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Jedziesz z szybkoscia {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -=25

    def __zmien_bieg(self):
        print("Zmiana biegu")

ferrari = Car("Ferrari", 1960)
ferrari.gaz()
ferrari.gaz()
ferrari.gaz()
ferrari.gaz()
ferrari.gaz()
#print(ferrari.__predkosc)  #50

#pole nie istnieje

ferrari.licznik()
ferrari.__predkosc = 0
ferrari.__predkosc = 100
ferrari.licznik()

print(ferrari.__predkosc)
ferrari.hamuj()
ferrari.hamuj()
ferrari.licznik()
print(ferrari.__predkosc)
