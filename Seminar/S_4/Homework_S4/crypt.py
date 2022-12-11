# def crypt(txt, s): 
#     result = "" 
#     for i in range(len(txt)): 
#         char = txt[i] 
#         if(char.isupper()): 
#             result += chr((ord(char) + s - 64) % 26 + 65) 
#         else: 
#             result += chr((ord(char) + s - 96) % 26 + 97) 
#     return result 

# txt = "CEASER CIPHER EXAMPLE" 

# # s = 4 
 
# print("Plain txt : " + txt) 
# print("Shift pattern : " + str(s)) 
# print("Cipher: " + crypt(txt, s)) 


# _________________________________________________
# Пора вставать... Ресниц не вскинуть сонных. Пора вставать... Будильник сам не свой. В окно глядит и сетует подсолнух, покачивая рыжей головой

# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# while True:
#     print('Введите Ш чтобы зашифровать сообщение, Р чтобы расшифровать и В чтобы выйти')
#     menu = input('>>> ').lower()
#     if menu == 'в':
#         break
#     elif not (menu == 'ш' or menu == 'р'):
#         continue
#     output = ''
#     message = input('Введите строку: ').lower()
#     key = int(input('Введите ключ: '))
#     if menu == 'р':
#         key *= -1
#     for letter in message:
#         if letter in alphabet:
#             t = alphabet.find(letter)
#             new_key = (t + key) % len(alphabet)
#             output += alphabet[new_key]
#         else:
#             output += letter
#     print('Результат: ' + output)

# path ='D:/Google Disk/Личное/GeekBrains/12. Знакомство с языком Python (лекции)/2. Семинар_1/Python/GB/Seminar/S_4/Homework_S4/'
# file = 'TEXT_2.txt'
# path_file = (path+file)
# print(path_file)

# open_t2 = open(path_file, encoding='utf-8')

# # Выводим на консоль текст из файла
# data_8 = open(path_file, 'r')
# for line in data_8:
#     print(open_t2.read())
# data_8.close()
# exit()