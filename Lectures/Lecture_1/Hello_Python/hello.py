# print("Hello world")
# value = None
# a = 123
# b = 1.23
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# value=12334
# print(type(value))
# s = 'hello world' # \n - переход на следующую строку
# # print(s) #Вывод строки
# print(a, '-', b,  '-', s)
# print('{1} - {2} - {0}'.format(a, b, s)) # 0, 1 и 2 это индексы переменных в скобках
# print(f'{a} - {b} - {s}')

# f = True #Fals
# print(f)
# #В C# были массивы, а в Python - списки:
# list = [1,2,3, 'hello', 1,2,3.4, True]
# print(list)

#Ввод данных
# print('Введите a');
# a = input()
# print('Введите b');
# b = input()
# print(a, '+', b, '=', a+b) #В таком варианте результатом сложения будет два введённых числа без пробелов
# print('{1} - {0}'.format(a, b))
# print(f'{a} - {b}')
  
# print('Введите a');
# a = int(input()) #Присваиваем переменной int(целочисленные) или float(вещественные)
# print('Введите b');
# b = int(input())
# print(a, '+', b, '=', a+b) #В таком варианте результатом сложения будет два введённых числа без пробелов
# print('{1} - {0}'.format(a, b))
# print(f'{a} - {b}')

#Арифметические операции
# +, -, *, /, %, // - деление в целых числах, ** - возведение в степень
# **, 
# a = 1.31346546
# b = 3
# c = round(a * b, 6) #round - округление 6 - знаков после запятой
# print(c)

# a = 3
# a += 5
# print(a) #8

# a = 1 < 4 and 5 > 2
# print(a) #True

# func = 1
# T = 4
# x = 123
# print(func<T<(x))

# f = 1>2 or 4<6
# print(f) #True

# f = [1, 2, 3, 4]
# print(2 in f) #True

# f = [1, 2, 3, 4]
# is_odd = not f[0] % 2 == 0
# print(is_odd)


#Оператор ветвления
# if condition:
#     # operator 1
#     # operator 2
#     # ...
#     # operator n
# else:
#     # operator n+1
#     # operator n+2
#     # ...
#     # operator n+m

# a = int(input('a='))
# b = int(input('b='))
# if a>b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя:')
# if username == 'Маша':
#     print('Ура, это же МАША')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина:)')
# elif username == 'Ильнар':
#     print('Ильнар - топчик!')
# else:
#     print('Привет, ', username)


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
# print(inverted) #Переворачивает число

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)

#Управляющие конструкции

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i) #0 1 2 3 4 5 ... 9

#Строки

# text = 'съешь ещё этих мягких французских булок'
# help(text.istitle)

# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

#Списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
# i *= 2
# print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']
# for e in colors:
# print(e) # red green blue
# for e in colors:
# print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

#Функции
# def function_name(x):
# body line 1
# . . .
# body line n
# optional return

# def f(x):
#     return x**2
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return 
arg = 1
print(f(arg))
print(type(f(arg)))