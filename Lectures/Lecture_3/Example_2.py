# list = []

# for i in range(1, 101): #добавляем в список чётные числа от 1 до 100 по порядку
#     # if(i%2 == 0):
#         list.append(i);

# print(list)


# list = [(i, i) for i in range (1, 21) if i % 2 == 0] # Делает то же самое
# print(list)

def f(x):
    return x**3

list = [(i, f(i)) for i in range (1, 21) if i % 2 == 0] # Задаём катежи, с указанием чисел и их кубов
print(list)
