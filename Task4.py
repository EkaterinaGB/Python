# Задача №1: Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

# n = int(input('Введите число: '))
 
# b = ''
 
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
 
# print(b)

# Задача №2: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))

# Задача №3: Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# string = '48 15 25 7 14 3 58 5'

# def convert_to_int(str):
#     return [int(x) for x in str.split()]

# str_list = convert_to_int(string)
# print(min(str_list), max(str_list))

# Задача №4: Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a, b = 7, 5
i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print(i)