# krotka - jest niezmienialna (przydatne przy wspolnej pracy nad jednym zbiorem) nie ulega modyfikacji, moze byc jednoelementowa jak stala ale rownoczesnie pelni funkce zmiennej
#zmienna - niezmienna moze byc traktowana jako zmienna
#ciag wartosci podobny jak lista ktore nie zmieniaja swoich wartosci nie dzialaja np sortowanie powoduje zmiane na liste


tupla = "Radek" # format tupla kiedy w wyniku sa okragle nawiasy i jest przecinek miedzy elementami

print(type(tupla))
temp = 36, 6
print(type(temp)) #class tuple

tupla2 = "Tomek", "Asia", "Zbyszek", "Marek"
print(type(tupla2))
print(tupla2)

tupla3 = (43, 55,22.34, 11, 200)
print(type(tupla3))
print(tupla3)

print(tupla2.index("Tomek")) #0
print(tupla2.count("Asia")) #1

a,b = 1,2
print(a)
print(b)

# a,b = 1, 2, 3 error za duzo danych
a, *b = 1, 2, 3, 4 # bierze pierwszy a z gwiazdka bierze reszte
print(a)
print (b)

#rozpakowanie tupli z dodoatkowymi elemantmi, do gwizdki dodaje dodotkowy element

imie, *imie2, imie3 = tupla2
print(imie)
print(imie2)
print(imie3)

*imie, imie2, imie3 = tupla2
print(imie)
print(imie2)
print(imie3)

print(sorted(tupla2)) #przy sortowaniu zmienia na liste
print(tupla2)
# opcja sortowania powoduje konwersje na tupli zwykla liste, nawiasy zmienily sie

lista = list(tupla2) #zmiana na liste
print(lista)
print(type(lista)) #class list








