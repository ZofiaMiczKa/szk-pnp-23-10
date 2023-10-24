# slownik - para wyrazen: klucz i wartosc
# {"name" : "Radek"}

# klucze nie moga sie powtarzac


dictionary = {} #pusty slownik tu sa klamerki nawet przy pustym
print(type(dictionary)) #class 'dict'

dictionary['imie'] = 'Radek'
print(dictionary) #{'imie': 'Radek'}
dictionary['wiek'] = '39'
print(dictionary) #{'imie': 'Radek', 'wiek': '39'}

print(dictionary.values()) #otrzymujemy wartosci
print(dictionary.keys()) #otrzymujemy klucze
print(dictionary.items()) #lista par rzeczy w slowniku

dictionary.update({"date":'12-12-2023'})
print(dictionary)

dict2 = {'x':2}
dict2.update([("y",5),("z",7)])
print(dict2)

ang = {'dog':"pies", "camel": "wielblad", "turtle":"zolw"}
ang.update([("cat","kot"),("cow","krowa"),("horse","kon"),("mouse","mysz")])
print(ang)

print(ang.keys(),"linia30")
print(ang.keys())
print(f"Umiem przetlumaczyc {ang.keys()}")
key = input("podaj slowo do przetlumaczenia") #klucz
print(ang[key.lower().replace(" ","")])

#kalkulator

a = int(input("podaj pierwsza liczbe"))
b = input("podaj druga liczbe")
print(a+int(b))



