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
    type("Your body begins to shake violently as you resist the implant\n")
    time.sleep(2)
    type("'Release him!' a woman shouts\n")
    time.sleep(2)
    type("You scream in pain as the neural implant is ripped from the back of your neck\n")
    time.sleep(2)
    type("You can feel your blood flowing down your neck and your vision starts to get hazy.\n")
    time.sleep(2)
    type("'You resisted! You changed the memory!' shouted a woman in front of you. You just make out the armoured woman you saw earlier\n")
    time.sleep(2)
    type("She pointed her pistol up your head and whispered in your ear\n")
    time.sleep(2)
    type("'Let me put you out of your misery. I have waited a long time to do this...'\n")
    time.sleep(2)
    type("'Wait a minute...' you say weakly\n")
    mixer.music.load("PistolShot.mp3")
    mixer.music.play()
    time.sleep(2)
    type("You don't even feel the shot before your vision ceases and your mind goes silent...\n")
    dead = True