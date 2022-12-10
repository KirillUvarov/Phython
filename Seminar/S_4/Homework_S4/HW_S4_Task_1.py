# 1 - Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def is_prime(a): # Проверка на простое число
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

def simple_list_for(s): # Создание листа из простых чисел до s
    list_s =[]
    for i in range(2, s+1):
        if is_prime(i) == True: 
            list_s.append(i)
    return list_s

m = int(input("Введите число: "))
list_1 = simple_list_for(m)
list_2 =[]


for i in range(0, len(list_1)):
    if m % list_1[i] == 0:
        list_2.append(list_1[i])

print(list_2)