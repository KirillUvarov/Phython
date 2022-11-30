# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# # Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint 
# n = int(input('Введите число: '))
# list_n = [randint(1,10) for x in range(n)]
# print(list_n)
# print('=>')
# i = 0
# j = len(list_n)
# multi = 0
# print(list_n[j])
# print(list_n[i])
# while i < len(list_n)/2:
#     multi = list_n[i] * list_n[j]
#     i += 1
#     j -= 1
#     print(multi)

# multi = list_n[i] * list_n[j]
# i += 1
# j -= 1
# print(multi)

from random import randint


number = int(input('Введите размер списка '))
list_1 = []
list_2 = []

for i in range(number):
    list_1.append(randint(1, 10))

for i in range(len(list_1)):
    while i < len(list_1)/2 and number > len(list_1)/2:
        number = number - 1
        a = list_1[i] * list_1[number]
        list_2.append(a)
        i += 1

print(list_1)
print('=>')
print(list_2)