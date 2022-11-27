# with open('file.txt', 'w') as data:
# data.write('line 1\n')
# data.write('line 2\n')
colors = ['red', 'green', 'blue']
data = open('file.txt', 'r')
data.writelines(colors) # разделителей не будет
data.close() #закрыли подключение к файлу
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()