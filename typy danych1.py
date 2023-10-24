wiek = 47 #int
rok = 2023 #int
temp = 36.6 #loat
wiek2 =37.5 #float - tylko z kropka

print (wiek)
print( type (wiek2)) #<class 'float'>
print(5* "radek")

print (wiek + rok)
print (wiek * rok)
print (wiek / rok) #dzielenie daje w wyniku float
print (wiek - rok)
print (wiek // rok) #czesc calkowita z dzielenia
print (wiek % rok) #reszta z dzielenia tzw modulo
print (wiek ** rok) #potegowanie

print (5 % 2) # 1 bo 2 * 2 +1 =5
print (54 - 5 * 43 + 4 / 2 + 4 / 2) #rozpoznaje pierwszenstwo wykonywania dzialan
print (54 - 5 * 43 + (4 / 2 + 4) / 2)

print (0.2 + 0.8) # 1.0 float
print (0.2 + 0.7) # 0.89999999999999 blad zakraglenia przy liczeniu zmiennych typu float
# wystepuje blad w zaokraglenia

print(f"{0.2+0.7:.1f}")

print(f"sprawdzebie zmiennej temp {wiek} {temp}")
print(f"""
{wiek}
{temp}""")

#typ logiczny
#prawda lub fałsz

# true, false
czy_znasz_python = True
print(czy_znasz_python)
print(type(czy_znasz_python)) #<class 'bool'>

print(int(czy_znasz_python)) # true -1, false - 0
x=1
print(bool(x)) # bool() - zmiana na typ logiczny
x=100
print(bool(x))
x=-10
print(bool(x))
x=0
print(bool(x))

x="Radek"
print(bool(x))
x= ''
print(bool(x))
x= None
print(bool(x)) #sprawdzanie zmiennej czy cos jest

#dzialanie logiczne

print(True and True) #tylko tu bedzie True
print(True and False)
print(False and True)
print(False and False)

# or - lub

print(True or True)
print(True or False)
print(False or True)
print(False or False) #tylko tu bedzie False

#not
print (not False) #true
print (not True)  #false

x = 0
print(not x ==1) #true

a = 8
b = 7

print(f"porównanie {a}>{b}", a>b)
print(f"porównanie {a}<{b}", a<b)
print(f"porównanie {a}=={b}", a==b) # == porownanie
print(f"porównanie {a}!={b}", a!=b) # != czy rozne
print(f"porównanie {a}>={b}", a>=b)
print(f"porównanie {a}<={b}", a<=b)


