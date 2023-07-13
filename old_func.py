def choise_race():
    print(">Выберите рассу:\n"
          "нажмите 1 (человек)\n"
          "нажмите 2 (эльф)\n"
          "нажмите 3 (орк)\n"
          "нажмите 4 (гном)\n")
    data = input('enter: ')
    if data == "1":
        print('-' * 80)
        print('В отражении вы видите лицо человека.')
        print('-' * 80)
        return human_race()
    elif data == "2":
        print('-' * 80)
        print('В отражении вы видите лицо эльфа.')
        print('-' * 80)
        return elf_race()
    elif data == "3":
        print('-' * 80)
        print('В отражении вы видите лицо орка.')
        print('-' * 80)
        return orc_race()
    elif data == "4":
        print('-' * 80)
        print('В отражении вы видите лицо гнома.')
        print('-' * 80)
        return dwarf_race()


def class_choise():  # метод выбор класса
    print(">Выберите класс:\n"
          "нажмите 1 (воин)\n"
          "нажмите 2 (маг)\n"
          "нажмите 3 (разбойник)\n"
          "нажмите любую клавишу, если неважно (random)")
    data = input('enter: ')
    if data == '1':
        print('-' * 80)
        print('Вы выбрали класс воин!')
        print('-' * 80)
        return warrior()
    elif data == '2':
        print('-' * 80)
        print('Вы выбрали класс маг!')
        print('-' * 80)
        return mage()
    elif data == '3':
        print('-' * 80)
        print('Вы выбрали класс разбойник!')
        print('-' * 80)
        return rouge()
    # elif data == '4':
    #     print('-' * 80)
    #     print('Вы выбрали класс клирик!')
    #     print('-' * 80)
    #     return cleric()
    else:
        return random_class()


def start_add_weapon(char_class):# функция из принимаемого списка забирает

    if 'warrior' in char_class:
        weapon = 'Короткий меч'
        print(f'Вы нашли <{weapon}>')
        char_class.append(weapon)
        return char_class
    elif 'mage' in char_class:
        weapon = 'Палочка мага'
        print(f'Вы нашли <{weapon}>')
        char_class.append(weapon)
        return char_class
    elif 'rouge' in char_class:
        weapon = 'Кинжал разбойника'
        print(f'Вы нашли <{weapon}>')
        char_class.append(weapon)
        return char_class

def cleric():
    hp = 20  # множитель
    mp = 10  # множитель
    ap = 3  # множитель
    str = 10  # сила
    dex = 3  # ловкость
    endr = 5  # выносливость
    intel = 2  # интеллекс
    status_list = ['cleric', hp * endr, mp * intel, ap * dex, str, dex, endr,
                    intel]
    # class, HP,MP,AP strength,dexterity,endurance,intelligence
    return status_list