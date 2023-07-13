
def start_add_weapon(char_class):# функция из принимаемого списка забирает
    weapons = { 'warrior':'Короткий меч','mage':'Палочка мага','rouge':'Кинжал разбойника'}
    for key in char_class:
        if key =='warrior' or key == 'mage' or key == 'rouge':
            weapon = weapons.get(key)
            print(f'Вы нашли <{weapon}>')
            char_class.append(weapon)
            return char_class
