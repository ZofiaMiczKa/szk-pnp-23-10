teksty = 'Witaj w świecie'
print(teksty.upper())
print(teksty)
tekst2=teksty.upper()
print(tekst2)
print(teksty.lower())
tekst3 = teksty.lower()
print(tekst3)

print(teksty.removeprefix("Wit"))
print(teksty.removesuffix("cie"))
print(teksty.removesuffix("cie"))
print(teksty.removeprefix("Wit").removesuffix("cie")) #kazda operacja zwraca nowy tekst pierwotny tekst pozostaje ez zmian

print(teksty.count("i"))
print(teksty.count("i", 0,4)) # indeksowanie od zera 01234, w tym wypadku sprawdza od 0 do 3, 4 juz nie bierze pod uwage

tekst5 = teksty.encode('utf-8')
encoded_s = teksty.encode('utf-8')
print(tekst5) # musi byc polski znak

print(type(encoded_s))

imie ="Radek"
tekst_format = f"\tMam na {imie}\n i lubie Pythona\b" #tekst sformatowny poprzez znaki sterujace
print(tekst_format)

#\t tabulator
#\n nowa linia
#\b backspace

starszy = 'witaj %s!'
print(starszy % imie)

print("witaj {}!".format(imie))
print("""Tekst


Wielolinijkowy""") #do takiego tekstu trzy """ przed i po

