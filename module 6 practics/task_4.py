print('Задача 4. Вклады')
#Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, после чего дробная часть копеек отбрасывается. Определите, через сколько лет вклад составит не менее Y рублей.
#
#Что нужно сделать
#Напишите программу, которая по данным числам X, Y, P определяет, сколько лет пройдёт, прежде чем сумма достигнет значения Y.
contribution = int ( input ('Вклад в банке: '))
percent = int ( input ('Проценты: '))
contribution_threshold = int ( input ('Порог вклада: '))
year = 0
while contribution <= contribution_threshold:
    total = contribution * (1 + percent/ 100 )
    year += 1
    print (year,'год.',contribution,'+',percent,'% = ', total)
    contribution = total
print ('Кол-во лет для достижения порога:', year)
