#Jake Eaton
#Death

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
    type("Your mind suddenly starts to flash with memories and your body aches in pain\n")
    time.sleep(2)
    type("'Memory Overload! The implant is being resisted!'\n")
    time.sleep(2)
    type("'Release the implant!' a woman shouts\n")
    time.sleep(2)
    type("You shout in pain as the neural implant is removed from the back of your neck\n")
    time.sleep(2)
    type("You feel your blood flowing down your neck as you are set free\n")
    time.sleep(2)
    type("You collapse onto the cold solid floor beneath you and pant heavily\n")
    time.sleep(2)
    type("'You resisted. You changed the memory.' said a woman above you. You try to look up at the armoured woman\n")
    time.sleep(2)
    type("'I am sorry. But unless you follow our orders, you can not live.' you can just make out a gun pointing at your head\n")
    time.sleep(2)
    type("You hold up your hand, shaking\n")
    time.sleep(2)
    type("'Wait a minute!' you say weakly. But it didn't stop the inevitable...\n")
    mixer.music.load("PistolShot.mp3")
    mixer.music.play()
    time.sleep(2)
    type("You don't even feel the shot...\n")
    time.sleep(2)
    type("You don't even feel yourself hit the ground...\n")
    time.sleep(2)
    type2("You")
    time.sleep(2)
    type2("Feel")
    time.sleep(2)
    type2("Nothing...\n")
