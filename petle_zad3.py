# while - petla sterowana warunkiem

# licznik =0
# while True:
#    print("komunikat1")

# petla idzie w nieskonczionosc

licznik = 0
while True:
    licznik += 1
    print("komunikat1")
    if licznik > 10:
        break  # przerwanie biezacej petli
print(licznik)  # 11
licznik = 0
while licznik < 10:
    print("komunikat2")
    licznik += 1

lista = []
lista2 =[]
while True:
    wej = input("Podaj liczbe")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)  # 4, 5 , 6 , 7 lista stringow
print(lista2)  # 4 5 6 7  - lista int
