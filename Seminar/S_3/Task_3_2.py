# 2. Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def input_method():
    num = ""
    while not num.isdigit():
        num = input('Enter value: ')
        if num.isdigit():
            num = int(num)
            return num
        elif num == -1:
            exit('Bye-bye')
        else:
            print('Value is incorrect\nIf you want to exit the program then type "-1"')


def func_n(number):
    number = 3 * number + 1
    return number


length = input_method()
dict = {i: func_n(i) for i in range(length + 1)}
print(dict)



# def input_list():
#     data = input('Введите значения в списке через пробел:\n').split(" ")
#     return data


# def find_value(data_list):
#     what_find = input('Кого ищем то?\n')
#     count = 0
#     for i in range(len(data_list)):
#         if what_find in data_list[i]:
#             count += 1
#             if count == 2:
#                 return f'Индекс второго вхождения - {i}, а позиция - {i + 1}'
#     else:
#         return '2 раз не приходило, а может и первого раза не было, мы не в курсе'


# elements = input_list()
# result = find_value(elements)
# print(result)
