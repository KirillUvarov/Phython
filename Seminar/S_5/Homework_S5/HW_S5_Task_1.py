# Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

str_1 = 'Пугать ты галок пугай'
rem = 'пугай'

def del_str(str, remove_txt):
    list_str = str.split()
    new_list = [wrd for wrd in list_str if wrd not in remove_txt]
    new_str = ' '.join(new_list)
    return new_str

print(str_1)
print(rem)
print(del_str(str_1, rem))
