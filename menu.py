#Jake Eaton

import time
from main_game import Main_Game
from typing import type     #Imports time, os and pygame modules as well as the code objects from external scripts
from clear import clear
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"       #Used to hide the PyGame welcome message
from pygame import mixer

type("Welcome!\n")      #Uses imported type object to print the letters individually
time.sleep(2)           #Pauses code for 2 seconds
type("Please note: This is still in Beta\n")
time.sleep(2)
type("All future versions can be found using the link: https://github.com/Spud-Lord/The-Formula-Front-Wars---The-Text-Adventure\n")
time.sleep(2)
type("DISCLAIMER: Some of the scenes in this game are not appropriate for children under 12. It is entirely your discretion to play this game\n")
time.sleep(2)
type("The Text Adventure will start in 10 seconds...")
mixer.init()        #Intialises PyGame Mixer
mixer.music.load("10SecondCountdown.mp3")       #Loads audio
mixer.music.play(1)     #Plays audio once
time.sleep(10.5)
clear()     #Clears terminal using imported clear object
Main_Game() #Runs imported Main_Game object
