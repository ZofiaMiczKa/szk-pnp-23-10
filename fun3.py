a=10
b=10

def dodaj():
    a=6
    b=7
    print(a,b) #zakres lokalny

def dodaj2(): #uzyje z globalnego scopa (globalny zakreas)
    print(a+b)

def dodaj3():
    global a #zmieniamy globalna wattosc dla a ale dopiero po jej uruchomieniu
    a=6
    b=7
    print(a+b)

def dodaj4(a,b):
    print(a,b)

print(f'Zmienna a z gory {a}')  #daje wynik z gory 10 zakres calosciowy
dodaj() # a,b
print(f'Zmienna a z gory {a}') #daje wynik z gory 10 zakres calosciowy
dodaj2()    # 20
print(f'zmienna a z gory {a}') #daje wynik z gory 10 zakres calosciowy
dodaj3()                        #zmienia gloablnie z 10 a na nowe na 6, jakby nie bylo komendy dodaj3 to by nie nadpisal a
print(f'Zmianna a z góry {a}')   #zamienia wynik z gory na 6
dodaj2()    #patrzy na zmieniona wartosc a
dodaj4(a,b)