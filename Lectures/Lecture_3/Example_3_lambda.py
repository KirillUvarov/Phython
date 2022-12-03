# path = 'D:/Google Disk/Личное/GeekBrains/12. Знакомство с языком Python (лекции)/2. Семинар_1/Python/GB/Lectures/Lecture_3/Example_3.py/file.txt'
# f = open(path, 'a')
# data = f.read() + ' '
# f.close()

# numbers = []
# while data != '':
#     space_pos = data.index(' ')
# numbers.append(int(data[:space_pos]))
# data = data[space_pos+1:]
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e **2))
# print(out)

# def select(f, col): #Функция принимает функцию и набор данных
#     return [f(x) for x in col] #Принимаетсписок и сразу его возвращает

# def where(f, col): #
#     return [x for x in col if f(x)] #Возвращает список

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int ,data)
# res = where(lambda x: not x%2, res) 
# res = select(lambda x: (x, x**2), res)
# print(res)

# Точно так же работает встроенная функция map

li = [x for x in range(1, 21)]

li = list(map(lambda x:x+10, li)) # Преобразуем в список

print(li)