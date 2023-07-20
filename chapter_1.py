from chapter_1_texts import *
from random import *
from character import *
from classes import *
from game_over import game_over_loose
from write_function import *
from random_func import *

def random_travel(dict):
    """Функция для движения персонажа"""
    move = randint(0,21)
    weapon = dict.get('weapon')
    dock_event = dict.get('doctor_who')
    if move >= 0 and move <= 3:
        if weapon == None:
            remains_event_1_lvl(dict)
            sleep(3)
            print('-' * 20)
            return random_travel(dict)
        else:
            print('>>Вы двигаетесь вдоль пещеры. Кажется на вас кто-то смотрит. Вас не покидает чувство\n'
              'что за Вами следят.')
            sleep(2)
            print('-'*20)
            return random_travel(dict)
    elif move >= 4 and move <=7:
        print('>>Вы двигаетесь вдоль пещеры. Слышны странные шорохи в темноте. Вас не покидает чувство\n'
              'что за Вами следят.')
        sleep(2)
        print('-' * 20)
        return random_travel(dict)
    elif move >=8 and move <=10:
        print('>>Вы споткнулиcь и чуть не ушибли голову о камень...Будьте осторожнее!')
        sleep(2)
        print('-'*20)
        return random_travel(dict)
    elif move ==11:
        if dock_event == 'yes':
            print('>>В дали Вы видите необычное свечение. Подойдя ближе это оказывается необычная на вид синяя будка. \n'
              '>>По виду она сделана из дерева. Вы осматриваете надписи на ней: "Police box". \n'
              '>>Что бы это значило..? Будка издает странный звук и начинаем мигать. Через пару секунд она пропадает\n'
              '>>словно ничего и не было. Что это такое?!..\n'
              '>>Пещеру снова наполняет тьма и глазам нужно привыкнуть к темноте.. ')
            dict.pop('doctor_who')
            sleep(10)
            print(dict)
            return random_travel(dict)
        else:
            print('>>Вы идете и не замечаете ничего необычного..')
            sleep(2)
            print("-" * 20)
            return random_travel(dict)
    elif move >=12 and move <=19:
        print('>>Вы идете и спотыкаетесь. Еще бы чуть чуть и потеряли бы глаз...')
        sleep(2)
        print("-"*20)
        return random_travel(dict)
    elif move == 20:
        data=input('>>Вы обнаружили спуск. Судя по всему там ниже есть что-то интересное...\n'
              '>>Хотите спуститься? \n <<Yes(1)>>  <<No(2)>>')
        if data == '1':
            return
        elif data == '2':
            print('>>Вы решили поискать другой путь и возвращаетесь в попытке найти проход.')
            return random_travel(dict)






def choise_1(dict): # начальное действие в пещере
    choose_1_0()
    data = input('enter number: ')
    if data == "1":
        choose_1_1()
        sleep(3)
        start_add_weapon(dict)
        print('>Больше здесь делать нечего. Вы возвращаетесь к лучу света.')
        return choise_1_2(dict)
    elif data == "2":
        choose_1_2()
        return 1
    elif data == "3":
        choose_1_3()

def choise_1_2(dict): # начальное действие в пещере
    print('-'*80)
    print('Выберите действие:\n>пройти туда,откуда дует ветер (1)\n>подождать немного любуясь светом с потолка пещеры(2)\n')
    print()
    data = input('enter number: ')
    if data == "1":
        choose_1_2()
        return dict
    elif data == "2":
        choose_1_3()


def location_cave(dict):
    # cave_intro()
    random_travel(dict)
    choise_1(dict)


