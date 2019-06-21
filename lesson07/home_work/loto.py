#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

total_barrel = 90


class Barrel:
    def __init__(self, total_barrel):
        self.total_barrel = total_barrel
        self.count = self.unique()
        self.list_num = [x for x in range(1, self.total_barrel + 1)]

    def unique(self):
        random.shuffle(self.list_num)
        for i, j in enumerate(self.list_num):
            self.total_barrel - (i + 1)
            print(f"Следующий бочонок - {j} (осталось {self.total_barrel - (i + 1)})")
            yield j



class Card:

    def string(self):
        check = []
        num_list = []
        while len(num_list) < 15:
            number = str(random.randrange(1, 91))
            if number not in check:
                num_list.append(number)
                check.append(number)
        return num_list

    def int_card(self):
        avg = len(self.string()) / 3
        self.out = []
        last = 0
        while last < len(self.string()):
            self.out.append(self.string()[int(last):int(last + avg)])
            last += avg
        for i, j in enumerate(self.out):
            self.out[i] = list(j) + list(" " * 4)
            for x, y in enumerate(j):
                if int(y) < 10:
                    self.out[i][x] = f"{y} "
            random.shuffle(self.out[i])
        print("-------------------------------")
        print(self.player)
        print("-------------------------------")
        print(f"{'  '.join(self.out[0])}\n{'  '.join(self.out[1])}\n{'  '.join(self.out[2])}")
        print("-------------------------------")
        return self.out

    def __init__(self, player):
        self.player = player
        card = self.int_card()




class Game:
    def __init__(self):
        self.card_human = Card("Ваша карточка")
        self.card_computer = Card("Карточка компьютера")
        self.first_move = Barrel(total_barrel)
        self.start_game()
    def start_game(self):
        self.move = next(self.first_move.count)

    def check(self, num_list):
        print(num_list)
        for i, j in enumerate(num_list):
            for x, y in enumerate(j):
                if self.move == y:
                    num_list[i][x] = "-"
                    print(num_list)













game = Game()
print(game.check(Card("Моя карточка")))




# next(test.count)
# next(test.count)

