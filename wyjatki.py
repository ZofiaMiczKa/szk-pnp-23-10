
while True:
    print("""
        1. Dodawanie
        2. Odejmowanie
        3. Mnozenie
        4. Dzielenie
        5. Koniec
        """)

    odp = input("Podaj opcje z menu")
    if odp == "5":
        break

    a = float(input("Podaj pierwsza liczbe"))
    b = float(input("Podaj druga liczbe"))
    if odp == "1":
        print(a+b)
    elif odp == '2':
        print(a-b)
    elif odp == '3':
        print(a*b)
    elif odp == '4':
        if b != 0:
            print(a/b)
        else:
            print("nie dziel przez zero")
    else:
        print("nie znam takiego zadania")
