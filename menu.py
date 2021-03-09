#Jake Eaton

import time
from main_game import Main_Game
from os import system, name
from typing import type

def clear():
    if name =='nt':
        _ = system('cls')

type("Welcome\n")
time.sleep(2)
type("Please remember this is still in Beta and may never have a full 1.0 release\n")
time.sleep(2)
type("If you spot any bugs other than those mentioned in the Release Notes, please let me know")
time.sleep(2)
type("All releases and the Source Code can be found on GitHub using the link:")
time.sleep(2)
type("Read the book as it is released at https://www.wattpad.com/story/245646734-the-formula-front-war-part-of-the-world-space")
time.sleep(2)
type("The Text Adventure will start in 10 seconds...")
time.sleep(10)
clear()
Main_Game()
