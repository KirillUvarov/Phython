# f(x) ⇒ x - чётное
# print(filter(f, [ 1, 2, 3, 4,5]))
# ↓
# [ 2, 4 ]

data = [x for x in range(10)] # Задаём список с числами от 0 до 9
print(data)
res = list(filter(lambda x: not x%2 == 0, data)) #Фильтруем т определяем, что числа списка будут только нечётные 
print(res)
