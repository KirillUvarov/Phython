# 1- Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



from random import randint 
n = int(input('Введите количество элементов списка: '))
list_n = [randint(1,10) for x in range(n)]
number = list(enumerate(list_n))
print(number)
print('=>')

i = 0
sum = 0
while i < len(list_n):
    if i%2 == 0:
        # print(f' {list_n[i]}')
        i+=1
    else:
        sum = sum + list_n[i]
        i+=1

print(f'Сумма чисел на нечётных позициях: {sum}')