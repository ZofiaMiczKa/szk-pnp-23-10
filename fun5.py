#stworzenie funkcji kantor zaw dwie funkcje USD i EUR
#wykorzystanie funkcji wew w zaleznosci od parametru inicjujacego

def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota=0):
        print(f"wymieniam {kwota} dol = {kwota*4.10}")

    def eur(kwota=0):
        print(f"wymieniam {kwota} eur = {kwota * 4.50}")

    if waluta == 'eur':
        return eur
    else:
        return usd

kantor_usd = kantor('usd')
kantor_usd() #dolary

kantor_usd(1000)

kantor_eur=kantor('eur')
kantor_eur(1000)
