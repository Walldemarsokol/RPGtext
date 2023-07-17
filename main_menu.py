from race import *
from classes import *

def load_game():
    pass


def new_game():
    race = menu_choose_race()
    dict = class_choise()
    dict['race'] = race
    dict['doctor_who'] = 'yes'
    return dict



def main_menu():
    print('-' * 100)
    print('<<<<<You are in main menu>>>>>')
    print('-' * 100)
    data = input('<New game> <Load game>\n'
                 '    (1)        (2) \n '
                 'Выберите действие: ')
    if data == "1":
        return new_game()
    elif data == "2":
        return load_game()
