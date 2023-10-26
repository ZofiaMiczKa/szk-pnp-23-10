#CRUD - create, read, update, delete (system laczacy fronten z backhand)
#HTTP - post, get, pu/patch, delete (fronten
#baza - insert, select, update, delete (element backhand - baza + crud)
#Rest API

import requests as re
#lub pip install requests

#url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

#NBP wskazuje aby uzyc metody HHTP GET
response = re.get(url)
print(response)

#status odpowiedzi
#response [200]
# 3... - bledy przegladarki np przekierowanie
# 4... - blad danych np 404 brak zasobow, 400 bad requests - np. przekroczony limit
# 5... - bledy wewn serwera

#W przypadku braku danych dla prawidłowo określonego zakresu czasowego zwracany jest komunikat 404 Not Found
#W przypadku zadania nieprawidłowo sformułowanych zapytań serwis zwraca komunikat 400 Bad Request
#W przypadku zapytania przekraczającego limit zwracanych danych serwis zwróci komunikat 400 Bad Request - Przekroczony limit

table = response.json()
print(table)
#{'table': 'A', 'currency': 'euro', 'code': 'EUR', 'rates': [{'no': '207/A/NBP/2023', 'effectiveDate': '2023-10-25', 'mid': 4.4758}]}
print(type(table)) #<class 'dict'>

print(table.keys())
print(table['table'])   #A

for k in table.keys():
    print(k,table[k])

print(table['rates'][0])
for k in table['rates'][0]:
    print(k, table['rates'][0][k])

url_zloto = 'http://api.nbp.pl/api/cenyzlota'
reponse = re.get(url_zloto)
print(response)
gold = reponse.json()
print(gold)
print(gold[0]['cena'])

for k in gold[0]:
    print(k,'=>', gold[0][k])

#269.6
#data => 2023-10-26
#cena => 269.6
