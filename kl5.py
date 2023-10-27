#dziedziczenie #wspolne pola ma ja te same nazwy, mozna je pozniej porownywac

class Pojazd:

    """
    klasa opisujaca pojazd
    """

    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")
class Samochod(Pojazd):

    """
    klasa opisujaca samochod
    """
    def __init__(self, kolor, marka):
    #pass
        super().__init__(kolor)
        self.marka = marka
        self.kolor = kolor

    def info(self):
        """
        metoda informujaca o cechach obiektu
        :return:  None
        """
        #print(f'{self.marka} :{self.kolor}')
        super().info()
        print(f"Samochod: {self.marka}")

poj = Pojazd("zielony")
poj.info()

sam = Samochod("czerwony", "Maserati")
sam.info()

print(sam.__doc__)
print(sam.info.__doc__)
