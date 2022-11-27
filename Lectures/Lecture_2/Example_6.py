# Множества

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# # exit() # код ниже не выполняется
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray') # добавляем в множество новую переменную
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # удаляем переменную из множества
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } # очищаем все переменные
# print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8} # копируем из множества a все переменые
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} #объединяем два множества приэтом совпадающие значения не дублируются
i = a.intersection(b) # i = {8, 2, 5} # пересечение
dl = a.difference(b) # dl = {1, 3} # 
dr = b.difference(a) # dr = {13, 21} #
q = a \
.union(b) \
.difference(a.intersection(b))
# {1, 21, 3, 13}

# b = frozenset(a) #неизменяемое множество (замороженное)
# print(b) # frozenset({1, 2, 3, 5, 8})