# for - petla interacyjna

import random

for i in range (10): #przedzial od 0...9
    print(i)

for i in range (10): #przedzial od 0...9
    pass # nic nie robi

for _ in range (10): # niema zmienna ale drukuje 0...9
    print(_)
    pass

for i in range(10):
    print(i*2)

#lotto wersja nr 2

lista2 = list(range(1,50)) #int od 1 do 49
lista_wynik = []
for i in range(6): # 0...5 bedzie 6 liczb
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    lista_wynik.append(wyn)
print(lista_wynik)

lista_wynik.sort()
print(lista_wynik)

for i in range(10): #bedzie od 0 do 9
    if i % 2 == 0:  #modulo reszta z dzielenia
        print(i, "jest parzysta")

    #dodoaje do listy jak elementy sa parzyste
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

# zamienia 2 na 3
lista3 = []
for j in range (10):
    if j % 2 == 0:
        lista3.append(j)
print(lista3)


print(lista3) #
for c in lista3:
    if c==2:
        c+= 1 #c=c+1
    print(c)

a = 1
a += 1 # a = a+1
print(a)  #2

a = 1
a -= 1 # a = a-1
print(a)  #0

a = 1
a *= 2 # a = a*2
print(a)  #2

a = 2
a /= 2 # a = a/2
print(a)  #1

a = 2
a /= 2 #a = a/2
print(a)  #1 dzielenie daje wynik typu float()
a %= 2
print(a) #1

imiona =["Radek", "Zenek", "Monika"]
print(imiona)
print(type(imiona))

for p in imiona:
    print(p)

#wyswietlic elementy z listy ale z indeksem
# 0 Radek
for p in imiona:
    print(imiona.index(p),p) # 0 Radek

for i in range(len(imiona)): #range(3) => 0,1,2
    print(i, imiona[i])

#enumerate - numeruje kolekcje
for p in enumerate(imiona):
    print(p)
for p, o in enumerate(imiona):
    print(p,o)

ludzie = ["Radek", "Janek","Asia", "Michal", "Tadek"]
wiek = [47,67,32,34]

#for i in ludzie:
#   print(i, wiek[ludzie.index(i)])
# dobre przy tej samej ilosci argumentow w obu zbiorach

#for i in zip(ludzie, wiek):
#    print(i)

for l, w in zip(ludzie, wiek):
    #print(l, w)
    print(l,w, sep = ';', end='') #modyfuikacja wydruku, zmiana spacji na srdnik i w jednej linijce
print()

#zgubil Tadka ale sie nie wywalil

for i in range (0,10,2): # 0...9 drukuje co druga start, stop krok
    print(i)

for i in range (0,-10, -2): #krok ujemny petla do tylu
    print(i)

#wypisac 0 Radek 47

for i in enumerate(zip(ludzie, wiek)):
    print()

for i, (l, w) in enumerate(zip(ludzie, wiek)):   #nawias oznacza grupowanie
    print(i, l, w)

#wytlumaczenie co to oznacza na gorze
for i, w in enumerate(zip(ludzie, wiek)):  # nawias oznacza grupowanie
    print(i, w)
ind, we (0,('Radek',47))
print(ind)
print(we)
l,w = ('Radek', 47)
print(l)
print(w)

