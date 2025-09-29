#Задача «Максимальное число»
a = int(input ('введите a: '))
b = int(input ('введите b: '))
c = int(input ('введите c: '))
if a >= b:
    max = a
else:
    max = b
if c >= max:
     max = c
print (max)