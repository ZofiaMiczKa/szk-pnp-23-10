#match case

lista=[]
lang = input("podaj znany Ci jezyk programowania")
match lang:
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case _: #domysly odpowiednik elase
        print('nie znam takiego jezyka')
print(lista)


