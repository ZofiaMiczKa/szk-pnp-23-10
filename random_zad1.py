import random

#random - biblioteka do dzialnia z liczbami pseudolosowymi

print(random.randint(1,6)) # przedzial domkniety
print(random.random()) #float 0 ..... 0.9999999 nie wyjdziesz powyzj jedynki
print(random.random()*6) #float od 0... 5.9999
print(random.randrange(6)) #int 0...5
print(random.randrange(1,6)) #int 1...5

lista = [5,7,45,34,56]
print(random.choice(lista)) #34 losowanie z listy

lista2 =list(range(1,50)) #int od 1...49 generowani listy liczb od 1 do 49
print(lista2)

lista_wynik = []
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
lista_wynik.append(wyn)
print(lista_wynik)

print(random.choices(lista2, k=6)) #losowane wartosci tu sie powtarzaja [46, 25, 24, 9, 16, 16]
print(random.sample(lista2, 6)) #losowane wartosci tu sie nie powtarzaja [31, 34, 19, 24, 37, 35]

