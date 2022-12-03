# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных (перезапись)
# w+, r+

# Записываем текст в файл
# colors = ['red', ' ', 'green', ' ', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close() #закрыли подключение к файлу

with open('file.txt', 'w') as data:
    data.write('line 444 \n')
    data.write('line 333 \n')


# Выводим на консоль текст из файла
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
exit()