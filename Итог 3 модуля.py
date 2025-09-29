#Задача 1. Режем число на части
digital = 1234
thousands = digital // 1000
hundreds = digital // 100 % 10
tens = digital // 10 % 10
units = digital % 10
print ('Thousands:', thousands)
print ('Hundreds:', hundreds)
print ('Tents:', tens)
print ('Units:', units)

#Задача 2. Поменять местами
a = int(input ('введите a: '))
b = int(input ('введите b: '))
print(a, b)
b, a = a, b
print (a, b)
