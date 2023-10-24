#lista - kolekcja, przechowuje rozne typy
#zachowuje kolejnosc dodawania

lista =[] #pusta lista definiowane przez kwadratowy nawias

print(lista)
print(type(lista)) #class "list

lista.append("Radek") #dodawanie do listy
lista.append("Maciek") #dodawanie do listy
lista.append("Jaśko") #dodawanie do listy
lista.append("Zenek") #dodawanie do listy
print(lista)

#indeksowanie od 0
#['Radek', 'Maciek', 'Jaśko', 'Zenek']
#   0(-4)   1(-3)     2 (-2)      3 (-1)

print(lista[0]) #nazwa listy nawias indeks z litsy
print(lista[2])
#print(lista[10])  #error
print(lista[-1])
print(len(lista)) #poprzez dlugosc wyswietlamy ostatni elemnt z listy
print(lista[3])
print(lista[-3])
print(lista[1])
print(lista[0:3]) #z praej strony otwartty z lewej zamkniety
print(lista[:3]) #opcja skrocona
print(lista[2:]) #do konca wlacznie

print(lista[0:-2]) #['Radek', 'Maciek']
print(lista[-2:0])  #idzie w prawo, dlatego lista jest pusta

#nadpisanie elementu
lista[2] = "Mikolaj"
print(lista)

#wstawiamy element na konkretne miejsce
lista.insert(1,"Marcin")
print(lista)

#usuniecie elementu
lista.remove("Maciek") #usunie pierwszy napotkany obiekt o tej nazwie
print(lista)

#sprawdzanie indeksu dla elementu z listy
indeks = lista.index("Zenek")
print(indeks)

#usuniecie po indeksie
print(lista.pop(indeks)) #zwraca usuniety element
print(lista)

a =1
b = 3
a = b
print(a)
b = 7
print(a)

lista2=lista # w przypadku list kopiuje refrencje  a nie dane wsadowe (adres pamieci)
lista3=lista.copy() #kopiowanie wartosci z jednej listy do drugiej listy

print(lista)
print(lista2)

lista.clear() #usuniecie wszystkich elekementow z listy  nr 1 i z listy nr 2 bo jest tylko sciezka lista nr 3 jest skopiowana wiec sie nie usunie

print(lista)
print(lista2)

print(id(lista))
print(id(lista2))

print(lista3)
print(id(lista3))

liczby = [54,999,34,22,12.34,687]
#liczby = [54,999,34,22,12.34,687,"A"] #mozna je wymieszac rozne formaty ale juz nie da sie sortowac
print(liczby)
liczby.sort()
print(liczby)

lista_osoby =['radek', 'ola']
lista_osoby.sort(reverse=True) #sortowanie odwrocone
print(lista_osoby)

liczby.reverse() # odwrocona kolejnosc bez sortowania
print(liczby)

liczby[3] = 6666
print(liczby[0:3])
print(liczby[-2])
print(liczby[-3:]) #[666,22,12.34
liczby.remove(54)
print(liczby)

print(liczby.pop(3))
print(len(liczby))

tekst ="Python"
lista_1 = list(tekst) #zamiana str na list, rozpakowanie sekwencji
print(lista_1) #['P', 'y', 't', 'h', 'o', 'n']

lista_2 = [tekst] #stworzenie listy z danym jednym elementem
print(lista_2) #Python

krotka = tuple(liczby) #zamiana listy na krotke, tuple
print(type(krotka))
print(krotka)
