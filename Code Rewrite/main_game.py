#Jake Eaton

def Main_Game():
    from room import Room
    from introduction import Intro
    from death import Death
    from victory import Victory
    from typing import type
    from clear import clear
    import time
    import os
    import sys
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    from pygame import mixer
    
    #Intro()
    
    first_room = Room("The ruins of an ancient castle\n")
    first_room.set_description("You remember this place as the place you lost your closest friend. The crime was never solved\n")
    
    second_room = Room("A large office\n")
    second_room.set_description("You remember this office as the office of Admiral Cora Jean of the World Space Command. Nothing went well for you that day\n")
    
    third_room = Room("A riverside resturant\n")
    third_room.set_description("One of the darkest days of your life. Your friend and colleague betrayed you...\n")
    
    forth_room = Room("The Artemis\n")
    forth_room.set_description("You don't remember this... or rather... you don't want to remember this...\n")
    
    mixer.init()
    mixer.music.load("Battle.Of.The.Heroes.mp3")
    mixer.music.play(10)
    
    current_room = first_room
    
    type("You find yourself focusing on a memory...\n")
    
    time.sleep(2)
    
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
    answer1 = input("\n")
    if answer1.lower() == "left":
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
        type("You turned to confront the perosn who did it but they had already run off\n")
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