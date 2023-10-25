def odejmij(a,b):
    return a-b

print(odejmij(6,7))
odejmij2 = lambda a, b: a-b #return jest domyslnie
print(odejmij2(6,7))

oblicz_vat = lambda cena, vat=23: cena * (100+vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000,7))

wiek = lambda x: "dziecko" if x<10 else ("nastolatek" if x<18 else "dorosly")
print(wiek(8))
print(wiek(15))
print(wiek(25))

lista=[1,2,3,4,5,6,7,8,10,23,50]
l = []  #pusta lista

for i in lista:
    l.append(i*2)
print(l)

# map() - bierxe kazdy element z kolekcji, wykonuja na nim operacje wg zadanej funkcji

def zmien(x):
    return x*2
print(f"Zastosowanie map():{list(map(zmien, lista))}")
print(f"Zastosowanie map():{list(map(lambda x:x*2, lista))}")
#lambda uzyta jako funkcja anonimowa w miejscu wykonania nie wymaga definicji
# filter () - bierze elementy kolekcji i sprawdza wg warunku zadanego funkcje

print(f' Zastosowanie filter(): {list(filter(lambda x:x<3,lista))}')
#zastosowanie filtra (): [1,2]

print(f' Zastosowanie filter(): {list(filter(lambda x:x>8,l))}')
print(f' Zastosowanie filter(): {list(filter(lambda x: 3 < x < 20, l))}')



