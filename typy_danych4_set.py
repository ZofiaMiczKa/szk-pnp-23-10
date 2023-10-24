# set - zbior - przechowuje niezduplikowane elementy
# nie zachwouje kolejnsoci przy dodawaniu elemwntow, elelmenty sa drukowane w przypadkowej kolejnosci
# mozna dodawac elementy
# elementy drukuje po nawiasie { jednka gdy jest pusty
#spowko pop usuwa pojedyncze pierwsze elekmety ze zbioru - gdyz kolejnosc jest losowa
#zbiory mozna porownywac jak w matematyce, czesc wspolna itp

lista = [44,55,66,777,33,22,11,33,11]
zbior = set(lista)

print(zbior) # {33, 66, 777, 11, 44, 22, 55} nawias klamerkowy dla listy

zb2 = set() #pusty zbior
print(zb2) #set()
print(type(zb2)) #class set

zbior.add(33)
zbior.add(18)
zbior.add(18)

print(zbior) #{33, 66, 777, 11, 44, 18, 22, 55}  #usuwane sa pierwsze elementy ze zbioru
print(zbior.pop())
print(zbior)
print(zbior.pop())
print(zbior.pop())
print(zbior.pop())
print(zbior) #{44, 18, 22, 55}

zbior.remove(55)
zbior.remove(18)
print(zbior) #{44, 22}

lista = list(zbior) #zamieniamy zbior na liste
print(lista) #[44, 22]

zbior2 = {667,11,44,18,52,62,999,999}
print(zbior2) #{18, 52, 999, 11, 44, 667, 62} #po jednym wystapieniu kazdej liczby

print(zbior | zbior2) #suma zbiorów
print(zbior & zbior2) #czesc wspolna 44
print(zbior - zbior2) #roznica zbiorów #22
print(zbior.difference(zbior2)) #suma zbiorów #22






