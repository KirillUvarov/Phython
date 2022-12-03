# data = list(map(int, input('Введите числа: ').split())) #Вводим список со значениями списка
# print(data) # Выводим список ['4', '3', '2']
# for  e in data:
#     print(e*12)

# print('____________')

# for  e in data:
#     print(e*10)

# for  e in data:
#     print(e*2)


#Заменяем select из прошлого примера на map 
def where(f, col): #
    return [x for x in col if f(x)] #Возвращает список

data = '1 2 3 5 8 15 23 38'.split()

# res = map(int ,data) #Преобразуем в объект типа map, но пока ещё не список
# res = where(lambda x: not x%2, res) 
# res = list(map(lambda x: (x, x**2), res))
# print(res)

#Альтернативное представление через фильтр


res = map(int ,data) #Преобразуем в объект типа map, но пока ещё не список
res = filter(lambda x: not x%2, res) 
res = list(map(lambda x: (x, x**2), res))
print(res)