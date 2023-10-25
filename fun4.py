# funkcje zagniezdzona

def fun1():
    print("To jest fun1")

    def fun2(): #funkcja zagniezdzona
        print("To jest fun2")
    return fun2 # zwraca tylko adres funkcji (nie dajemy())


print(fun1())   #<function fun1.<locals>.fun2 at 0x00000205ACB38680>
xfun = fun1()
print(xfun)     #<function fun1.<locals>.fun2 at 0x00000205ACB38680>
print(type(xfun))   #<class 'function'>
xfun()

