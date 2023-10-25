def connect(**opcje):   # parametry slownikowe

    print(opcje)
    print(type(opcje))  #<class 'dict'>

    connect_param ={
        "host":"127.0.0.7",
        "port":"8080"
    }
    print(connect_param)
    connect_param['pwd'] = opcje
    print(connect_param)


def connect_all(*args, **kwargs):
    print(args) # pozycyjny czyli bez nazwy zdefiniowanej np jako a, b lub c po * robia sie krotka
    print(kwargs) # slownikowe czyli zdefiniowane po literce w wywolaniu funkcji po ** robia sie slownikiem - po nazwie () ale nie opisane w definicji funkcji


connect(a=6, b=8, c=9) #parametry nazwane
# {'a': 6, 'b': 8, 'c': 9}
# przy takiej konstrukcji wszytskie parametry przekazywane do funkcji zostana zamienione na pary klucz:wartosc w slowniku

connect()
connect(name='Radek')

connect_all(1,2)
# (1, 2)
# {}

connect_all(1,2, a=8)
# (1, 2)
# {'a': 8}

connect(a=9)
# {'a': 9}
