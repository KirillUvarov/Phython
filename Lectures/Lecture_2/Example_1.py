
# a – Откроет для добавления нового содержимого. Создаст новый файл для записи, если не найдет с указанным именем.
# r – Только для записи. Создаст новый файл, если не найдет с указанным именем.
# w – открытие для записи данных (перезапись)
# rb	Только для чтения (бинарный).
# wb	Только для записи (бинарный). Создаст новый файл, если не найдет с указанным именем.
# r+	Для чтения и записи.
# rb+	Для чтения и записи (бинарный).
# w+	Для чтения и записи. Создаст новый файл для записи, если не найдет с указанным именем.
# wb+	Для чтения и записи (бинарный). Создаст новый файл для записи, если не найдет с указанным именем.
# a+	Откроет для добавления нового содержимого. Создаст новый файл для чтения записи, если не найдет с указанным именем.
# ab	Откроет для добавления нового содержимого (бинарный). Создаст новый файл для записи, если не найдет с указанным именем.
# ab+	Откроет для добавления нового содержимого (бинарный). Создаст новый файл для чтения записи, если не найдет с указанным именем.
# w+, r+

# Записываем текст в файл
# colors = ['red', ' ', 'green', ' ', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close() #закрыли подключение к файлу

with open('D:/Google Disk/Личное/GeekBrains/12. Знакомство с языком Python (лекции)/2. Семинар_1/Python/GB/Lectures/Lecture_2/file_N.txt', 'w') as data:
    data.write('line 444 \n')
    data.write('line 333 \n')


# Выводим на консоль текст из файла
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
data.close()
# exit()