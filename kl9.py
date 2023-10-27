class MyException(Exception): #dziedziczymy po klasie exception - glownym wyjatku w Pythonie
    def __init__(self, message):
        super().__init__(message)

try:
 #  print(6/0)
    raise ValueError("Blad wartosci")
# powystapieniu pierwszego bledu, program przerywa dzialanie i kiruje sie do sekcji obslugi bledow
    raise MyException('Wystapil wyjatek')
except ZeroDivisionError:
    print("Dzielenie przez Zero")
except MyException:
    print("Wystapil wyjatek MeException")
except Exception as e:
    print("Blad:", e)

print('Program nadal działa')