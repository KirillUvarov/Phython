# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring
# (Дополнительно для навыков работы со словарями)

# Fn = Fn-1 + Fn-2
def fibonachi(num):
    # num = int(input('Введите число: '))
    fib_1 = 1
    fib_2 = 1
    i =0
    while i < num - 2:
        fiboch = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fiboch
        i += 1
    return fiboch
num = int(input('Введите число: '))
print(fibonachi(num))

# for febonach in range(1, num):
#     feboch = num-1 + num-2
#     print(feboch)

# num = int(input('Введите число в десятичной системе: '))
# list_1 = []
# list_1.append(febonach(num))
# print(list_1)


