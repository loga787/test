#a = input ('введите a: ')
#b = input ('введите b: ')
#print (a + b)

#a = int(input ('введите a: '))
#b = int(input ('введите b: '))
#print (a + b)

a = '12'
b = '34'
c = int(a + b) * 2
print (c)
print (int(a + b) * 2)

#Задача 1. Координаты точки
a = int(input ('введите a: '))
b = int(input ('введите b: '))
print ('Сумма:', a + b)

#Задача 2. Отрезок
c = int(input ('введите c: '))
d = int(input ('введите d: '))
print ('Ответ:', 2 * ( c + 5 + (a * b ) / (4 * b)) * (d - 2 * (a **3 / 30)) - 10)

#Задача 3. Исправление ошибки
a = '2'
b = '5'
c = '3'
num = 6 ** int(a) + (7 - int(b)) * int(c)
print(num)