#Jake Eaton

import time
from main_gamev2 import Main_Game
from os import system, name
from typing import type
from clear import clear
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

type("Welcome\n")
time.sleep(2)
type("Please note: This is still in Beta\n")
time.sleep(2)
type("If you spot any bugs other than those mentioned in the Release Notes, please let me know")
time.sleep(2)
type("All releases and the Source Code can be found on GitHub using the link: https://github.com/Spud-Lord/The-Formula-Front-Wars---The-Text-Adventure")
time.sleep(2)
type("DISCLAIMER: This game is not really appropriate for children under 12. It is entirely your discretion to play this game")
time.sleep(2)
type("The Text Adventure will start in 10 seconds...")
mixer.init()
mixer.music.load("10SecondCountdown.mp3")                                    #Plays mp3 file
mixer.music.play(1)
time.sleep(10.5)
clear()
Main_Game()
