

def create_menu_parameters(dict):
    parameters = ['Здоровье', 'Мана', 'Очки действий', 'Сила', 'Ловкость', 'Выносливость', 'Интеллект','Удача', 'Базовая атака',
                  'Базовая защита']
    values = ['health_points', 'mana_points', 'action_points', 'str', 'dex', 'endr', 'intel','luck', 'attack', 'armor']
    word = 'class'
    print('-'*25)
    print(f'Параметры класса <<{dict.get(word)}>>')
    print('^'* (len(dict.get(word))+21))
    for i in range(len(parameters)):
        print(f'>>{parameters[i]} = {dict.get(values[i])}')
    print('_' * 25)
    print()

def class_choise():  # метод выбор класса
    data = input("Выберите свой класс!\n<Воин>  <Маг>  <разбойник> \n (1)     (2)       (3)  \nEnter number: ")
    if data == '1':
        dict = warrior()
        create_menu_parameters(dict)
        res = input('Вы хотите выбрать воина?\n<<Yes(1)>>  <<No(2)>>\n Enter number: ')
        if res == '1':
            return warrior()
        else:
            print('Неверный ввод. Выберите класс героя.')
            return class_choise()
    elif data == '2':
        dict = mage()
        create_menu_parameters(dict)
        res = input('Вы хотите выбрать мага?\n<<Yes(1)>>  <<No(2)>>\n Enter number: ')
        if res == '1':
            return mage()
        else:
            print('Неверный ввод. Выберите класс героя.')
            return class_choise()
    elif data == '3':
        dict = rouge()
        create_menu_parameters(dict)
        res = input('Вы хотите выбрать разбойника?\n<<Yes(1)>>  <<No(2)>>\n Enter number: ')
        if res == '1':
            return rouge()
        else:
            print('Неверный ввод. Выберите класс героя.')
            return class_choise()
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
    luck = 1    #luck
    attack = 1 # показатель атаки
    armor = 1
    status_dict = {'class':'warrior',}
    status_list = [health_points * endr, mana_points * intel, action_points * dex, str, dex, endr,
                   intel, luck, attack * intel, endr * armor]
    status_char = ['health_points', 'mana_points', 'action_points', 'str', 'dex', 'endr', 'intel', 'luck', 'attack',
                   'armor']
    status_calc(status_list,status_char,status_dict)
    return status_dict


def mage():
    health_points = 20  # очки здоровья
    mana_points = 10  # очки магии
    action_points = 1  # очки действий
    str = 2  # сила
    dex = 6  # ловкость
    endr = 2  # выносливость
    intel = 10  # интеллект
    luck = 1    #luck
    attack = 1 # показатель атаки
    armor = 1
    status_dict = {'class':'mage'}
    status_list = [health_points * endr, mana_points * intel, action_points * dex, str, dex, endr,
                   intel,luck, attack * intel, endr * armor]
    status_char = ['health_points', 'mana_points', 'action_points', 'str', 'dex', 'endr', 'intel','luck','attack','armor' ]
    status_calc(status_list,status_char,status_dict)
    return status_dict


def rouge():
    health_points = 20  # очки здоровья
    mana_points = 10  # очки магии
    action_points = 1  # очки действий
    str = 3  # сила
    dex = 10  # ловкость
    endr = 3  # выносливость
    intel = 4  # интеллект
    luck = 1 #luck
    attack = 1 # показатель атаки
    armor = 1
    status_dict = {'class':'rouge'}
    status_list = [health_points * endr, mana_points * intel, action_points * dex, str, dex, endr,
                   intel, luck, attack * intel, endr * armor]
    status_char = ['health_points', 'mana_points', 'action_points', 'str', 'dex', 'endr', 'intel', 'luck', 'attack',
                   'armor']
    status_calc(status_list, status_char, status_dict)
    return status_dict
