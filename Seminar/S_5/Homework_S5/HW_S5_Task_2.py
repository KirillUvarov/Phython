# # Создайте программу для игры с конфетами человек против человека.
# # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# # Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# # Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# # чтобы забрать все конфеты у своего конкурента?
# # a) Добавьте игру против бота
# # b) Подумайте как наделить бота ""интеллектом""

import random

def lollipop():
    lol = 100
    maximum_lol = 28
    minimum_lol = 1
    count = 0
    
    the_lot_1 = random.randint(1, 2)
    if the_lot_1 == 1:
        the_lot_2 = int(2)
    else: 
        the_lot_2 = int(1)
        print(f'Начинает ИГРОК {the_lot_1}')

    # print(the_lot_1)
    # print(the_lot_2)
    # exit()

    while lol > 0:
        if count == 0:
            if lol > 0:    
                x = (int(input(f'ИГРОК {the_lot_1}, возьмите со стола от 1 до 28 конфет: ')))
                if x in range(1, 29): 
                    if x <= lol: 
                        lol = lol - x
                        print(f'Конфет осталось: {lol}')
                        count +=1
                    else: 
                        print(f'На столе {lol} конфет. Попробуй ещё раз!')
                else: print('Больше 28 конфет брать нельзя!')
            else:
                print(f'Конфеты кончились(((')


        if count == 1:
            if lol > 0:
                x = (int(input(f'ИГРОК {the_lot_2}, возьмите со стола от 1 до 28 конфет: ')))
                if x in range(1, 29): 
                    if x <= lol: 
                        lol = lol - x
                        print(f'Конфет осталось: {lol}')
                        count -=1
                    else: 
                        print(f'На столе {lol} конфет. Попробуй ещё раз!')
                else: print('Больше 28 конфет брать нельзя!')
            else:
                print(f'Конфеты кончились(((')

    if count == 1:
        print(f'Победил ИГРОК {the_lot_2}')
    if count == 0:
        print(f'Победил ИГРОК {the_lot_1}')

# lollipop()

# ____________________________________________________________________
# ИГРОК 1 против Компьютера:

def lollipop_2():
    lol = 100
    maximum_lol = 28
    count = 0
    
    the_lot_1 = random.randint(1, 2)
    if the_lot_1 == 1:
        the_lot_2 = int(2)
    else: 
        the_lot_2 = int(1)
        print(f'Начинает ИГРОК {the_lot_1}')

    # print(the_lot_1)
    # print(the_lot_2)
    # exit()

    while lol > 0:
        if count == 0:
            if lol > 0:    
                x = (int(input(f'ИГРОК {the_lot_1}, возьмите со стола от 1 до 28 конфет: ')))
                if x in range(1, 29): 
                    if x <= lol: 
                        lol = lol - x
                        print(f'Конфет осталось: {lol}')
                        count +=1
                    else: 
                        print(f'На столе {lol} конфет. Попробуй ещё раз!')
                else: print('ОТ 1 ДО 28 СТРОГО!!!')
            else:
                print(f'Конфеты кончились(((')


        if count == 1:
            if lol > 0:
                # x = (int(input(f'ИГРОК {the_lot_2}, возьмите со стола от 1 до 28 конфет: ')))
                x = random.randint(1, 29)
                print(f'Компьютер выбрал {x} конфет')
                if x in range(1, 29):
                    if x <= lol: 
                        lol = lol - x
                        print(f'Конфет осталось: {lol}')
                        count -=1
                    else: 
                        print(f'На столе {lol} конфет. Попробуй ещё раз!')
                else: print('ОТ 1 ДО 28 СТРОГО!!!')
            else:
                print(f'Конфеты кончились(((')

    if count == 1:
        print(f'Победил ИГРОК {the_lot_2}')
    if count == 0:
        print(f'Победил ИГРОК {the_lot_1}')

# lollipop_2()

# ____________________________________________________________________
# ИГРОК против умного Компьютера:

def lollipop_3():
    lol = 100
    count = 0
    
    the_lot_1 = 'ИГРОК'
    the_lot_2 = 'КОМПЬЮТЕР'

    while lol > 0:
        if count == 0:
            if lol > 0:
                x = (int(input(f'{the_lot_1}, возьмите со стола от 1 до 28 конфет: ')))
                if x in range(1, 29):
                    if x <= lol: 
                        lol = lol - x
                        print(f'Конфет осталось: {lol}')
                        count +=1
                    else: 
                        print(f'На столе {lol} конфет. Попробуй ещё раз!')
                else: print('ОТ 1 ДО 28 СТРОГО!!!')
            else:
                print(f'Конфеты кончились(((')

        r_1 = random.randint(1, 29)
        r_2 = lol-1


        if count == 1:
            if lol >= 30:
                x = r_1
            elif lol == 29:
                    x = 28
            elif lol == 1:
                    x = 1
            else: 
                    x = r_2
            if lol > 0:
                print(f'Компьютер выбрал {x} конфет')
                if x in range(1, 29):
                    if x <= lol: 
                        lol = lol - x
                        print(f'Конфет осталось: {lol}')
                        count -=1
                    else: 
                        print(f'На столе {lol} конфет. Попробуй ещё раз!')
                else: print('ОТ 1 ДО 28 СТРОГО!!!')
            else:
                print(f'Конфеты кончились(((')

    if count == 1:
        print(f'Победил {the_lot_2}')
    if count == 0:
        print(f'Победил {the_lot_1}')

lollipop_3()