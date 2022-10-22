#Jake Eaton

import time
from main_game import Main_Game
from typing import type
from clear import clear
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

type("Welcome!\n")
time.sleep(2)
type("Please note: This is still in Beta\n")
time.sleep(2)
type("All future versions can be found using the link: https://github.com/Spud-Lord/The-Formula-Front-Wars---The-Text-Adventure\n")
time.sleep(2)
type("DISCLAIMER: Some of the scenes in this game are not appropriate for children under 12. It is entirely your discretion to play this game\n")
time.sleep(2)
type("The Text Adventure will start in 10 seconds...")
mixer.init()
mixer.music.load("10SecondCountdown.mp3")
mixer.music.play(1)
time.sleep(10.5)
clear()
Main_Game()