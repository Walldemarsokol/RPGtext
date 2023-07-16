import random

def human_race():
    human = 'Human'
    return human

def orc_race():
    orc = 'Orc'
    return orc

def elf_race():
    elf = 'Elf'
    return elf

def dwarf_race():
    dwarf = 'Dwarf'
    return dwarf

def menu_choose_race():
    data = input(">Выберите рассу:\n<человек> <эльф> <орк> <гном>)\n   (1)     (2)    (3)    (4)\n Enter num: ")
    if data == "1":
        return human_race()
    elif data == "2":
        return elf_race()
    elif data == "3":
        return orc_race()
    elif data == "4":
        return dwarf_race()
    else:
        print("Неверное значение!")
        return menu_choose_race()