# Задача №1: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр(отсекаем минус, считаем все в плюс).

# Пример:
# 67,82 -> 23
# 0,56 -> 11

# material_num = input('Введите вещественное число: ')
# print(type(material_num))
# sum = 0
# for i in material_num:
#     if i != '.':
#         sum += int(i)
# print(sum)

# Задача №2: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

# n = int(input("Введите число: "))
# factorial = 1
# for i in range(1,n+1):
#     factorial = factorial*i
# print(factorial)

# Задача №3: Реализуйте случайное перемешивания списка.

# *Пример:
# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True '] Результат -> [250, 3.14, 'True ', 'Веселый пианист']

# list = ['Веселый пианист', 250, 3.14, 'True ']
# print(list) 
# import random
# random.shuffle(list)
# print('->', list) 