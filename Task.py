# Задача №1: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# 6 -> да
# 7 -> да
# 1 -> нет

# day = int(input('Введите число соответствующее дню недели: '))
# if day > 7 or day < 1:
#     print('Вы ввели неверные данные,пожалуйста,повторите')
# elif day == 6 or day == 7:
#     print('Урааа,выходной!')
# else:
#     print('Увы,надо работать(')

# Задача №2: Напишите программу, которая принимает на вход координаты точки (X и Y) 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

# x = int(input('Введите координату точки x: '))
# y = int(input('Введите координату точки y: '))
# if x > 0 and y > 0:
#     print('1')
# if x < 0 and y > 0:
#     print('2')
# if x < 0 and y < 0:
#     print('3')
# if x > 0 and y < 0:
#     print('4') 

# Задача №3: Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter = int(input('Введите номер четверти: '))
# if quarter < 1 or quarter > 4:
#  print('Такой четверти не существует,пожалуйста,попробуйте ещё раз')
# elif quarter == 1:
#  print('x > 0 and y > 0')
# elif quarter == 2:
#  print('x < 0 and y > 0')
# elif quarter == 3:
#  print('x < 0 and y < 0')
# elif quarter == 4:
#  print('x > 0 and y < 0')

#  Задача №4: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#  Пример:

#  A (3,6); B (2,1) -> 5,09
#  A (7,-5); B (1,-1) -> 7,21

# print('Введите координаты точки А:')
# xA = float(input('X: '))
# yA = float(input('Y: '))
# print("Введите координаты точки B:")
# xB = float(input('X: '))
# yB = float(input('Y: '))

# from math import sqrt

# distance = round(sqrt((xA-xB)**2+(yA-yB)**2),2)
# print('Расстояние между точками',distance)










