#Jake Eaton

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