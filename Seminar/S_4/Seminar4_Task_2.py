# 2. Задайте два числа. Напишите программу, которая найдет 
# НОК (наименьшее общее кратное) этих двух чисел. 
# НОК - наименьшее общее кратное, которое делится и на первое, 
# и на второе число.

import math

data = list(map(int, input().split()))

gcd = math.gcd(*data)
lcm = math.lcm(*data)

print(gcd, lcm)

def nok(a, b):
    if a > b:
        largest = a
    else:
        largest = b
    while True:
        if largest % a == largest % b == 0:
            nok_res = largest
            break
        largest += 1
    return nok_res


a, b = int(input('Type value for first number: ')), \
       int(input('Type value for second number: '))
print(nok(a, b))
