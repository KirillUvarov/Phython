# 3- Создайте программу для игры в ""Крестики-нолики"". 
# Для определения победы вам может пригодиться функция filter. 
# Проверяйте победу после каждого хода, фильтруя столбцы, строки 
# и диагонали по знаку хода

print('ПОЛЕ:')

# Задаём строки
enter = '\n'
line_1 = '0 | 1 | 2'
line_2 = '3 | 4 | 5'
line_3 = '6 | 7 | 8'
line_4 = '---------'

# Определяем символы, на которые будут заменены значения под индексами
mark_1 = 'X'
mark_2 = 'O'

#Печатаем заданные строки
def pole (line_1, line_2, line_3, line_4):
    return print(enter, line_1 + enter, line_4 + enter, line_2 + enter, line_4 + enter, line_3 + enter)

pole (line_1, line_2, line_3, line_4)

# Переводим заданные строки в списки
def str_to_list(str):
    list_str = str.split(' | ')
    new_list = [i for i in list_str]
    return new_list

i_1 = str_to_list(line_1)
i_2 = str_to_list(line_2)
i_3 = str_to_list(line_3)

    lsi_1.insert(0, " | ")
    lst.insert(1, " | ")

print(str_to_list(line_1))
print(str_to_list(line_2))
print(str_to_list(line_3))

# Переводим списки в строки
# def list_to_string(lst):
#     lst.insert(0, " | ")
#     lst.insert(1, " | ")
#     str = ''.join(lst)
#     return str

# k = [1, 2, 3]
# l = list_to_string(k)
# print(l)


exit()

print(list_to_string(str_to_list(line_1)))
print(list_to_string(str_to_list(line_2)))
print(list_to_string(str_to_list(line_3)))

# print(i_1)
# print(i_2)
# print(i_3)

# i_1[1] = mark_2
# i_1[0] = mark_1
# i_2[1] = mark_2


# print(list_to_string(i_1))
# print(list_to_string(line_4))
# print(list_to_string(line_2))
# print(list_to_string(line_4))
# print(list_to_string(line_3))


i_11 = list_to_string(i_1)
i_22 = list_to_string(i_2)
i_33 = list_to_string(i_3)

# print(i_1[0],

# )

def new_pole():
    pole(i_11, i_22, i_33, line_4)

new_pole()

exit()



# exit()



# print(str_to_list(line_1))
# print(str_to_list(line_2))
# print(str_to_list(line_3))



# i = input(f'Введите номер поля для отметки {mark_1}: ')
# j = input(f'Введите номер поля для отметки {mark_2}: ')





# exit()

print()





i = input(f'Введите номер поля для отметки {mark_1}: ')
i_1[i] = mark_1

print(list_to_string(i_1))
print(line_4)
print(list_to_string(i_2))
print(line_4)
print(list_to_string(i_3))

exit()

count = 9
while count >= 0:
    if count%2 != 0:
        i = input(f'Введите номер поля для отметки {mark_1}: ')
        if i in range(0, 4):
            i_1[i] = mark_1
            count-=1
            print(list_to_string(i_1))
            print(line_4)
            print(list_to_string(i_2))
            print(line_4)
            print(list_to_string(i_3))
        else:
            i_1[i] = mark_2
            count-=1
            print(list_to_string(i_1))
            print(line_4)
            print(list_to_string(i_2))
            print(line_4)
            print(list_to_string(i_3))

print()

# def print_new_pole():
#     pole(i_11, i_22, i_33, line_4, enter)

# print_new_pole()








# print(pole (line_1, line_2, line_3, line_4, enter))

# count = 0

# while count < 9:
#     i = input(f'Введите номер поля для отметки {mark_1}')





# player_1 = []
# player_2 = []

# while lol > 0:
#         if count == 0:
#             if lol > 0:    
#                 x = (int(input(f'ИГРОК {the_lot_1}, возьмите со стола от 1 до 28 конфет: ')))
#                 if x in range(1, 29): 
#                     if x <= lol: 
#                         lol = lol - x
#                         print(f'Конфет осталось: {lol}')
#                         count +=1
#                     else: 
#                         print(f'На столе {lol} конфет. Попробуй ещё раз!')
#                 else: print('Больше 28 конфет брать нельзя!')
#             else:
#                 print(f'Конфеты кончились(((')


#         if count == 1:
#             if lol > 0:
#                 x = (int(input(f'ИГРОК {the_lot_2}, возьмите со стола от 1 до 28 конфет: ')))
#                 if x in range(1, 29): 
#                     if x <= lol: 
#                         lol = lol - x
#                         print(f'Конфет осталось: {lol}')
#                         count -=1
#                     else: 
#                         print(f'На столе {lol} конфет. Попробуй ещё раз!')
#                 else: print('Больше 28 конфет брать нельзя!')
#             else:
#                 print(f'Конфеты кончились(((')
