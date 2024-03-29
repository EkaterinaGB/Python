#  Задача №1: Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141

# import math

# d = input('Введите степень округления в формате 0.01 и т.д: ')
# d = d[2:len(d)]
# print(round(math.pi,len(d)))

# Задача №2: Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

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

# Задача №3: Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

# my_list = [1, 1, 2, 3, 4, 4, 4]

# # так
# result_list = []
# for i in my_list:
#     if my_list.count(i) == 1:
#         result_list.append(i)
# print(result_list)

# или так
# print([i for i in my_list if my_list.count(i) == 1])

# Задача №4: Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

# import random

# def write_file(st):
#     with open('file33.txt', 'w') as data:
#         data.write(st)


# def rnd():
#     return random.randint(0,101)


# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    

# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))

# Задача №5: Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

# import random

# # запись в файл
# def write_file(name,st):
#     with open(name, 'w') as data:
#         data.write(st)

# # создание случайного числа от 0 до 100
# def rnd():
#     return random.randint(0,101)

# # создание коэффициентов многочлена
# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    
# # создание многочлена в виде строки 
# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0 or lst[i+2] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# # получение степени многочлена
# def sq_mn(k):
#     if 'x^' in k:
#         i = k.find('^')
#         num = int(k[i+1:])
#     elif ('x' in k) and ('^' not in k):
#         num = 1
#     else:
#         num = -1
#     return num

# # получение коэффицента члена многочлена
# def k_mn(k):
#     if 'x' in k:
#         i = k.find('x')
#         num = int(k[:i])
#     return num

# # разбор многочлена и получение его коэффициентов
# def calc_mn(st):
#     st = st[0].replace(' ', '').split('=')
#     st = st[0].split('+')
#     lst = []
#     l = len(st)
#     k = 0
#     if sq_mn(st[-1]) == -1:
#         lst.append(int(st[-1]))
#         l -= 1
#         k = 1
#     i = 1 # степень
#     ii = l-1 # индекс
#     while ii >= 0:
#         if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
#             lst.append(k_mn(st[ii]))
#             ii -= 1
#             i += 1
#         else:
#             lst.append(0)
#             i += 1
        
#     return lst

# # создание двух файлов

# k1 = int(input("Введите натуральную степень для первого файла k = "))
# k2 = int(input("Введите натуральную степень для второго файла k = "))
# koef1 = create_mn(k1)
# koef2 = create_mn(k2)
# write_file("file34_1.txt", create_str(koef1))
# write_file("file34_2.txt", create_str(koef2))

# # нахождение суммы многочлена

# with open('file34_1.txt', 'r') as data:
#     st1 = data.readlines()
# with open('file34_2.txt', 'r') as data:
#     st2 = data.readlines()
# print(f"Первый многочлен {st1}")
# print(f"Второй многочлен {st2}")
# lst1 = calc_mn(st1)
# lst2 = calc_mn(st2)
# ll = len(lst1)
# if len(lst1) > len(lst2):
#     ll = len(lst2)
# lst_new = [lst1[i] + lst2[i] for i in range(ll)]
# if len(lst1) > len(lst2):
#     mm = len(lst1)
#     for i in range(ll,mm):
#         lst_new.append(lst1[i])
# else:
#     mm = len(lst2)
#     for i in range(ll,mm):
#         lst_new.append(lst2[i])
# write_file("file34_res.txt", create_str(lst_new))
# with open('file34_res.txt', 'r') as data:
#     st3 = data.readlines()
# print(f"Результирующий многочлен {st3}")