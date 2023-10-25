# funkcje zwracajace wynik musza byc zakonczone slowem return

def dodaj(a,b):
    return a+b

#dodaj(6,9) #tu wykonuje obliczenie, zeby wyswetlila wynik musimy wywolac print
print(dodaj(6, 9)) #na koncu dopisac .pr i enter wtedy dopisuje PRINT automatycznie z przodu

def dodaj2(a=2,b=5,c=10):
    print(a+b+c)

def oblicz_vat(cena,vat=23):
    return cena*(100+vat)/100

dodaj2()

def dodaj3(a=0,b=0,c=00):
    return(a+b+c)


print(dodaj3(5))
print(dodaj3(5,10))
print(dodaj3(5,10,10))
print(dodaj3(c=5,b=10,a=10))
#print(dodaj3(c=5,b=10,10)) #nie umie rozszyfrowac

print(oblicz_vat(1000))
print(oblicz_vat(1000,7))
print(oblicz_vat(vat=15, cena=1000))

