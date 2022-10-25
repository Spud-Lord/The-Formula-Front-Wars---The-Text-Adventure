#Jake Eaton

import time
import os       #Imports time, os and pygame modules as well as the code objects from external scripts
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"       #Used to hide the PyGame welcome message
from pygame import mixer
from typing import type

def Death():         #Defines the code below as the Death object
    mixer.init()        #Initialises PyGame Mixer
    mixer.music.load("imperial_alert.mp3")      #Loads audio file
    mixer.music.play(1)     #Plays audio once
    
    type("'The memory has collapsed!' you hear a voice shout\n")      #Uses imported type object to print the letters individually
    time.sleep(2)           #Pauses code for 2 seconds
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
    type("'We can't have that. Are you going to give me what I want? Or am I going to have to take your blood?' she says\n")
    time.sleep(2)        
    type("'I will never help you...' you whisper. You don't have the energy to say much more\n")
    time.sleep(2)        
    type("'Then let me put you out of you misery. I have waited a long time to do this...' she whispered in your ear\n")
    time.sleep(2)
    type("'Wait a second...' you say weakly\n")
    mixer.music.load("PistolShot.mp3")      #Loads new audio file
    mixer.music.play()      #Plays audio once
    time.sleep(2)
    type("You don't even feel the shot before your vision ceases and your mind goes silent...\n")