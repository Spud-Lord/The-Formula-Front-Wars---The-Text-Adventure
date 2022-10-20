#Jake Eaton
#DeathV2

import time
import os
import sys                                          #Imports time, OS, Sys and Pygame Modules
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"   #Hides the Welcome to Pygame Message
from pygame import mixer
from typing import type, type2

def Death():                                        #Defines all indented code as Death
    mixer.init()
    mixer.music.load("imperial_alert.mp3")          #Loads and plays the mp3 file
    mixer.music.play(1)

    type("'Critical Failure!' you hear a voice shout\n")
    time.sleep(2)