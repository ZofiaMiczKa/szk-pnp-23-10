#wielodziedziczenie

# w Pythonie klasa moze dziedziczyc po wielu klasach

class A:
    def method(self):
        print('Metoda z klasy A')



class B:
    def method(self):
        print("Metoda z klasy B")

class C(A,B):       #dziedziczy po pierwszej klasie z listy
    """
    Klasa C dziedziczy po klasie A i po klasie B
    """

    def method(self):
        print("Metoda z klasy C")
        super().method()
        B.method(self)

a = A()
b = B()
a.method()
b.method()
c = C()
c.method()

print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# kolejnosc w zapisie dziedziczenia ma znaczenie C(B,A)
#C(A,B)

#C(B,A)
#(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

#po napisaniu metod w klasie C mamy wynk
# Metoda z klasy C
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

#po dodoaniu w klasie C super mamy wynik
# Metoda z klasy A
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

#mozemy wskazac z ktorej klasy ma byc uzyta method
# B.method(self)
# wynik dla klasy C:
# Metoda z klasy C
# Metoda z klasy A
# Metoda z klasy B