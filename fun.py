# funkcja - wydzielony fragment kodu ktory mozna wywolywac wielokrotnie

a = 6
b = 7

#funkcja moze przyjac wartosci z innego scope
 #  deklarowanie funkcji,  zapisuje wynik dzialania, tylko zapamietuje to miejsce umieszczenia funkcji


def dodaj(): #funkcja bezargumentowa
    print(a+b)  #wyswietli wynik dzialania,


def dodaj2(a,b): #funkcja z argumentami a i b (obowiazkowymi)
    print(a+b)


#parametr c jest opcjonalny pozswala zasymulowac przeciazenie funkcji liczba argumentow


def odejmij (a,b, c=0): #a i b obowiazkowe a c ma wartosc domyslna
    print(a-b-c)


#uruchomienie funkcji: nazwa i nawiasy
dodaj() #13
dodaj2(5,6) #11
odejmij(9,5)    #4
odejmij(9,5,2)  #2
odejmij(b=5, a = 9)
odejmij(c=2, b=5, a = 9)
# print(dodaj()) #None
# print(dodaj() = dodaj2(6,7) #wyjdzie blad nie moze dodawac dwoch funkcji
