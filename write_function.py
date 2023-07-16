
def start_add_weapon(out_dict):
    """"функция принимает словарь и на его основе доавляет оружие"""
    weapons = { 'warrior':'Короткий меч','mage':'Палочка мага','rouge':'Кинжал разбойника'}
    res = out_dict.get('class')
    if res =='warrior' or res == 'mage' or res== 'rouge':
        weapon = weapons.get(res)
        print('_'*(len(weapon)+13))
        print(f'|Вы нашли <{weapon}>|')
        print('-'*(len(weapon)+13))
        out_dict['weapon'] = weapon
        return out_dict