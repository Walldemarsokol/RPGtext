


def add_weapon(char_class):# функция из принимаемого списка забирает
    # weapons = { 'warrior' :'Короткий меч',}
    if 'warrior' in char_class:
        weapon = 'Короткий меч'
        print(f'Вы нашли {weapon}')
        char_class.append(weapon)
        return char_class
    elif 'mage' in char_class:
        weapon = 'Палочка мага'
        print(f'Вы нашли {weapon}')
        char_class.append(weapon)
        return char_class

    elif 'rouge' in char_class:
        weapon = 'Кинжал разбойника'
        print(f'Вы нашли {weapon}')
        char_class.append(weapon)
        return char_class


