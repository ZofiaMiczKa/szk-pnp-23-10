#pliki csv - dane rozdzielone przecinkiem lub innym dopuszczalnym znakiem podzialu
#Zenek, Michal, Radek, Monika

import csv #biblioteka do pracowania z plikam csv (tandas do excela)

fields =['name','branch','year','cgpa']
row = ["Radek", 'cos', '3', '0']

filename = 'records.csv'
dict_list = [
    {'name':'Radek', 'branch':'coe', 'year':'3', 'cgpa':'0'},
    {'name':'Zosia', 'branch':'cos', 'year':'2', 'cgpa':'9'},
    {'name':'Asia', 'branch':'cot', 'year':'4', 'cgpa':'9.1'},
    {'name':'Monika', 'branch':'cob', 'year':'5', 'cgpa':'11'},
    {'name':'Zenek', 'branch':'coo', 'year':'7', 'cgpa':'11.5'}
]

dict_2 = dict(zip(fields, row))
print(dict_2)

with open (filename, 'w', newline = '') as csv_f: #otwieramy plik csv w PC i wprowadzamy dane w pierwszym wierszu, newline powpduje ze pusta linia znika
    #csvwriter = csv.writer(csv_f)
    csvwriter = csv.DictWriter(csv_f,fieldnames=fields,delimiter=",")
    #csvwriter.writerow(row)
    csvwriter.writeheader()
    csvwriter.writerow(dict_2)
    csvwriter.writerows(dict_list) #dodoanie wiecej wierszy