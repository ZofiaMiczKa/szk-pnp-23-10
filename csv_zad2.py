import csv

filename = "records.csv"

fields = []
rows = []

with open(filename, 'r') as csv_f:
    dialect= csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter) # ;
    print(dialect.quotechar)    # " - ustawienie domysle gdyz u nas brakuje
    csv_f.seek(0) #zerujemy ponownie wskaznik na element

    #csvreader = csv.reader(csv_f, delimiter = ';') #delimiter zmienia z zdefiniowanego jesli nie podajemy na co to na przecinek
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter) #delimiter zmienia z zdefiniowanego jesli nie podajemy na co to na przecinek

    print(csvreader)  #iterable, irterator - idzie po kolei od pierwszego do ostatniego
    fields = next(csvreader) #pobiera element i ustawia wskaznik na nastepny
    for row in csvreader:
        rows.append(row)

print(fields)
print(type(fields))
print(rows)
