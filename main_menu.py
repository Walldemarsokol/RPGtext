from race import *
from classes import *
from write_function import *

def load_game():
    pass


def new_game():
    race = menu_choose_race()
    list = class_choise()
    list.append(race)
    return list




def main_menu():
    print('-' * 100)
    print('You are in main menu')
    print('-' * 100)
    data = input('<New game> <Load game>\n'
                 '    (1)        (2) \n Выберите действие: ')
    if data == "1":
        return new_game()
    elif data == "2":
        return load_game()
