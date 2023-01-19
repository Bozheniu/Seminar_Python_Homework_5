"""Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты
у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом"""""


import random

messages = ['возьмите конфеты', 'сколько конфет заберете?']


def game(all_candies, max_candies_for_one, players, messages):
    count = 0

    while all_candies > 0:
        print(f'{players[count % 2]}, {random.choice(messages)}')
        move = int(input())
        if move > all_candies or move > max_candies_for_one:
            print(f'Вы забрали слишком много конфет! Попробуйте еще раз:')
            move = int(input())
        all_candies = all_candies - move
        if all_candies > 0:
            print(f'Осталось {all_candies} конфет')
        else:
            print('Конфеты закончились!')
        count += 1
    return players[not count % 2]


player1 = input('Первый игрок, введите свое имя: \n')
player2 = input('Второй игрок, введите свое имя: \n')
players = [player1, player2]

all_candies = 100
max_candies_for_one = 28

winner = game(all_candies, max_candies_for_one, players, messages)
if not winner:
    print('Победителя нет')
else:
    print(f'Победил {winner}! Он получает все конфеты!')