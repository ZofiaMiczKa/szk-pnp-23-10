import pickle # wspomaga dzialanie ze zlozonymi danymi

lista =[1,2,3,4,5]

with open('test_lista.txt','w') as f: #przypisujemy do zmiennej f
    f.write(str(lista))

with open('test_lista.txt','r') as f:
    lines = f.read()

print(lines)
print(type(lines))
print(list(lines))

with open('lista_pickle.log', 'wb') as z:
    pickle.dump(lista, z)

with open ('lista_pickle.log', 'rb') as z:
    loaded_list = pickle.load(z)

print(loaded_list)
print(type(loaded_list))
print(loaded_list)

