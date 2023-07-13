# def choise_race():
#     print(">Выберите рассу:\n"
#           "нажмите 1 (человек)\n"
#           "нажмите 2 (эльф)\n"
#           "нажмите 3 (орк)\n"
#           "нажмите 4 (гном)\n")
#     data = input('enter: ')
#     if data == "1":
#         print('-' * 80)
#         print('В отражении вы видите лицо человека.')
#         print('-' * 80)
#         return human_race()
#     elif data == "2":
#         print('-' * 80)
#         print('В отражении вы видите лицо эльфа.')
#         print('-' * 80)
#         return elf_race()
#     elif data == "3":
#         print('-' * 80)
#         print('В отражении вы видите лицо орка.')
#         print('-' * 80)
#         return orc_race()
#     elif data == "4":
#         print('-' * 80)
#         print('В отражении вы видите лицо гнома.')
#         print('-' * 80)
#         return dwarf_race()


# def class_choise():  # метод выбор класса
#     print(">Выберите класс:\n"
#           "нажмите 1 (воин)\n"
#           "нажмите 2 (маг)\n"
#           "нажмите 3 (разбойник)\n"
#           "нажмите любую клавишу, если неважно (random)")
#     data = input('enter: ')
#     if data == '1':
#         print('-' * 80)
#         print('Вы выбрали класс воин!')
#         print('-' * 80)
#         return warrior()
#     elif data == '2':
#         print('-' * 80)
#         print('Вы выбрали класс маг!')
#         print('-' * 80)
#         return mage()
#     elif data == '3':
#         print('-' * 80)
#         print('Вы выбрали класс разбойник!')
#         print('-' * 80)
#         return rouge()
#     # elif data == '4':
#     #     print('-' * 80)
#     #     print('Вы выбрали класс клирик!')
#     #     print('-' * 80)
#     #     return cleric()
#     else:
#         return random_class()