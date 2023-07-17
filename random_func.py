from classes import *
from random import *
from write_function import *


def random_choice(a, b):
    result = randint(a,b)
    return result


def remains_event_1_lvl(dict):
    weapon = dict.get('weapon')
    hero = dict.get('class')
    body = ['оркa','гномa','эльфа','челвека']
    body_random = randint(0,4)
    if weapon == None:
        print(f'>>Вы обнаружили останки гуманоида. Это был {hero}. Вы нашли чудом уцелевшее оружие.')
        start_add_weapon(dict)
        print(">>Вы идете дальше. Настроение немного прибавилось.")
    else:
        print(f'>>Вы обнаружили останки {body[body_random]}. Вокруг только сгнившее оружие и куча паутины.\n '
              'Вы просто идете дальше...')