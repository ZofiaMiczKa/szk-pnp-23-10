from datetime import date, timedelta, datetime

today = date.today()
print(today) #2023-10-25
print(type(today)) #class datetime date

time = datetime.now() #2
print(time)
print(type(time)) #2023-10-25 09:38:03.738288

#days=0, seconds=0, microseconds=0 miliseconds =0, minutes=0, hours=0, weeks=0

tomm = today + timedelta(days=1)
print(tomm)
print(type(tomm)) #2023-10-26

print(time.hour)
print(today.day)

formated_date = datetime.now().strftime('%d/%m/%Y') # male m miesiac
print(formated_date) #2 5/10/2023

formated_time = datetime.now().strftime('%H:%M')
print(formated_time) # 09:49
print(formated_time.removeprefix('0'))

formated_time2 = datetime.now().strftime('%I:%M %p') # I format amerykanski %p oznacza PM/AM
print(formated_time2) # 09:49
print(formated_time2.removeprefix('0'))

products = [            #lista ktora sie sklada z czterech slownikow
    {'sku':1, 'exp_date':today,'price':100.0},
    {'sku':2, 'exp_date':tomm,'price':80.0},
    {'sku':3, 'exp_date':today,'price':50.0},
    {'sku':4, 'exp_date':today,'price':250.0}
]

#print(products)

for product in products:
    #print(product)
    if product['exp_date'] !=today:   #rozne od today wtedy czyta continue czyli pomija ten element, wykonuje tylko dla today
        continue
    #print(f"{product['exp_date']}:jade dalej")
    product['price'] *= 0.8 # price = price *0.8
    print(f"""
    Price for sku = {product['sku']}
    is now {product['price']}""")

