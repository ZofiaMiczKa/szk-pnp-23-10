user = "Tomek" #string
wiek = 39 #integer - calkowiet
wersja = 3.900001 #float zmiennoprzecinkowe
liczba = 13456112456 #integer

print("witaj %s masz teraz %d lat" % (user, wiek)) #definiujemy po kolei zgodnie z formatami
# print("witaj %s masz teraz %d lat") % (wiek, user) #wychopdzi blad ze wzgl na bledny format
print("witaj %d masz teraz %s lat" % (wiek, user)) #poprawione formaty

# %s - string
# %d - digit

print ("witaj %(user)s, masz teraz %(age)d lat." % {'user':user, 'age':wiek})

print ("witaj {} masz teraz {} lat".format(user,wiek))
print ("witaj {} masz teraz {} lat".format(wiek, user))
# nie weryfikuje typow

print (f"witaj {user}, masz teraz {wiek} lat.")
# f - f string - sformatowany string

print("uzywamy wersji Pythona %i"%3)
print("uzywamy wersji Pythona %f"%3.8)
print("uzywamy wersji Pythona %.1f"%3.8)
print("uzywamy wersji Pythona %.3f"%3.8)
print("uzywamy wersji Pythona %.0f"%3.8)
print("uzywamy wersji Pythona %.f"%3.8) #zaokraglenie

print("uzywamy wersji Pythona {}".format(wersja)) #pobiera zmienna z gory
print(f"uzywamy wersji Pythona {wersja}")
print(f"uzywamy wersji Pythona {wersja:.1f}")
print(f"uzywamy wersji Pythona {wersja:.2f}")
print(f"uzywamy wersji Pythona {wersja:.0f}")

print(f"{user:>10}") #  Tomek
print(f"{user:>20}") #      Tomek
print(f"{user:<20}") #Tomek
print(f"{user:^10}") #" Tomek  "    #wysrodkowuje

print("Nasza duża liczba {:,}".format(liczba))
print("Nasza duża liczba {:,}".format(liczba).replace(",","."))
print("Nasza duża liczba {:,}".format(liczba).replace(","," "))
print(f"Nasza duża liczba {liczba:,}".replace(","," "))





