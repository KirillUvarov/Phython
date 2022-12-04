# 2 - Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

data = list(map(int, input('Введите числа: ').split())) #Вводим список со значениями списка
print(data) # Выводим список ['4', '3', '2']
data_2 = data
# print(data_2)

data_3 = []
i = 0
j = 0

# for i in data:
#     if i not in data_3:
#         data_3.append(i)

# print(data_3)

# for i in data:
#     if i != i+1:
#         for j in data_2:
#             if j == j+1:
#                 j+=1
#             else:
#                 data_3.append(j)
#     i+=1
# print(data_3)

if data[0] != data_2[i]:
    data_3.append(i)
#     i+=1
# if data[0] != data_2[i]:
#     i+=1
#     data_3.append(i)

# for i in data:
#     for j in data_2:
#         if i > j:
#             data_3.append(i)
#             j+=1
#         elif i < j:
#             data_3.append(j)
#             j+=1
#         else:
#             i+=1

            
            

print(data_3)