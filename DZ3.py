# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения
#  n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# a1 = int(input('Введите значение первого элемента: '))
# d = int(input('Введите разность: '))
# n = int(input('Введите количесво элементов: '))
# for i in range(n):
#     print(a1 + i * d, end=' ')

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

import random

count = int(input('Введите кол-во элементов: '))
list_1 = []
for _ in range(count):
    number = random.randint(-20, 20)
    list_1.append(number)
print(list_1)

list_2 = []
max = int(input('Введите максимум: '))
min = int(input('Введите минимумм: '))

for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        list_2.append(i)
print(list_2)