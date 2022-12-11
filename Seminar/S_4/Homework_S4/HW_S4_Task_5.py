# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия 
# и восстановления данных. Входные и выходные данные 
# хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol


def encode(s):
    encoding = "" # сохраняет выходную строку
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1
    return encoding
 
 
if __name__ == '__main__':
 
    s = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
    print(encode(s))