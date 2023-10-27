#dekorator
#dodaje do funkcji dodoatkowe wlasciwosci

def dekor(funk):
    def wew():
        print("Dekorujemy")
        return(funk()) # tu z nawiasami bo wynik  dzialania
    return wew #tu bez nawaisow bo adres w pamieci (referencja)

@dekor
def hej():
    print("Hej!!!")

# Hej!!!
# Dekorujemy
# Hej!!!

hej()
dk = dekor(hej)
dk()

#po dodoaniu @dekor do funkcji hej
# Dekorujemy
# Hej!!!