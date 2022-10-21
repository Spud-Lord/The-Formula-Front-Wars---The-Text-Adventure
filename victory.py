#Jake Eaton
#Victory Code

import time
from typing import type, type2
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

def Victory():
    type("Emily quickly grabbed her pistol and shot it four times\n")
    mixer.music.load("4xPistolShot.mp3")
    mixer.music.play()
    time.sleep(2)
    type("Your arms and legs begin to bleed and you yell out in pain\n")
    time.sleep(2)
    type("'You'll recognise this method of execution. After all, you taught me it.' she says")
    time.sleep(2)
    type("Emily turns and starts to walk away. 'Find the Aorus and destroy it. His crew will come after him sooner or later.' she commanded")
    time.sleep(2)
    type("The Aorus. Your ship. Your crew. 'No...' you whisper, unable to muster anything else")
    time.sleep(2)
    type("You watch Emily walk off as your vision begins to blur\n")
    time.sleep(2)
    type("You close your eyes as the pain begins to subside...\n")
    time.sleep(2)
    type("Eventually...\n")
    type2("You...\n")
    type2("Felt...\n")
    type2("Nothing...\n")
    dead = True
