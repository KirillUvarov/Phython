# 4- Шифр Цезаря - это способ шифрования, где каждая буква 
# смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

cyrillic = [chr(i) for i in range(ord('а'), ord('я') + 1)] # print(cyrillic)  # ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
cyrillic_str = ''.join(cyrillic) 
# print(cyrillic_str)  # 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
cyrillic_str_up = cyrillic_str.upper()
# print(cyrillic_str_up)
cyrillic_mix_up = (cyrillic_str + cyrillic_str_up)
# print(cyrillic_mix_up)


text = 'Пора вставать... Ресниц не вскинуть сонных. Пора вставать... Будильник сам не свой. В окно глядит и сетует подсолнух, покачивая рыжей головой.'

def crypt(txt):
    output = ''
    message = txt
    key = int(input('Введите числовой ключ шифрования: '))
    for letter in message:
        if letter in cyrillic_mix_up:
            t = cyrillic_mix_up.find(letter)
            new_key = (t + key) % len(cyrillic_str)
            output += cyrillic_mix_up[new_key]
        else:
            output += letter
    # print(txt)
    with open('D:/Google Disk/Личное/GeekBrains/12. Знакомство с языком Python (лекции)/2. Семинар_1/Python/GB/Seminar/S_4/Homework_S4/key.txt', 'w', encoding = 'UTF-8') as key_data:
        key_data.write(f'{key}\n') #Записываем ключ в файл
        key_data.close
    return output

# print(crypt(text))

# Записываем текст в файл
with open('D:/Google Disk/Личное/GeekBrains/12. Знакомство с языком Python (лекции)/2. Семинар_1/Python/GB/Seminar/S_4/Homework_S4/TEXT_1.txt', 'w', encoding = 'UTF-8') as data:
    data.write(f'{text}\n')
    data.close

# Записываем алфавит в файл
with open('D:/Google Disk/Личное/GeekBrains/12. Знакомство с языком Python (лекции)/2. Семинар_1/Python/GB/Seminar/S_4/Homework_S4/ALPHABET_CYRILL.txt', 'w', encoding = 'UTF-8') as data_2:
    data_2.write(f'{cyrillic_mix_up}\n')
    data_2.close

# Записываем зашифрованный текст в файл
with open('D:/Google Disk/Личное/GeekBrains/12. Знакомство с языком Python (лекции)/2. Семинар_1/Python/GB/Seminar/S_4/Homework_S4/TEXT_2.txt', 'w', encoding = 'UTF-8') as data_3:
    data_3.write(f'{crypt(text)}\n')
    data_3.close

path ='D:/Google Disk/Личное/GeekBrains/12. Знакомство с языком Python (лекции)/2. Семинар_1/Python/GB/Seminar/S_4/Homework_S4/'
file = 'TEXT_2.txt'
path_file = (path+file)
# print(path_file)

open_t2 = open(path_file, encoding='utf-8')
# print(open_t2.read())


# exit() # После этой команды остальной код не запускается

file_key = 'key.txt'
path_file_2 = (path + file_key)

# Выводим ключ
# data_9 = open(path_file_2, 'r')
# for line in data_9:
#     # print(open_t2.read())
#     open_t2.read()
# data_9.close()

open_t3 = open(path_file_2, encoding='utf-8')
read_key = open_t3.read()
# print(type(read_key))
key_int = int(read_key)

# print(read_key) #Выводим ключ

file_crypt = 'TEXT_2.txt'
path_file_3 = (path + file_crypt)

# Выводим зашифрованный текст
open_t4 = open(path_file_3, encoding='utf-8')
data_110 = open(path_file_3, 'r')
for line in data_110:
    # print(open_t4.read())
    txt_2 = open_t4.read()
    # print(type(open_t4.read()))
data_110.close()


def decrypt(txt, key):
    output = ''
    message = txt
    key *= -1
    for letter in message:
        if letter in cyrillic_mix_up:
            t = cyrillic_mix_up.find(letter)
            new_key = (t + key) % len(cyrillic_str)
            output += cyrillic_mix_up[new_key]
        else:
            output += letter
    return output

txt_3 = decrypt(txt_2, key_int)
# print(f'дешифровано: {txt_3}')

# print(decrypt('жезч щийчщчйу... зьидян дь щибядкйу иеддтм. жезч щийчщчйу... шкыявудяб ичг дь ищеа. щ ебде ъвцыяй я иьйкьй жеыиевдкм, жебчоящчц зтэьа ъевещеа.', 23))

# exit()
# print(decrypt(open_t4.read(), read_key))
# exit()
# decr = decrypt((open_t2.read()), read_key)
# print(decr)

# Создаём новый файл и записываем расшифрованный текст
file_decrypt = 'TEXT_3.txt'
path_file_4 = (path + file_decrypt)
# print(open_t2.read())

# exit()

# Записываем расшифрованный текст в файл
with open(path_file_4, 'w', encoding = 'UTF-8') as data_90:
    data_90.write(txt_3)
    # data_90.write(decrypt(open_t4.read()), read_key)
    data_90.close
