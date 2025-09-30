#Задача 1. Сравнение веса грузов
#a = int(input ('введите вес 1 груза: '))
#b = int(input ('введите вес 2 груза: '))
#if a < b:#
#    print ('Первый груз легче второго')
#elif a == b:
#    print ('Оба груза весят одинаково')
#else:
#    print ('Первый груз тяжелее второго')

#Задача 2. Прогрессивный налог
#profit = int(input ('введите доход: '))
#if profit < 10000:
#    tax = profit * 13 / 100
#    print ('Размер налога (13%) равен:', tax)
#elif profit < 50000:
#     tax = profit * 20 / 100
#     print ('Размер налога (20%) равен:', tax)
#else:
#     tax = profit * 30 / 100
#     print ('Размер налога (30%) равен:', tax)

#Задача 3. Фальшивомонетчики
first = int(input("Введите вес 1й монетки: "))
second = int(input("Введите вес 2й монетки: "))
third = int(input("Введите вес 3й монетки: "))

if first == second:
    print("Третья легче")
elif first < second:
    print("Первая легче")
else:
    print("Вторая легче")