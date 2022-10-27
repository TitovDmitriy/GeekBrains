# Task2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# а) Добавьте игру против бота
# б) Подумайте как наделить бота "интеллектом"

from random import *

def Player_vs_Player():
    candies_amount = 2021
    max_bet = 28
    count = 0
    player_1 = 'Игрок 1'
    player_2 = 'Игрок 2'

    print('\nВыбираем того, кто начнёт игру...')

    x = randint(1, 2)
    if x == 1:
        first = player_1
        second = player_2
    else:
        first = player_2
        second = player_1
    print(f'{first} - ходит первым!')

    while candies_amount > 0:
        if count == 0:
            move = int(input(f'{first}, ставка: '))
            if move > candies_amount or move > max_bet or move <= 0:
                move = int(input(f'За один ход можно взять от 1 до 28 конфет, {first} переигрывай: '))
            candies_amount = candies_amount - move
        if candies_amount > 0:
            print(f'Осталось - {candies_amount}')
            count = 1
        else:
            print('Игра окончена!')
        if count == 1:
            move = int(input(f'{second}, ход: '))
            if move > candies_amount or move > max_bet or move <= 0:
                move = int(input(f'За один ход можно взять от 1 до 28 конфет, {second} переигрывай: '))
            candies_amount = candies_amount - move
        if candies_amount > 0:
            print(f'осталось {candies_amount}')
            count = 0
        else:
            print('Игра окончена!')
    if count == 1:
        print(f'Победитель - {second}')
    if count == 0:
        print(f'Победитель - {first}')

def Player_vs_Bot():
    candies_amount = 2021
    max_bet = 28
    player_1 = 'Игрок'
    player_2 = 'Бот'
    players = [player_1, player_2]

    lottery = randint(-1, 0)
    print('\nВыбираем того, кто начнёт игру...')
    print(f'{players[lottery+1]} начинает!')

    while candies_amount > 0:
        lottery += 1
        if players[lottery%2] == 'Бот':
            print(
                f'Ходит {players[lottery%2]}. Осталось {candies_amount} конфет.')
            if candies_amount < 29:
                move = candies_amount
            else:
                strategy_bot = candies_amount//28
                move = candies_amount - ((strategy_bot*max_bet)+1)
                if move == -1:
                    move = max_bet - 1
                if move == 0:
                    move = max_bet
            while move > 28 or move < 1:
                move = randint(1, 28)
            print(move)
        else:
            move = int(input(f'Осталось {candies_amount} конфет. Делай свой ход {players[lottery%2]}: '))
            while move > max_bet or move > candies_amount or move <= 0:
                move = int(input('За один ход можно взять от 1 до 28 конфет, переигрывай: '))
        candies_amount = candies_amount - move
    print(f'Осталось - {candies_amount} \tПобедитель - {players[lottery%2]}')

def Choise():
    print('Выберите режим игры:')
    messege = (int(input('   Если нужен режим "Игрок против Игрока" - нажмите цифру 1: \n'
                    '   Если интересен режим "Игрок против Бота" - нажмите цифру 2: '))) 
    if messege == 1:
        print("\nВыбран режим 'Игрок против Игрока'")
        return Player_vs_Player()
    if messege == 2:
        print("\nВыбран режим 'Игрок против Бота'")
        return Player_vs_Bot()

print('Правила игры: имеется 2021 конфета!\n'
      'Поочередно берём не более 28 конфет.\n'
      'Все конфеты достаются тому, кто сделает последний ход.\n')
      
Choise()