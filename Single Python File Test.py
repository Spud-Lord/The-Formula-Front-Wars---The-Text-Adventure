# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 14:56:48 2023

@author: Jake Eaton
"""

from os import system, name     #Imports system and name of os module
import sys                          #Imports System and Time Modules
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"       #Used to hide the PyGame welcome message
from pygame import mixer

class Room():                       #Defines the Room Class to be called and used in the main program

  def __init__(self, room_name):    #Initializes the class with variables, names and descriptions
    self.name = room_name
    self.description = None
    self.linked_rooms = {}          #The empty lists and set variables for the required items
    self.character = []
    self.item = []

  def set_character(self, new_character):     #Defines the new character and adds it to the list
    self.character.append(new_character)

  def get_character(self):                    #Defines how the program will retrieve the character
    return self.character

  def set_description(self, room_description):    #Defines the description for the character
    self.description = room_description

  def get_description(self):                  #Defines how the program will retireve the description for the character
    return self.description

  def get_name(self):                         #Defines how the character will retrieve the character name
    return self.name

  def set_name(self, room_name):              #Defines how the name for the room is set
    self.name = room_name

  def get_item(self):                         #Defines how the program will retrieve the items in the room
    return self.item

  def set_item(self, item_name):              #Defines the items in the room
    self.item.append(item_name)

  def describe(self):                         #Defines how the program will retrieve the description of the Room
    print(self.description)

  def link_room(self, room_to_link, direction):   #Defines how the rooms are links
    self.linked_rooms[direction] = room_to_link

  def get_details(self):                      #Defines how the program retrieves the details of the room and how it is printed on screen
    print(self.name)
    print("-----------------------------------------------------------")
    print(self.description)
    for direction in self.linked_rooms:
      room = self.linked_rooms[direction]
      print("The " + room.get_name() + " is " + direction)

  def move(self, direction):                  #Defines how the user will move between rooms
    if direction in self.linked_rooms:
      return self.linked_rooms[direction]
    else:
      print("You can't go that way")          #Runs the following code if the User types in something that isn't a room
      return self

def clear():
    if name =='nt':     #Windows Clear Command
        _ = system('cls')

    else:   #MacOS and Linux Clear Command
        _ = system('clear')
        
def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()          #This def will print strings in this way. When type is used instead of print, the program will now know to print each character separately wth a small time gap inbetween
        time.sleep(0.04)
    sys.stdout.write("\n")

def type2(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()          #This def will print strings in this way. When type is used instead of print, the program will now know to print each character separately wth a small time gap inbetween
        time.sleep(0.75)
    sys.stdout.write("\n")
    
def Victory():         #Defines the code below as the Death object
    print("")
    type("Your eyes fly open and you scream in pain as the neural implant is removed from your neck\n")      #Uses imported type object to print the letters individually
    time.sleep(2)           #Pauses code for 2 seconds
    type("'Did we get everything?' said a woman's voice\n")
    time.sleep(2)
    type("'Yes!' replied another voice\n")
    time.sleep(2)
    type("You open your eyes to see the armoured woman standing in front of you\n")
    time.sleep(2)
    type("She removed her helmet and her dark hair drops down as her face is revealed\n")
    time.sleep(2)
    type("You try to lunge at the woman as her identity is finally revealed...\n")
    time.sleep(2)
    type("'Emily!' you shout\n")
    time.sleep(2)
    type("Emily smiled in return\n")
    time.sleep(2)
    type("'I know it has been a while.' she said calmly. 'Took me a while to find you. We needed your memory to find out what augmentations you had so we can refine the procedure and create soldiers like you. But better.'\n")
    time.sleep(2)
    type("'So what happens now?' you ask. 'Going to throw me in a cell somewhere?'\n")
    time.sleep(2)
    type("'No.' she whispers. 'I have something better in store for you.' She took a few steps back\n")
    time.sleep(2)
    type("Moving like lightning, Emily grabbed her pistol and shot it four times\n")
    time.sleep(2)
    mixer.music.load("4xPistolShot.mp3")      #Loads new audio file
    mixer.music.play()      #Plays audio once
    time.sleep(2)
    type("Your arms and legs begin to bleed as you yell out in pain\n")
    time.sleep(2)
    type("'You'll recognise this method. After all, you taught me it.' she says\n")
    time.sleep(2)
    type("Emily turns and starts to walk away. 'Start analysing the memory and dispose of his body.' she commanded\n")
    time.sleep(2)
    type("You watch Emily walk off as your vision begins to blur\n")
    time.sleep(2)
    type("You close your eyes as the pain begins to subside...\n")
    time.sleep(2)
    type("Your mind finally falls silent...")
    time.sleep(2)
    
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

def Intro():         #Defines the code below as the Intro object
    type("As you start to wake up, you hear shouting and movement all around you\n")      #Uses imported type object to print the letters individually
    time.sleep(2)           #Pauses code for 2 seconds
    type("You open your eyes and see a blurry haze of lights\n")
    time.sleep(2)
    type("You feel a pain in your head as your eyes start to focus\n")
    time.sleep(2)
    type("You look around and you realise the gravity of the situation\n")
    time.sleep(2)    
    type("You sit bolt upright, noticing that you have been chained to a chair\n")
    time.sleep(2)
    type("As your senses return, your enhanced eyesight picks up details all over the room\n")
    time.sleep(2)    
    type("You spot oxygen regulators in the corners of the room which told you that you were in space... a space station of some kind? Or a ship?\n")
    time.sleep(2)
    type("You see cables hanging from the ceiling and all around you were people at computers talking and tapping away\n")
    time.sleep(2)
    type("Before you could notice anything else, someone walks in front of you\n")
    time.sleep(2)
    type("You look at the figure and notice that they are wearing a suit of armour\n")
    time.sleep(2)
    type("The black helmet covered the face of this mysterious figure\n")
    time.sleep(2)
    type("As you look down, you notice a pistol magnetically attached to their waist\n")
    time.sleep(2)
    type("'What is your name?' the woman asked\n")
    name = input(">> ")     #Used to take user input
    print("")
    type("'My name is "+name+"' you say\n")
    time.sleep(2)
    type("'I am sure you have lots of questions "+name+" so I will get right into it' the woman replies\n")
    time.sleep(2)
    type("She takes a step back. 'Welcome to the Artemis. A science research station orbiting Jupiter.'\n")
    time.sleep(2)
    type("You take another look around. The place looked like it hadn't been used for years\n")
    time.sleep(2)
    type("'Care to tell me why I am here?' you say\n")
    time.sleep(2)
    type("'You have something we want.' the woman replied\n")
    time.sleep(2)
    type("You look directly into her visor. Her voice is familiar...\n")
    time.sleep(2)
    type("'You're not an ordinary human are you?' she asked\n")
    time.sleep(2)
    type("She was right. But how did she know? You were part of a highly classified experience which turned you into a very different person...\n")
    time.sleep(2)
    type("You became stronger, faster, more agile, more alert, more intelligent. You became a super soldier. But you left that life behind years ago after losing your entire 3,000 strong squad in one battle. A battle in which only you survived...\n")
    time.sleep(2)
    type("'You're mind isn't the same as it once was is it?' she says\n")
    time.sleep(2)    
    type("You stay silent. She was right again. The PTSD had haunted you for years. You keep having visions, hallucinations. Your training had taught you that violence was always the first response...\n")
    time.sleep(2)    
    type("You have been a dangerous person for a while. So much so that you left your entire life behind to escape and try and move on from the past\n")
    time.sleep(2)    
    type("'We are here on behalf of Admiral James Osbourne. You are here to give us access to your memories so we can see what happened to you. That way, we can help you.'\n")
    time.sleep(2)    
    type("'And in return?' you ask\n")
    time.sleep(2)    
    type("'As I said, we want access to your memories. Afterwards, if you want, we will accept help in training our soldiers to fight in our war.'\n")
    time.sleep(2)    
    type("All the pieces fell into place and you had to respond\n")
    time.sleep(2)    
    type("You weren't going to help the Formula Front. You rip the chains apart and run the woman\n")
    time.sleep(2)    
    type("She reacted like lightning and shot you with something mounted on her wrist\n")
    time.sleep(2)    
    type("You fell to the floor instantly and the world went blank...\n")
    time.sleep(4)
    type("When you finally woke up, you felt yourself lying on something metal. You try to move but find yourself clamped down\n")
    time.sleep(2)        
    type("'The clamps are made with warship grade titanium alloy. So I wouldn't try to break it' called a voice\n")
    time.sleep(2)    
    type("'What do you really want? If you wanted my augmentations you would just my blood. Why am I really here?' you shout back\n")
    time.sleep(2)    
    type("The woman laughs and walks up to you\n")
    time.sleep(2)    
    type("'You've figured it out then! Yes we could take your blood and try to reverse engineer it. Or... we can use you as a test subject for this machine. I am defying orders by doing this so you better make it worth my time!' she responded\n")
    time.sleep(2)    
    type("You will not get anything from me! I'll die before I tell you anything!' you shout back\n")
    time.sleep(2)    
    type("'Don't worry! We aren't going to interrogate you. This machine will force you to give us what we want' she replied\n")
    time.sleep(2)    
    type("Suddenly, you hear something whirring behind you\n")
    time.sleep(2)    
    type("You feel a drill spin its way into the back of your neck and you begin to cry out in pain\n")
    time.sleep(2)    
    type("The drill continues to spin as you fell blood dripping out\n")
    time.sleep(2)    
    type("You feel something exit the tip of the drill and begin to move around your brain\n")
    time.sleep(2)
    type("As the drill stopped spinning, the pain subsided, but blood continued to fall\n")
    time.sleep(2)        
    type("The neural implant will give us access to your mind. You will have to repeat some of your memories in the exact same way that they happened to build up the connection while we search for what we want.' the woman said\n")
    time.sleep(2)        
    type("Repeat your memories? What does this machine do?\n")
    time.sleep(2)        
    type("'Prepare for us to enter your mind.' the woman called\n")
    time.sleep(2)        
    type("You hear screams, shouting, crying, laughing...\n")
    time.sleep(2)        
    type("You begin to see your memories all at at once\n")
    time.sleep(2)        
    type("Your neck and brain begins to burn and you cry out in pain...\n")
    time.sleep(2)        
    type("You go silent...\n")
    time.sleep(3) 
    clear()     #Clears terminal using imported clear object    
    
def Main_Game():        #Defines the code below as the Main_Game object
    from room import Room
    from introduction import Intro      #Imports code objects from other scripts
    from death import Death
    from victory import Victory
    from typing import type
    from clear import clear
    import time
    import os       #Imports time, os and pygame modules
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"       #Used to hide the PyGame welcome message
    from pygame import mixer        #Specifies that only mixer will be imported from pygame
    
    Intro()     #Runs Intro object from other script
    
    first_room = Room("The ruins of an ancient castle\n")
    first_room.set_description("You remember this place as the place you lost your closest friend. The crime was never solved\n")
    
    second_room = Room("A large office\n")
    second_room.set_description("You remember this office as the office of Admiral Cora Jean of the World Space Command. Nothing went well for you that day\n")
    #This code uses the Room object to define four different rooms and assign them a name and description to be called later
    third_room = Room("A riverside restaurant\n")
    third_room.set_description("One of the darkest days of your life. Your friend and colleague betrayed you...\n")
    
    forth_room = Room("The Artemis\n")
    forth_room.set_description("You don't remember this... or rather... you don't want to remember this...\n")
    
    mixer.init()        #Intialises mixer from PyGame
    mixer.music.load("Battle.Of.The.Heroes.mp3")        #Loads music file
    mixer.music.play(10)        #Plays the music file 10 times
    
    current_room = first_room       #Sets the current room to be the first room defined above
    
    type("You find yourself focusing on a memory...\n")     #Uses imported type object to print the letters individually
    
    time.sleep(2)       #Pauses code for 2 seconds
    
    current_room.get_details()
    
    time.sleep(4)
    
    type("You can't figure out why the people want to see this memory but you proceed\n")
    time.sleep(2)
    type("You walk forwards and reach the tall door where a staff member stops you\n")
    time.sleep(2)
    type("'Welcome! Can I see your ticket please?' they said\n")
    time.sleep(2)
    type("You hand the staff member your ticket and move over to a group waiting to head inside\n")
    time.sleep(2)
    type("Soon, the door opened and you walked in with the group\n")
    time.sleep(2)
    type("Left alone to explore, you look around and spot your friend at the top of the ruins taking pictures\n")
    time.sleep(2)
    type("You smile and begin to look around. How are you going to get to her?\n")
    time.sleep(2)
    type("Will you take the damaged left stairs or the right stairs?\n")
    time.sleep(2)
    type("Type Right or Left depending on which way you want to go")
    time.sleep(2)
    answer1 = input("\n")       #Used to take user input on a new line
    if answer1.lower() == "left":
        print("")
        type("The memory corrupts...\n")
        time.sleep(2)
        type("You try to look around but realise you're blind\n")
        time.sleep(2)
        type("Your brain and neck ache in pain...\n")
        time.sleep(2)
        clear()     #Clears terminal using imported clear object
        Death()     #Runs Death object from other script
        time.sleep(3)
        mixer.music.stop()      #Stops music playing
        clear()
        type("Thank you for playing!\n")
        time.sleep(2)
        exit()      #Exits game using imported exit object
        
    elif answer1.lower() == "right":
        print("")
        type("You head right and move up the stairs\n")
        time.sleep(2)
        type("You squeeze through the crowd and make your way to your friend\n")
        time.sleep(2)
        type("As you approach, she smiles and greets you\n")
        time.sleep(2)
        type("You walk up to her and she shows you some of the pictures she took\n")
        time.sleep(2)
        type("You take the phone from her to get a better look\n")
        time.sleep(2)
        type("Suddenly, someone turns and pushes your friend over the wall...\n")
        time.sleep(2)
        type("You try to grab her but it is too late...\n")
        time.sleep(2)
        type("She didn't even scream...\n")
        time.sleep(2)
        type("You couldn't look as she hit the sharp rocks...\n")
        time.sleep(2)
        type("You turned to confront the person who did it but they had already run off\n")
        time.sleep(2)
        type("You felt lost...\n")
        time.sleep(2)
        type("You leaned against the wall and broke down into tears...\n")
        time.sleep(2)
        type("You looked over and saw her body impaled on the rocks\n")
        time.sleep(2)
        type("You begin to shake violently and fall to the floor\n")
        time.sleep(2)
        type("You hold her phone close to your heart...\n")
        time.sleep(2)
        clear()
        
    current_room = second_room
    
    type("Another memory fills your mind...\n")
    time.sleep(2)
    
    current_room.get_details()
    
    print("")
    time.sleep(4)
    type("Sitting at your boss' desk, you tapped on her desk and it lit up\n")
    time.sleep(2)
    type("You began tapping through her files, searching for what you wanted to see\n")
    time.sleep(2)
    type("Eventually you saw what you wanted. The file. Your file. You tap on it and it opens...\n")
    time.sleep(2)
    type("You stared at your picture for a while before sifting through the digital contents\n")
    time.sleep(2)
    type("Horrified by what you read, you plugged in a USB drive and quickly move the file to it\n")
    time.sleep(2)
    type("It quickly transferred and you removed the drive\n")
    time.sleep(2)
    type("You walk towards the door and attach the drive to a chain on your neck\n")
    time.sleep(2)
    type("Just as you reach for the door handle however, you hear footsteps and the Admiral's voice coming closer...\n")
    time.sleep(2)
    type("You panic and wonder what to do\n")
    time.sleep(2)
    type("Do you hide or run?\n")
    time.sleep(2)
    type("Type Hide or Run depending on what you want to do...")
    answer2 = input("\n")
    if answer2.lower() == "hide":
        print("")
        type("The memory corrupts...\n")
        time.sleep(2)
        type("You try to look around but realise you're blind\n")
        time.sleep(2)
        type("Your brain and neck ache in pain...\n")
        time.sleep(2)
        clear()
        Death()
        time.sleep(3)
        mixer.music.stop()
        clear()
        type("Thank you for playing!\n")
        time.sleep(2)
        exit()
        
    elif answer2.lower() == "run":
        print("")
        type("You open the door and run...\n")
        time.sleep(2)
        type("'Stop! Someone stop him!' shouted a voice\n")
        mixer.music.load("Gunfire.mp3")
        mixer.music.play(1)
        type("You hear gunfire from security guards behind you ...\n")
        time.sleep(2)
        mixer.music.stop()
        type("You turn a corner and hit another guard\n")
        time.sleep(2)
        type("You are quickly surrounded by more guards\n")
        time.sleep(2)
        mixer.music.load("GunsReady3.mp3")
        mixer.music.play(1)
        type("They raise their guns and you raise your hands\n")
        time.sleep(2)
        type("You are pushed onto the floor and become face to face with the Admiral...\n")
        time.sleep(4)
        clear()
        
    print("")
    type("'We are almost there! The connection is stable. We need to strengthen it somehow.' you hear a voice shout\n")
    time.sleep(2)
    type("'Give him the memory of me. That will open him up.' you hear a woman say\n")
    time.sleep(2)
    type("Memory of her? You don't know her... do you?\n")
    time.sleep(2)
    type("You concentrate and let the memories flow...\n")
    mixer.music.load("Battle.Of.The.Heroes.mp3")
    mixer.music.play(10)
    time.sleep(2)
    
    clear()
    
    current_room = third_room
        
    print("")
    
    current_room.get_details()
    time.sleep(4)

    print("")
    type("No...\n")
    time.sleep(2)
    type("It can't be...\n")
    time.sleep(2)
    type("You look at the person sitting opposite you and recognise her instantly...\n")
    time.sleep(2)
    type("Emily. The woman who betrayed your heart...\n")
    time.sleep(2)
    type("You wanted nothing more than to lunge at her and kill her...\n")
    time.sleep(2)
    type("But you knew you had to let the memory flow\n")
    time.sleep(2)
    type("You can't change the past\n")
    time.sleep(2)
    type("But you intend to do something about it in the present\n")
    time.sleep(2)
    type("One of the restaurant staff came up to you with two glasses filled with drink\n")
    time.sleep(2)
    type("'On the house.' he says\n")
    time.sleep(2)
    type("You thank him and turn to face Emily\n")
    time.sleep(2)
    type("She raises her glass\n")
    time.sleep(2)
    type("Do you raise your glass and join her?\n")
    time.sleep(2)
    type("Type Yes or No depending on what you want to do...")
    answer3 = input("\n")
    if answer3.lower() == "no":
        print("")
        type("The memory corrupts...\n")
        time.sleep(2)
        type("You try to look around but realise you're blind\n")
        time.sleep(2)
        type("Your brain and neck ache in pain...\n")
        time.sleep(2)
        clear()
        Death()
        time.sleep(3)
        mixer.music.stop()
        clear()
        type("Thank you for playing!\n")
        time.sleep(2)
        exit()
        
    if answer3.lower() == "yes":
        print("")
        type("You raise your glass, smile and take a drink with her\n")
        time.sleep(2)
        type("Your throat suddenly burns and you clutch at your chest...\n")
        time.sleep(2)
        type("Emily just smiles at you...\n")
        time.sleep(2)
        type("You stand and attempt to walk out...\n")
        time.sleep(2)
        type("You collapse onto the floor...\n")
        time.sleep(2)
        mixer.music.load("GunsReady.mp3")
        mixer.music.play()
        type("You roll over onto your back and see guns pointing at you\n")
        time.sleep(2)
        type("You close your eyes and wait for your life to end...\n")
        clear()
        
    time.sleep(2)
    print("")
    type("'I found it!' shouted a voice\n")
    time.sleep(2)
    type("'Focus on that memory! Extract it now!' replied a woman\n")
    time.sleep(2)
    type("You don't think you can survive much longer as you plunge into what you hope is the last memory...\n")
    time.sleep(2)
    
    clear()
    
    current_room = forth_room
    
    print("")
    
    current_room.get_details()
    
    print("")
    time.sleep(4)
    type("Breathing calmly, you wait to see what happens next\n")
    time.sleep(2)
    type("Held tightly against a weird looking machine, you suddenly find yourself being rotated backwards so you are laying down\n")
    time.sleep(2)
    type("'Test Subject 66 is ready for primary injections!' you hear a voice call out\n")
    time.sleep(2)
    type("'Injections ready.' another voice says\n")
    time.sleep(2)
    type("You hear the machine whirring and close your eyes, you breathing becoming heavier\n")
    time.sleep(2)
    type("'Injecting subject.' said another voice\n")
    time.sleep(2)
    type("The pain was intense but it only lasted a few seconds\n")
    time.sleep(2)
    type("'Test Subject 66 is ready for secondary injections.' said the first voice\n")
    time.sleep(2)
    type("Your breathing become faster and shallower as the you brace for more pain\n")
    time.sleep(2)
    type("'Injecting subject.' said the second voice\n")
    time.sleep(2)
    type("Before you could brace yourself, you suddenly felt a burning sensation over your entire body\n")
    time.sleep(2)
    type("You begin to yell out in pain\n")
    time.sleep(2)
    type("'Secondary injections complete!' said the first voice\n")
    time.sleep(2)
    type("All you could feel was pain all throughout your body and you continue to cry out in pain\n")
    time.sleep(2)
    type("After what felt like an eternity, the pain stopped just as sudden as it arrived\n")
    time.sleep(2)
    type("'Test Subject 66 has accepted secondary injections' a voice says\n")
    time.sleep(2)
    type("Breathing is stabilising\n")
    time.sleep(2)
    type("'Move him to the aftercare division.' said a new voice\n")
    time.sleep(2)
    type("You keep your eyes shut as you feel yourself being moved\n")
    time.sleep(2)
    
    clear()
    
    Victory()       #Runs Victory object from other script
    clear()
    type("Thank you for playing!\n")
    time.sleep(2)
    exit()
    
type("Welcome!\n")      #Uses imported type object to print the letters individually
time.sleep(2)           #Pauses code for 2 seconds
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