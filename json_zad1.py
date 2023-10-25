#json - {"name":"Radek"}
#obiekt typu klucz - wartosc
#odpowiednikiem jsona w pythonie jest slownik
import json

person_dict = {"name": "Radek","age" : "40","czy pali": None}
print(type(person_dict))

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict,f, indent=4, sort_keys=True) #dump zrzuc do pliku indent zmiana na osobne linijki, sort keys sortowanie po kluczach alfabetycznie
#{"name": "Radek", "age": "40", "czy pali": null}


with open('nasze_dane.json', "r") as fh:
    data = json.load(fh) #wczytanie jsona do slownika w pythonie

print(data)
print(type(data)) # {'age': '40', 'czy pali': None, 'name': 'Radek'}
print(data['name']) #Radek

json_text = json.dumps(data)
#zamiana slownika na json w formie str
print(json_text)
string_json = json.loads(json_text)
print(string_json)

#roznice "" null zamiast none