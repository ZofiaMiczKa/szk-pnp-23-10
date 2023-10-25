
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
    try:
        a = float(input("Podaj pierwsza liczbe"))
        b = float(input("Podaj druga liczbe"))
        if odp == "1":
            print(a+b)
        elif odp == '2':
            print(a-b)
        elif odp == '3':
            print(a*b)
        elif odp == '4':
            #  if b != 0:
            print(a / b)
            #  else:
            #  print("Nie dziel przez zero")
        else:
            print("Nie znam takiego dzialania")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Blad wartosci")
    except TypeError:
        print("Blad typu")
    except Exception as e:
        print("Wystapil blad", e)  # wystapil kazdy inny blad
    else:
        print("Tylko gdy nie ma bledow")
    finally:
        print("Wykonuje sie zawsze")  # drukuje sie niezaleznie od wystepowania bledu
