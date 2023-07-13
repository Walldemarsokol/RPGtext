from classes import *
from character import *
from main_menu import *
from intro import greetings
from path import path_on_road
from chapter_1 import *


def start_game():
    # greetings()
    char_class = main_menu()
    # location_cave(char_class)
    return char_class

def first_location(char_class):
    location_cave(char_class)
    return char_class

def second_location(list):
    pass

result_1 = start_game()
first_location(result_1)

