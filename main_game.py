#Jake Eaton

def Main_Game():
    from room import Room
    from introductionv2 import Intro
    from death import Death                                                         #Imports Room, Intro, Death, Victory, type, type2 and Main_Menu Definitions
    from victory import Victory
    from typing import type, type2
    from clear import clear
    import time
    import os
    import sys
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    from pygame import mixer

    Intro()

    first_room = Room("The old ruins of an ancient Castle\n")
    first_room.set_description("You recognise the old castle as the place you lost your friend. She fell from the tallest tower. The castle has remained closed ever since.\n")

    second_room = Room("The frozen isle of a Supermarket\n")
    second_room.set_description("It has been nearly twenty years since you were here. Last time you were here, you messed with the temperature controls and caused all the products to defrost. You were banned from entering any of their stores again. But why do they want to know about this?\n")
    #This set defines each of the different rooms used in the game
    third_room = Room("A large office\n")
    third_room.set_description("You recognise this office as the office of your boss. Admiral Cora Jean of the World Space Command...\n")

    forth_room = Room("A riverside resturant\n")
    forth_room.set_description("One of the darkest days of your life. It was here where you were betrayed. You were just enjoying a friendly meal until you started to lose your breath. Poisoned by your trusted ally... is she the key to all this?\n")

    fifth_room = Room("The Artemis\n")
    fifth_room.set_description("You don't remember this... is this even your memory?\n")

    mixer.init()
    mixer.music.load("Battle.Of.The.Heroes.mp3")                                    #Plays mp3 file
    mixer.music.play(10)

    current_room = first_room                                                       #Sets the current room as the first room
    inventory = []

    dead = False                                                                    #Sets dead state to be False

    while dead == False:
        type("You suddenly find yourself focusing on one memory...\n")

        time.sleep(2)

        current_room.get_details()

        time.sleep(4)

        type("You can't figure out why the people want to see this memory but you proceed\n")
        time.sleep(2)
        type("You walk forwards and reach the tall doors where a staff member stops you\n")
        time.sleep(2)
        type("'Welcome! Can I see your ticket please?'\n")
        time.sleep(2)
        type("You hand the staff member your ticket and you are moved over to a group\n")
        time.sleep(2)
        type("Soon after, you walk with the group through the doors and you are left to explore\n")
        time.sleep(2)
        type("You look around. Your friend is meant to be here...\n")
        time.sleep(2)
        type("You spot her at the top of the ruins taking selfies\n")
        time.sleep(2)
        type("You smile and begin to look around. How are you going to get there?\n")
        time.sleep(2)
        type("Will you take the left stairs or the right stairs?\n")
        time.sleep(2)
        type("Type Right or Left depending on which way you want to go")
        time.sleep(2)
        answer1 = input("\n")
        if answer1.lower() == "left":
            print("")
            type("The memory corrupts...\n")
            time.sleep(2)
            type("You can't see anything\n")
            time.sleep(2)
            type("Your brain and neck aches in pain...\n")
            time.sleep(2)
            Death()
            dead = True

        elif answer1.lower() == "right":
            print("")
            type("You head right and move up some stairs\n")
            time.sleep(2)
            type("You squeeze through the crowd and make your way to your friend\n")
            time.sleep(2)
            type("As you approach, she smiles at you\n")
            time.sleep(2)
            type("You walk up to her and she shows you some of the pictures she took\n")
            time.sleep(2)
            type("You take the phone from her to get a better look\n")
            time.sleep(2)
            type("Suddenly, someone turns and pushes your friend over the wall of the tallest tower...\n")
            time.sleep(2)
            type("You try to grab her but it is too late...\n")
            time.sleep(2)
            type("She didn't even scream...\n")
            time.sleep(2)
            type("You couldn't look as she hit and fell down the sharp rocks...\n")
            time.sleep(2)
            type("You turned to face the person who did it but they had already run off\n")
            time.sleep(2)
            type("You felt lost...\n")
            time.sleep(2)
            type("You leaned against the wall and broke down into tears...\n")
            time.sleep(2)
            type("You hold her phone close to your heart...\n")
            clear()

        current_room = second_room

        type("You suddenly find yourself focusing on another memory...\n")
        time.sleep(2)

        current_room.get_details()

        time.sleep(4)
        type("You realise you have a briefcase in your hand\n")
        time.sleep(2)
        type("You notice the freezer and walk over there\n")
        time.sleep(2)
        type("You spot the control panel and unscrew the cover\n")
        time.sleep(2)
        type("You spot the connector you need to link up to your laptop\n")
        time.sleep(2)
        type("Now you need to select the correct program...\n")
        time.sleep(2)
        type("You couldn't remember which one was working properly...\n")
        time.sleep(2)
        type("You could choose the Alpha which will have all the features but might not work...\n")
        time.sleep(2)
        type("Or you could choose the Beta program which won't have all the features but will definitely worse...\n")
        time.sleep(2)
        type("Type Alpha or Beta depending on which program you want to run")
        answer2 = input("\n")
        if answer2.lower() == "beta":
            type("\n")
            type("The memory corrupts...\n")
            time.sleep(2)
            type("You can't see anything\n")
            time.sleep(2)
            type("Your brain and neck aches in pain...\n")
            time.sleep(2)
            Death()
            dead = True

        elif answer2.lower() == "alpha":
            print("")
            type("You remember that the Alpha program had the features needed to crack the code of the freezer\n")
            time.sleep(2)
            type("You wait what feels like an eternity for the program to finish before you quickly unplug the computer, screw up the control panel and leave the supermarket\n")
            time.sleep(2)
            type("As you leave, you just think of the amount of food that would now go to waste\n")
            time.sleep(2)
            type("But it would be the supermarket who will be yelled at\n")
            time.sleep(2)
            type("After all, everyone will think they turned off the freezer...\n")
            time.sleep(2)
            type("But the most important thing is that the big corporations see that they aren't invincible...\n")
            clear()

        current_room = third_room

        type("Yet another memory filled your brain...\n")

        print("")

        current_room.get_details()

        print("")
        time.sleep(4)
        type("Why on earth do they want this memory?\n")
        time.sleep(2)
        type("Sitting at your boss' desk, you placed the AMTel CPU into its socket...\n")
        time.sleep(2)
        type("You inserted the RAM...\n")
        time.sleep(2)
        type("You plug in all the cables...\n")
        time.sleep(2)
        type("You attempt to boot the PC...\n")
        time.sleep(2)
        type("It does boot and you get to work\n")
        time.sleep(2)
        type("You quickly install your special software onto the PC\n")
        time.sleep(2)
        type("This would allow you to see everything your boss does\n")
        time.sleep(2)
        type("And your boss is the Head of the World Space Command...\n")
        time.sleep(2)
        type("You go to leave the room but you hear footsteps coming down the corridor outside...\n")
        time.sleep(2)
        type("You recognise the voice of the Admiral and begin to panic...\n")
        time.sleep(2)
        type("Do you hide or run??\n")
        time.sleep(2)
        type("Type Hide or Run depending on what you want to do...")
        answer3 = input("\n")
        if answer3.lower() == "hide":
            type("\n")
            type("The memory corrupts...\n")
            time.sleep(2)
            type("You can't see anything\n")
            time.sleep(2)
            type("Your brain and neck aches in pain...\n")
            time.sleep(2)
            Death()
            dead = True

        elif answer3.lower() == "run":
            print("")
            type("You open the door and run...\n")
            time.sleep(2)
            type("'Take him down!' shouted a voice.'\n")
            mixer.music.load("Gunfire.mp3")
            mixer.music.play(1)
            type("You hear gunfire behind you...\n")
            time.sleep(2)
            type("You turn a corner and are met with a crowd of people\n")
            time.sleep(2)
            mixer.music.load("GunsReady.mp3")
            mixer.music.play(1)
            type("You are then instantly surrounded by security guards...\n")
            time.sleep(2)
            type("You raise your hands and get down on the ground...\n")
            time.sleep(4)
            clear()

        print("")
        type("'He is attempting to resist!' you hear a voice shout\n")
        time.sleep(2)
        type("'Find that memory now!' shouted a woman\n")
        time.sleep(2)
        type("'Stop resisting! You'll die if you don't let us in!' you hear the woman shout\n")
        time.sleep(2)
        type("You concentrate and let the memories flow...\n")
        mixer.music.load("Battle.Of.The.Heroes.mp3")
        mixer.music.play(10)

        current_room = forth_room
        time.sleep(2)
        
        clear()
        
        type("You prayed this was the last memory...\n")

        current_room.get_details()
        time.sleep(4)

        type("No\n")
        time.sleep(2)
        type("Why?\n")
        time.sleep(2)
        type("Why would they choose this memory?\n")
        time.sleep(2)
        type("You look at the person sitting opposite you and recognise her...\n")
        time.sleep(2)
        type("Emily. The woman who betrayed your heart...\n")
        time.sleep(2)
        type("You wanted nothing more than to lunge at her and kill her...\n")
        time.sleep(2)
        type("But you knew you had to let the memory flow\n")
        time.sleep(2)
        type("You can't change the past...\n")
        time.sleep(2)
        type("One of the resturant staff came up to you with their card machine to pay\n")
        time.sleep(2)
        type("You pay and the staff member goes to fetch some drinks\n")
        time.sleep(2)
        type("'On the house' he says\n")
        time.sleep(2)
        type("You thank him and turn to face Emily\n")
        time.sleep(2)
        type("You both raise your glasses and take a drink\n")
        time.sleep(2)
        type("Your throat suddenly burns and you clutch at your chest...\n")
        time.sleep(2)
        type("Emily begins to laugh...\n")
        time.sleep(2)
        type("You stand and attempt to walk out...\n")
        time.sleep(2)
        type("You collapse onto the floor...\n")
        time.sleep(2)
        mixer.music.load("GunsReady.mp3")
        mixer.music.play()
        type("You roll over onto your back and see dozens of guns pointing at you\n")
        time.sleep(2)
        type("You close your eyes...\n")
        clear()


        current_room = fifth_room
        time.sleep(2)
        print("")
        type("I found it! shouted a voice\n")
        time.sleep(2)
        type("Focus on that memory! replied a woman\n")
        time.sleep(2)
        type("'Last memory...' you think to yourself...\n")
        time.sleep(2)
        type("You don't think you can survive much longer...\n")
        mixer.music.load("Battle.Of.The.Heroes.mp3")
        time.sleep(2)

        clear()

        current_room.get_details()

        time.sleep(4)
        type("Breathing calmly, you lean your head back. You don't want to see the needles enter your body.\n")
        time.sleep(2)
        type("Held tightly against a weird looking machine, you suddenly find yourself being rotated backwards so you are led down\n")
        time.sleep(2)
        type("'Test Subject 66 is ready for Preliminary Tests!'' you hear a voice call out\n")
        time.sleep(2)
        type("'Preparing injections.' another voice says\n")
        time.sleep(2)
        type("You hear the machine whirring...\n")
        time.sleep(2)
        type("You close your eyes and breath gently...\n")
        time.sleep(2)
        type("'Injecting Subject.' said one of the voices\n")
        time.sleep(2)
        type("You may have had injections before but these were painful\n")
        time.sleep(2)
        type("The pain only lasted a few seconds...\n")
        time.sleep(2)
        type("'Test Subject 66 accepted primary injections. Preparing secondary.' said the first voice\n")
        time.sleep(2)
        type("'Its not over?' you think to yourself as the machine whirred again\n")
        time.sleep(2)
        type("'Injecting Subject.' said the second voice\n")
        time.sleep(2)
        type("Before you could brace youself, you suddenly felt a burning sensation over your entire body\n")
        time.sleep(2)
        type("You begin to yell out in pain\n")
        time.sleep(2)
        type("'Secondary Injections complete!' cried the first voice\n")
        time.sleep(2)
        type("'Why am I still burining alive?' you thought to yourself\n")
        time.sleep(2)
        type("It took at least 30 seconds for the burning to stop but it felt like an eternity\n")
        time.sleep(2)
        type("When it finally did stop, one of the people approached you\n")
        time.sleep(2)
        type("'Test Subject 66 accepted Secondary Injections...\n")
        time.sleep(2)
        type("Breathing is stable...\n")
        time.sleep(2)
        type("'One last injection just to finish up'\n")
        time.sleep(2)
        type("You keep your eyes welded shut as you wait for the final step to complete\n")

        clear()

        time.sleep(4)
        print("")
        type("Your eyes fly open and you scream in pain as the neural implant is removed from your neck\n")
        time.sleep(2)
        type("'Did we get everything?' said a woman's voice\n")
        time.sleep(2)
        type("'Yes!' shouted another voice")
        time.sleep(2)
        type("You open your eyes to see the armoured woman standing in front of you.")
        time.sleep(2)
        type("She removed her helmet and her dark hair was revealed")
        time.sleep(2)
        type("You try to lunge at the woman. 'Emily!' you shout")
        time.sleep(2)
        type("Emily smiled at you")
        time.sleep(2)
        type("'I know it has been a while.' she spoke calmly. 'As you know, you're augmentations were far superior to mine. Now we have the memory, we have what we need to refine your design and create soldiers like you. But better.'")
        time.sleep(2)
        type("'So what happens now?' you ask. 'Going to throw me in a cell somewhere?'")
        time.sleep(2)
        type("Emily smiled again")
        time.sleep(2)
        type("'No.' she whispers")
        time.sleep(2)
        Victory()
        dead = True

    while dead == True:
        time.sleep(3)
        mixer.music.stop()
        type("Thank you for playing!\n")
        time.sleep(2)
        exit()
