#Задача 1. Яблоки
apples = 41
boxes = 3
full_boxes = apples / boxes
print('Кол-во полных ящиков:', full_boxes)

full_boxes = apples // boxes
print('Кол-во полных ящиков:', full_boxes)

rest_apples = apples % boxes
print('Осталось яблок:', rest_apples)

#Задача 2. Последняя цифра
digital = int (input ('введите число: '))
print ('Номер дома:', digital // 100)
print ('Номер квартиры:', digital % 100)