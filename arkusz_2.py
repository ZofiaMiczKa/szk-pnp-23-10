import pandas as pd

#excel_data = pd.read_excel('sales.xlsx', sheet_name="Arkusz1")
excel_data = pd.read_excel('sales.xlsx')

print(excel_data)

data = pd.DataFrame(excel_data)
print("The content is: \n", data) #n przenosi do nast linii
print("The content is: ", data)

print(data.values) # tylko wartosci
print(data.columns) # tylko kolumny
print(data.items) #calosc

print(data.index[-1]) #wyswietla ostatni numer wiersz
#3

print(data.index.max()) # wyswietla dane z ost wiersza
# for i in data.max

print(data.tail(1)) #ostatni wiersz od konca tail zwraca ost n wierszy gdy n=1 zwraca oststni wiersz, jak 2 to dwa oststnie
print(data.tail(2)) #ostatni wiersz od konca tail zwraca ost n wierszy gdy n=1 zwraca oststni wiersz, jak 2 to dwa oststnie

#print(data.columns[5]) # wiersz spoza zakresu wyjdzie blad

print(data.iloc[1,2])   #konkretna komorka zdefiniowana po indeksie
print(data.loc[1,"Amount"])   #konkretna komorka moze byc zdefiniowana  po nazwie kolumny
#print("Wiersz", data.iloc[1]) # wiersz 2 trzeba podac indeks kolumny
#print("Wiersz2:", data.loc[1]) # wiersz 2 moznqa podac po nazwie kolumny


