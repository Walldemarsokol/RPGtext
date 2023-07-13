from random import *

def class_choise():  # метод выбор класса
    data = input("Выберите свой класс!\n"
                 "<Воин>  <Маг>  <Вор> \n"
                 " (1)     (2)    (3)  \n"
                 "Enter number: ")
    if data == '1':
        return warrior()
    elif data == '2':
        return mage()
    elif data == '3':
        return rouge()
    else:
        data = randint(1,4)
        if data == 1:
            return warrior()
        elif data == 2:
            return mage()
        else:
            return rouge()




def warrior():
    hp = 20  # множитель
    mp = 10  # множитель
    ap = 3  # множитель
    str = 10 # сила
    dex = 3 # ловкость
    endr = 5 #выносливость
    intel = 2 #интеллект
    attack = 1 # показатель атаки
    defence = 0.5 # множитель
    armor = 1
    status_list = ['warrior', hp * endr, mp * intel, ap * dex, str, dex, endr,
                   intel, attack * str,defence * endr + armor]
    # class, HP,MP,AP strength,dexterity,endurance,intelligence
    return status_list


def mage():
    hp = 20  # множитель
    mp = 10  # множитель
    ap = 3  # множитель
    str = 10  # сила
    dex = 3  # ловкость
    endr = 5  # выносливость
    intel = 10  # интеллект
    attack = 1 # показатель атаки
    defence = 0.5 # множитель
    armor = 1
    status_list = ['mage', hp * endr, mp * intel, ap * dex, str, dex, endr,
                   intel,attack * str,defence * endr + armor]
    # class, HP,MP,AP strength,dexterity,endurance,intelligence
    return status_list


def rouge():
    hp = 20  # множитель
    mp = 10  # множитель
    ap = 3  # множитель
    str = 3  # сила
    dex = 10  # ловкость
    endr = 3  # выносливость
    intel = 4  # интеллект
    attack = 1 # показатель атаки
    defence = 0.5 # множитель
    armor = 1
    status_list = ['rouge', hp * endr, mp * intel, ap * dex, str, dex, endr,
                   intel,attack * str,defence * endr + armor]
    # class, HP,MP,AP strength,dexterity,endurance,intelligence
    return status_list
