dictionary = {'imie':"Radek", "nazwisko":"Kowalski"}
print(dictionary)
print(type(dictionary)) #class dict

#zwraca klucze domyslnie
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

#zwraca wartości
for v in dictionary.values():
    print(v)

#zwraca pary
for p in dictionary.items():
    print(p) #(nazwisko kowalski)

for k, v in dictionary.items():
    print (k, "=>", v) #nazwisko => Kowalski

 # zamiana wartosci z kluczem transpozycja

dict1 = {'name':'imie', 'company':'Comarch'}
print(dict1)
print(type(dict1)) #class dict
print({value:key for key, value in dict1.items()})
# {'imie': 'name', "Comarch': 'Company"

d2 ={}
for key, value in dict1.items():
 #   d2.update({value: key})
    d2[value]=key
 print(d2)


