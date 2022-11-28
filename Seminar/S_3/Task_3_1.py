# 1. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3

from typing import Optional
list_1 = ['gfh5', 'gfh2', '67', 'jy32', '3put']
print(list_1)
n = int(input('Введите число: '))

for char in (list_1):
    if str(n) in char:
        print(list_1.index(char))
        break
    else:
        break