# Задача: предложить улучшения кода для уже решённых задач (3-5 задача):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 1)Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n = input('Введите вещественное число: ')
# sum = sum(map(int, n.replace('.', '')))
# print (sum)

# 2)Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# from math import factorial
# n = int(input('Введите число: '))
# print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,n+1)))))

# 3)Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# import math
# list_a = list(map(int, input('Введите числа, через пробел: ').split()))
# print('Исходный список: ',list_a)
# print('Результат: ',list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))

# 4)Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# from functools import reduce
# dot_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
# dot_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
# def dot_range(dot_1, dot_2):
#      rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
#      return round(rng, 2)
# print(dot_range(dot_1, dot_2))

# 5)Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# my_list = list(map(int, input('Введите числа, через пробел: ').split()))
# print(sum(my_list[1::2]))