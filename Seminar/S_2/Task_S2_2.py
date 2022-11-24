# ; 2. Напишите программу, в которой пользователь будет
# ; задавать две строки, а программа - определять количество
# ; вхождений одной строки в другой.

# string_1 = input()
# string_2 = input()
# result = string_1.count(string_2)
# print(result)

# a = list(input())
# b = list(input())
# cnt = 0
# for i in range(len(a)):
#     if a[i] == b[0]:
#         for j in range(len(b)):
#             if a[i+j] != b[j]:
#                 break
#         cnt += 1
# print(cnt)


# import random
# string_1 = (input('Введите ткст 1: '))
# string_2 = (input('Введите ткст 2: '))
# num = 0

# for i in range(len(string_1) - len(string_2)+1):
#     if string_1[i::+len(string_2)] == string_2:
#         swich
#         for j in range(len(string_2)):
#             if string_1[i] == string_1[j]:
#                 num += 1
#                 j += 1
#             else:
#                 j += 1
#     i += 1
# print(num)


# for i in range(len(string_1) - len(string_2)+1):
#     if string_1[i::+len(string_2)] == string_2:
#         num+=1

# print(num)

# word = 'python'
# print(word[2:])
# print(word[:2])
# print(word[1:3])
# # thon
# # py
# # yt


a = list(input())
b = list(input())
cnt = 0
for i in range(len(a)-len(b)+1):
    if a[i] == b[0]:
        switch=True
        for j in range(len(b)):
            if a[i+j] != b[j]:
                switch=False
                break
        if switch:
            cnt += 1
print(cnt)
