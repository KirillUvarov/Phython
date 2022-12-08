# 1 - Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

# def simple(n):
#    i = 2
#    simp = []
#    while i * i <= n:
#        for i in range(2, n):
#             if not (n % i):
#                 simp.append(i)
#                 n = n / i
#        i = i + 1
# #    if n > 1:
# #        simp.append(n)
#    return simp

# print(simple(int(input('Введите число: '))))
# теорема вильсона

# from fun
# a = "03523"
# a.isdigit()
# True
# b = "963spam"
# b.isdigit()
# False

# def is_numeric(n) -> bool:
#     return n.isdigit()

# print(is_numeric('50'))

   
# def is_simple(n: int) -> bool:
#     for i in range(2, n):
#         if not (n % i):
#             return False
#     return True

# x = int(input('Введите: '))
# print(is_simple(x))

# n = abs(is_numeric(input('Введите число: ')))
# fst_simple = [i for i in range(2, n + 1) if not n%i and is_simple(i)]
# print(fst_simple)

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1

# print(f"Простые множители числа {old} приведены в списке: {lst}")
# 
import math 

# def prime_factors(num): 
#     list_1 = []
#     while num % 2 == 0: 
#         print(2,) 
#         num = num / 2 
#     for i in range(3, int(math.sqrt(num)) + 1, 2): 
#         while num % i == 0: 
#             print(i,) 
#             num = num / i 
#     if num > 2: 
#         print(num) 
  
 
# n = input('Введите число: ') 
# prime_factors(n) 

# list_1 = []
# n = int(input('Введите число: '))
# for i in range(2, n):
#     if 
#     list_1.append(i)
# print(list_1)

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac

n = input('Введите: ')
primfacs(n)

print(n)