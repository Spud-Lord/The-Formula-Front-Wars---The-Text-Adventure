#Jake Eaton

import time
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from typing import type

def Death():
    mixer.init()
    mixer.music.load("imperial_alert.mp3")
    mixer.music.play(1)
    
    type("'The memory has collapsed!' you hear a voice shout\n")
    time.sleep(2)
    type("Your body begins to shake violently as you resist the implant\n")
    time.sleep(2)
    type("'Release him!' a woman shouts\n")
    time.sleep(2)
    type("You scream in pain as the neural implant is ripped from your neck\n")
    time.sleep(2)
    type("You can feel your blood flowing down your neck and your vision returns\n")
    time.sleep(2)
    type("'You resisted! You changed the memory!' shouted a woman in front of you. You look up slightly and just make out the armoured woman you saw earlier\n")
    time.sleep(2)
    type("She walked up to you, grabbed her pistol and rested it on your chin, pointing it up your head...\n")
    time.sleep(2)
    type("'Let me put you out of you misery. I have waited a long time to do this...' she whispered in your ear\n")
    time.sleep(2)
    type("'Wait a second...' you say weakly\n")
    mixer.music.load("PistolShot.mp3")
    mixer.music.play()
    time.sleep(2)
    type("You don't even feel the shot before your vision ceases and your mind goes silent...\n")