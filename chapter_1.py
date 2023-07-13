from chapter_1_texts import *
from character import *
from classes import *
from game_over import game_over_loose
from write_function import *
from random_func import *



def choise_1(list): # начальное действие в пещере
    choose_1_0()
    data = input('enter number: ')
    if data == "1":
        choose_1_1()
        sleep(3)
        add_weapon(list)
        print('>Больше здесь делать нечего. Вы возвращаетесь к лучу света.')
        return choise_1_2(list)
    elif data == "2":
        choose_1_2()
        return 1
    elif data == "3":
        choose_1_3()

def choise_1_2(list): # начальное действие в пещере
    print('-'*80)
    print('Выберите действие:\n'
          '>пройти туда,откуда дует ветер (1)\n'
          '>подождать немного любуясь светом с потолка пещеры(2)\n')
    print()
    data = input('enter number: ')
    if data == "1":
        choose_1_2()
        print(list)
        return list
    elif data == "2":
        choose_1_3()


def location_cave(list):
    # cave_intro()
    choise_1(list)

