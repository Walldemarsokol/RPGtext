


def write_weapon(char_class):# функция из принимаемого списка забирает
    weapon = ''
    if 'warrior' in char_class:
        weapon = 'Короткий меч'
        print('Вы нашли короткий меч')
    elif 'mage' in char_class:
        weapon = 'Палочка мага'
        print('Вы нашли палочку мага')
    elif 'rouge' in char_class:
        weapon = 'Кинжал разбойника'
        print('Вы нашли кинжал разбойника')
    else:
        weapon = 'Жезл клирика'
        print('Вы нашли жезл клирика')


    with open('weapon.txt','w',encoding= 'utf8') as text_weapon:
        text_weapon.write(weapon)
