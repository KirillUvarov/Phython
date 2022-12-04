# 1 - Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def simple(n):
   i = 2
   simp = []
   while i * i <= n:
       while n % i == 0:
           simp.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       simp.append(n)
   return simp

print(simple(int(input('Введите число: '))))