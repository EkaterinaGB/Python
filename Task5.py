# Задача №1: Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')

# Задача №2: Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import *
# import os


# welcome_text = ('Приветствую Вас, давайте сыграем в игру!\n'
#                 'Для начала я расскажу правила:\n'
#                 'Я даю Вам 2021 конфету, вы берете их поочереди,\n'
#                 'причем, за один раз можно взять не больше 28 конфет.\n'
#                 'Выигрывает тот, кто последним ходом заберет все конфеты.\n'
#                 'Ну что начнем?')
# print(welcome_text)

# message = ['твоя очередь']


# def player_vs_player():
#     candies_total = 2021
#     max_take = 28
#     count = 0
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = input('\nА твоего соперника?: ')

#     print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     x = randint(1, 2)
#     if x == 1:
#         lucky = player_1
#         loser = player_2
#     else:
#         lucky = player_2
#         loser = player_1
#     print(f'Поздравляю {lucky} ты ходишь первым !')

#     while candies_total > 0:
#         if count == 0:
#             step = int(input(f'\n{choice(message)} {lucky} = '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\nНе жадничай можно взять только {max_take} конфет {lucky}, попробуй еще раз: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\nна кону еще {candies_total}')
#             count = 1
#         else:
#             print('Все кончились конфетки')

#         if count == 1:
#             step = int(input(f'\n{choice(message)}, {loser} '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\nНе жадничай можно взять только {max_take} конфет {loser}, попробуй еще раз: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\nна кону еще {candies_total}')
#             count = 0
#         else:
#             print('Баста, карапузик, кончились конфетки')

#     if count == 1:
#         print(f'{loser} ПОБЕДИЛ')
#     if count == 0:
#         print(f'{lucky} ПОБЕДИЛ')


# player_vs_player()


# def player_vs_bot():
#     candies_total = 2021
#     max_take = 28
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = 'Компьютер'
#     players = [player_1, player_2]
#     print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     lucky = randint(-1, 0)

#     print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

#     while candies_total > 0:
#         lucky += 1

#         if players[lucky % 2] == 'Компьютер':
#             print(
#                 f'\nХодит {players[lucky%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

#             if candies_total < 29:
#                 step = candies_total
#             else:
#                 delenie = candies_total//28
#                 step = candies_total - ((delenie*max_take)+1)
#                 if step == -1:
#                     step = max_take -1
#                 if step == 0:
#                     step = max_take
#             while step > 28 or step < 1:
#                 step = randint(1,28)
#             print(step)
#         else:
#             step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа кону {candies_total} {choice(message)}:  '))
#             while step > max_take or step > candies_total:
#                 step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
#         candies_total = candies_total - step

#     print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

# player_vs_bot()

# Задача №3: Создайте программу для игры в ""Крестики-нолики"".

# theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
#             '4': ' ' , '5': ' ' , '6': ' ' ,
#             '1': ' ' , '2': ' ' , '3': ' ' }

# board_keys = []

# for key in theBoard:
#     board_keys.append(key)

# def printBoard(board):
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])

# def game():

#     turn = 'X'
#     count = 0


#     for i in range(10):
#         printBoard(theBoard)
#         print("Выш ход," + turn + ".Куда поставить знак?")

#         move = input()        

#         if theBoard[move] == ' ':
#             theBoard[move] = turn
#             count += 1
#         else:
#             print("Эта позиция уже занята.\nКуда поставить знак?")
#             continue

        
#         if count >= 5:
#             if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # верх
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")                
#                 break
#             elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # середина
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break
#             elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # низ
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break
#             elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # вниз по левой стороне
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break
#             elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # посередине
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break
#             elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # вниз по правой стороне
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break 
#             elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # диагональ
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break
#             elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # диагональ
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break 

        
#         if count == 9:
#             print("\nКонец игры.\n")                
#             print("Ничья!!")

        
#         if turn =='X':
#             turn = 'O'
#         else:
#             turn = 'X'        
    
    
#     restart = input("Хотите сыграть ещё раз?(y/n)")
#     if restart == "y" or restart == "Y":  
#         for key in board_keys:
#             theBoard[key] = " "

#         game()

# if __name__ == "__main__":
#     game()

# Задача №4: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")