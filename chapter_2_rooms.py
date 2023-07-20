from random import *
from time import sleep


def re_random_room(enemy):
    res = input(f'Вы обнаружили врага {enemy} и он не заметил Вас первым.\n Можете напасть первым(1)\n \
            Или можете сбежать(2)')
    if res == '1':
        pass
        print(f'Вы одержали победу. Больше в этой комнате нечего делать...\
        Вы вышли из комнаты.')
    if res == '2':
        pass
    else:
        re_random_room(enemy)

def random_room(data,loot,enemy):
    nums = randint(1,4)
    loot_random = randint(1,5)
    luck = data.get('luck')
    dex = data.get('dex')
    streigth = data.get('str')
    print('>>Вы заходите в комнату. Она очень похожа на другие.')
    sleep(2)
    print(('-'*20)+'>')
    if nums == 1:#1
        print(f'>>Оглядывая комнату Вы обаружили {loot.get()}')
    elif nums == 1 and luck >= 2:
        print(f'>>Оглядывая комнату Вы обаружили {loot.get()}')
    elif nums == 1 and luck >= 3:
        event = ('>>Вы оглядываете комнату. В комнате обнаружен сундук. Попробуете его вскрыть? \
         Да(1)  Нет(2)' )
        if event == '1':
            pass
        elif event =='2':
            pass
        else:
            print('>>Вы делаете попытку взлома и замок ломается. Увы его уже никак не открыть..')
    elif nums == 2:#2
        print(f'>>Вы оглядываете комнату. Среди барахла Вы ничего не обнаружили...')
    elif nums == 3:#3
        print(f'>>Неожиданно на Вас нападает {enemy}')
    elif nums == 3 and luck >=3:
        res=input(f'>>Вы обнаружили врага {enemy} и он не заметил Вас первым.\n Можете напасть первым(1)\n \
        Или можете сбежать(2)')
        if res == '1':
            pass
            print(f'>>Одержав победу Вы забрали трофей {loot.get()}. Больше в этой комнате нечего делать...\
            Вы вышли из комнаты.')
        if res == '2':
            pass
        else:
            re_random_room(enemy)

