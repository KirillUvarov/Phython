# 2 - Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

list_1 = list(map(int, input("Введите числа через пробел:").split()))
# print(list_1)
new_list = []
[new_list.append(i) for i in list_1 if i not in new_list]
print(f"Список из неповторяющихся элементов: {new_list}")