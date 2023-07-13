from classes import *
from character import *
from main_menu import *
from intro import greetings
from path import path_on_road
from chapter_1 import *


def start_game():
    # greetings()
    char_class = main_menu()
    location_cave(char_class)
    print(char_class)

start_game()