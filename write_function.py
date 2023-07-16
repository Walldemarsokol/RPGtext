
def start_add_weapon(out_dict):# функция из принимаемого списка забирает
    weapons = { 'warrior':'Короткий меч','mage':'Палочка мага','rouge':'Кинжал разбойника'}
    # for key in out_dict:
    res = out_dict.get('class')
    if res =='warrior' or res == 'mage' or res== 'rouge':
        weapon = weapons.get(res)
        print(f'Вы нашли <{weapon}>')
        out_dict['weapon'] = weapon
        return out_dict
