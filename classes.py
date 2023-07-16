from random import *


def class_choise():  # метод выбор класса
    data = input("Выберите свой класс!\n"
                 "<Воин>  <Маг>  <Вор> \n"
                 " (1)     (2)    (3)  \n"
                 "Enter number: ")
    print('-'*25)
    if data == '1':
        dict = warrior()
        parameters = ['Здоровье','Мана','Очки действий','Сила','Ловкость','Выносливость','Интеллект','Базовая атака','Базовая защита']
        values = ['health_points', 'mana_points', 'action_points', 'str', 'dex', 'endr', 'intel','attack','armor' ]
        for i in range(len(parameters)):
            print(f'>>{parameters[i]} = {dict.get(values[i])}')
        print('_'*25)
        print('Вы хотите выбрать воина?\n''<<Yes(1)>>  <<No(2)>>')
        res = input('Enter number: ')
        if res == '1':
            return warrior()
        elif res == '2':
            return class_choise()
        else:
            print('Неверный ввод. Выберите класс героя.')
            return class_choise()
    elif data == '2':
        return mage()
    elif data == '3':
        return rouge()
    else:
        print('Неверно. Введите корректный номер.')
        return class_choise()


def status_calc(list_1,list_2,dict,):
    count = 0
    for element in range(len(list_1)):
        dict[list_2[element]] = list_1[count]
        count+=1
    return dict



def warrior():
    health_points = 20  # очки здоровья
    mana_points = 10  # очки магии
    action_points = 1  # очки действий
    str = 10 # сила
    dex = 3 # ловкость
    endr = 5 #выносливость
    intel = 2 #интеллект
    attack = 1 # показатель атаки
    armor = 1
    status_dict = {'class':'warrior',}
    status_list = [ health_points * endr, mana_points * intel,action_points * dex, str, dex, endr,
                   intel, attack * str, endr * armor]
    status_char = ['health_points', 'mana_points', 'action_points', 'str', 'dex', 'endr', 'intel','attack','armor' ]
    status_dict=status_calc(status_list,status_char,status_dict)

    # class, HP,MP,AP strength,dexterity,endurance,intelligence
    return status_dict


def mage():
    health_points = 20  # очки здоровья
    mana_points = 10  # очки магии
    action_points = 1  # очки действий
    str = 2  # сила
    dex = 4  # ловкость
    endr = 4  # выносливость
    intel = 10  # интеллект
    attack = 1 # показатель атаки
    armor = 1
    status_dict = {'class':'mage'}
    status_list = [health_points * endr, mana_points * intel, action_points * dex, str, dex, endr,
                   intel, attack * intel, endr * armor]
    status_char = ['health_points', 'mana_points', 'action_points', 'str', 'dex', 'endr', 'intel','attack','armor' ]
    status_calc(status_list,status_char,status_dict)
    # class, HP,MP,AP strength,dexterity,endurance,intelligence
    return status_list


def rouge():
    char_class = 'rouge'
    health_points = 20  # очки здоровья
    mana_points = 10  # очки магии
    action_points = 1  # очки действий
    str = 3  # сила
    dex = 10  # ловкость
    endr = 3  # выносливость
    intel = 4  # интеллект
    attack = 1 # показатель атаки
    armor = 1
    status_dict = {}
    status_list = [health_points * endr, mana_points * intel, action_points * dex, str, dex, endr,
                   intel, attack * str, endr * armor]
    status_char = ['health_points', 'mana_points', 'action_points', 'str', 'dex', 'endr', 'intel','attack','armor' ]
    status_calc(status_list, status_char, status_dict)
    # class, HP,MP,AP strength,dexterity,endurance,intelligence
    return status_list
