# # Напишите программу вычисления арифметического выражения заданного строкой. 
# # Используйте операции +,-,/,*. приоритет операций стандартный. 
# #     *Пример:* 
# #     2+2 => 4; 
# #     1+2*3 => 7; 
# #     1-2*3 => -5
# #     - Добавьте возможность использования скобок, меняющих приоритет операций.
# #         *Пример:* 
# #         1+2*3 => 7; 
# #         (1+2)*3 => 9;

# # def sum_1(x):


# # def dif_1():

# # def mult_1():

# # def dev_1():

# # list_1 = [input('Введите выражение : ').replace(' ', '')]

# # list_2 = ['+', '-', '/', '*']

# # for i in range(0, len(list_1)):
# #     ind = min( list_1.find('/'), list_1.find('*'))
# #     if ind != -1:
# #         for i in range()


# # 10+(2+2)-1
# # 10+(10/(22*5))+4

# import re

# list_1 = ('2 * 2 / 2 + 2').split()
# list_2 = [* / + -]
# list_3 = [2 5 6 ]
# print(list_1)
# for i in range(0, len(list_1)):
#     if i == '*' or '/':
#         list_2.append(list_1[i])
#         list_1[i-1]





# # list_1 = ['2', '2', '1']
# # list_2 = [+, -]

num1 = input("First Number:\n")
operator = input("Operator (+, -, *, /):\n")
num2 = input("Second Number:\n")

num1 = float(num1)
num2 = float(num2)

out = None

if operator == "+":
    out =  num1 + num2
elif operator == "-":
    out = num1 - num2
elif operator == "*":
    out = num1 * num2
elif operator == "/":
    out = num1 / num2
    
print("Answer: " + str(out))

# ___________________
#  Напишите программу вычисления арифметического выражения заданного строкой.
# # Используйте операции +,-,/,*. приоритет операций стандартный.


# def priority(data, arg1, arg2):
#     for i in range(len(data)):
#         try:
#             ind1 = data.index(arg1)
#         except ValueError:
#             ind1 = -1
#         try:
#             ind2 = data.index(arg2)
#         except ValueError:
#             ind2 = -1
#         min_ind = min(ind1, ind2)
#         max_ind = max(ind1, ind2)
#         if min_ind != -1:
#             data[min_ind - 1] = op(data[min_ind], data[min_ind - 1], data[min_ind + 1])
#             data.pop(min_ind)
#             data.pop(min_ind)
#         elif min_ind == -1 and max_ind != -1:
#             data[max_ind - 1] = op(data[max_ind], data[max_ind - 1], data[max_ind + 1])
#             data.pop(max_ind)
#             data.pop(max_ind)
#         elif min_ind == max_ind == -1:
#             break
#     return data


# def op(oper: str, arg1: str, arg2: str):
#     if oper == '*':
#         return int(arg1) * int(arg2)
#     elif oper == '/':
#         return int(arg1) / int(arg2)
#     elif oper == '+':
#         return int(arg1) + int(arg2)
#     elif oper == '-':
#         return int(arg1) - int(arg2)


# lst = input().split()
# lst = priority(lst, '/', '*')
# print(lst)
# lst = priority(lst, '-', '+')
# print(f'Result = {lst[0]}')