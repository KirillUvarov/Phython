# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

from random import randint 
n = int(input('Введите число: '))
list_n = [randint(-100,100) for x in range(n)]
print(list_n)
print('=>')
i=0 
while i < len(list_n):
    if list_n[i] < 0:
        list_n.insert(i+1, 0)
        i+=1
    else:
        i+=1
print(list_n)