# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring
# (Дополнительно для навыков работы со словарями)

# Fn = Fn-1 + Fn-2
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list_1 = []

num = int(input('Введите число для вывода ряда фибоначи: '))

for e in range(1, num+1):
    list_1.append(fib(e))
print(list_1)

# F−1 = 1
# F−2 = -1
# Fn = F(n+2)−F(n+1)

list_2 = list_1[::-1]
list_2.insert(len(list_2), 0)
list_3 = []

i=0 
while i<len(list_2):
    if i%2 != 0:
        list_3.append(list_2[i])
    else:
        list_3.append(list_2[i]*-1)
    i+=1
    
print(list_3 +list_1)
