# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

list_1 = list(map(float, input("Введите вещественные числа, используя пробел как разделитель:\n").split()))
list_2 = [ round (i%1,2) 
    for i in list_1 
        if i%1 != 0]

print(max(list_2) - min(list_2))