# 3 - В файле, содержащем фамилии студентов и их оценки, изменить 
# на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

# path = 'D:/Google Disk/Личное/GeekBrains/12. Знакомство с языком Python (лекции)/2. Семинар_1/Python/GB/Seminar/S_4/Homework_S4/file_HW1.txt'


# dictionary = \
#     {
#         'Angela Merkel': 5,
#         'Enakin Skywalker': 5,
#         'Freddie Mercury': 3,
#         'Alexander Pushkin': 4,
#     }

# with open(path, 'w') as data:
#     for key, value in dictionary.items(): 
#         data.write('%s:%s\n' % (key, value))

# if value == 5:

# Выводим на консоль текст из файла
# path = 'file_HW1.txt'
# data = open(path, 'r+')
# for line in data:
#     print(line)
# data.close()
# exit()

#.upper
