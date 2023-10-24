#if warunek - instrukcja streowania przeplywem

#odp = True
#if odp :       #jesli jest cokolwiek to jest true, jesli nic nie ma to jest False
#    print("Brawo") # to co jest w warunku tylko w w tej linijce
#print('Ide dalej') # to jest poza warunkiem jesli jest bez wciecia

# odp = True
odp = True
if odp :       #jesli jest cokolwiek to jest true, jesli nic nie ma to jest False
    print("Brawo") # to co jest w warunki tylko w w tej linijce
else:
    print('Ucz sie dalej') # to jest drugi warunek
print("Ide dalej")


podatek = 0.9
zarobki = int(input('podaj dochod'))
if zarobki <10000:
    podatek = 0.1
elif zarobki <29000:
    podatek = 0.2
elif zarobki <100000:
    podatek = 0.4
else:
    podatek = 0.6

print(f"placisz {zarobki *podatek}")


suma_zam = 250
if suma_zam>150:
    rabacik = 25
else:
    rabacik =0
print(f'Rbacik wynosi{rabacik}')

rabat = 25 if suma_zam >150 else 0
print(f'Rabat wynosi:{rabat}')

#zasymulujemy system zbierania logow i wyswietlania komunikatow od tego jaki system i jaki komunikat przyslal
lista_bledow =[]
alert_system ="console"
error = 'critical'
error_message = "Stało sie cos starsznego"

if alert_system == 'email':
    print(error_message)
elif alert_system == 'console':
    if error == 'medium':
        lista_bledow.append("ostrzezenie")
    elif error == 'critical':
        lista_bledow.append("krytyczny")
    else:
        lista_bledow.append("inny")

print(lista_bledow)

stolica = (input("Jaka jest stolica Polski?")) #input zawsze zwraca w formacie string, zmiana tylko jesli chcemy na integer
if stolica == "Warszawa":
    print("wspaniale! :)")
else:
    print("fatalnie! :(")

odp = (input("Jaka jest data chrztu Polski?")) #input zawsze zwraca w formacie string, zmiana tylko jesli chcemy na integer
if odp == "966":      #traktujemy w tym wypadku ciag znaow jako tekst
    print("Brawo")
else:
    print("sprawdz w ksiazce")


