#bank = int(input ('Сколько денег на счету? '))
#if bank >= 75000:
#    bank -= 75000
#    print ("Курс успешно приобретен")
#    if bank < 5000:
#        bank += 1000
#        print ('Сделана скидка')
#else:
#    print ('Не хватает денег')
#print (bank)

#Задача 1. Координаты
x = int(input("Введите икс: "))
y = int(input("Введите игрек: "))

if x == y:
    print("X равен Y")
if x > y:
    print("X больше Y")
if x < y:
    print("X меньше Y")

#Задача 3. Маша пошла за сыром
x = int(input ('введите сколько денег: '))
s = 60
m = 20
sum = s + m
if x >= s:
    print ('на сыр денег хватило')
    if x >= sum:
        print ('и на мороженое тоже')
    else:
        print ('Денег маловато')
else:
        print ('Денег не хватило даже на сыр')