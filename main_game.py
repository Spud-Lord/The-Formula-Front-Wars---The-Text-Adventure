#Jake Eaton

def Main_Game():
    from room import Room
    from introduction import Intro
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

    first_room = Room("The old ruins of an ancient Castle")
    first_room.set_description("You recognise the old castle as the place you lost your friend. She fell from the tallest tower. The castle has remained closed ever since.")

    second_room = Room("The frozen isle of a Supermarket")
    second_room.set_description("It has been nearly twenty years since you were here. Last time you were here, you messed with the temperature controls and caused all the products to defrost. You were banned from entering. But why do they want to know about this?\n")
    #This set defines each of the different rooms used in the game
    third_room = Room("A large office")
    third_room.set_description("You recognise this office as the office of your boss. Admiral Cora Jean of the World Space Command...\n")

    forth_room = Room("A riverside resturant")
    forth_room.set_description("One of the darkest days of your life. It was here where you were betrayed. You were just enjoying a friendly meal until you started to lose your breath. Poisoned by your trusted ally... is she the key to all this?\n")

    fifth_room = Room("The Artemis")
    fifth_room.set_description("You don't remember this... is this even your memory?")

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

        print("")

        type("You can't figure out why the people want to see this memory but you proceed")
        time.sleep(2)
        type("You walk forwards and reach the tall doors where a staff member stops you")
        time.sleep(2)
        type("'Welcome! Can I see your ticket please?'")
        time.sleep(2)
        type("You hand the staff member your ticket and you are moved over to a group")
        time.sleep(2)
        type("Soon after, you walk with the group through the doors and you are left to explore")
        time.sleep(2)
        type("You look around. Your friend is meant to be here...")
        time.sleep(2)
        type("You spot her at the top of the ruins taking selfies")
        time.sleep(2)
        type("You smile and begin to look around. How are you going to get there?")
        time.sleep(2)
        type("Will you take the left stairs or the right stairs?")
        time.sleep(2)
        type("Type Right or Left depending on which way you want to go\n")
        time.sleep(2)
        answer1 = input("")
        if answer1.lower() == "left":
            print("")
            type("The memory corrupts...")
            time.sleep(2)
            type("You can't see anything")
            time.sleep(2)
            type("Your brain and neck aches in pain...")
            time.sleep(2)
            Death()
            dead = True

        elif answer1.lower() == "right":
            print("")
            type("You head right and move up some stairs")
            time.sleep(2)
            type("You squeeze through the crowd and make your way to your friend")
            time.sleep(2)
            type("As you approach, she smiles at you")
            time.sleep(2)
            type("You walk up to her and she shows you some of the pictures she took")
            time.sleep(2)
            type("You take the phone from her to get a better look")
            time.sleep(2)
            type("Suddenly, someone turns and pushes your friend over the wall of the tallest tower...")
            time.sleep(2)
            type("You try to grab her but it is too late...")
            time.sleep(2)
            type("She didn't even scream...")
            time.sleep(2)
            type("You couldn't look as she hit and fell down the sharp rocks...")
            time.sleep(2)
            type("You turned to face the person who did it but they had already run off")
            time.sleep(2)
            type("You felt lost...")
            time.sleep(2)
            type("You leaned against the wall and broke down into tears...")
            time.sleep(2)
            type("You hold her phone close to your heart...")
            clear()

        current_room = second_room

        type("You suddenly find yourself focusing on another memory...\n")
        time.sleep(2)

        current_room.get_details()

        time.sleep(4)
        type("You realise you have a briefcase in your hand")
        time.sleep(2)
        type("You notice the freezer and walk over there")
        time.sleep(2)
        type("You spot the control panel and unscrew the cover")
        time.sleep(2)
        type("You spot the connector you need to link up to your laptop")
        time.sleep(2)
        type("Now you need to select the correct program...")
        time.sleep(2)
        type("You couldn't remember which one was working properly...")
        time.sleep(2)
        type("You could choose the Alpha which will have all the features but might not work...")
        time.sleep(2)
        type("Or you could choose the Beta program which won't have all the features but will definitely worse...")
        time.sleep(2)
        type("Type Alpha or Beta depending on which program you want to run\n")
        answer2 = input("")
        if answer2.lower() == "beta":
            type("")
            type("The memory corrupts...")
            time.sleep(2)
            type("You can't see anything")
            time.sleep(2)
            type("Your brain and neck aches in pain...")
            time.sleep(2)
            Death()
            dead = True

        elif answer2.lower() == "alpha":
            print("")
            type("You remember that the Alpha program had the features needed to crack the code of the freezer")
            time.sleep(2)
            type("You wait what feels like an eternity for the program to finish before you quickly unplug the computer, screw up the control panel and leave the supermarket")
            time.sleep(2)
            type("As you leave, you just think of the amount of food that would now go to waste")
            time.sleep(2)
            type("But it would be the supermarket who will be yelled at")
            time.sleep(2)
            type("After all, everyone will think they turned off the freezer...")
            time.sleep(2)
            type("But the most important thing is that the big corporations see that they aren't invincible...")
            clear()

        current_room = third_room

        type("Yet another memory filled your brain...")

        print("")

        current_room.get_details()

        print("")
        time.sleep(4)
        type("Why on earth do they want this memory?")
        time.sleep(2)
        type("Sitting at your boss' desk, you placed the AMTel CPU into its socket...")
        time.sleep(2)
        type("You inserted the RAM...")
        time.sleep(2)
        type("You plug in all the cables...")
        time.sleep(2)
        type("You attempt to boot the PC...")
        time.sleep(2)
        type("It does boot and you get to work")
        time.sleep(2)
        type("You quickly install your special software onto the PC")
        time.sleep(2)
        type("This would allow you to see everything your boss does")
        time.sleep(2)
        type("And your boss is the Head of the World Space Command...")
        time.sleep(2)
        type("You go to leave the room but you hear footsteps coming down the corridor outside...")
        time.sleep(2)
        type("You recognise the voice of the Admiral and begin to panic...")
        time.sleep(2)
        type("Do you hide or run??")
        time.sleep(2)
        type("Type Hide or Run depending on what you want to do...")
        print("")
        answer3 = input("")
        if answer3.lower() == "hide":
            type("")
            type("The memory corrupts...")
            time.sleep(2)
            type("You can't see anything")
            time.sleep(2)
            type("Your brain and neck aches in pain...")
            time.sleep(2)
            Death()
            dead = True

        elif answer3.lower() == "run":
            print("")
            type("You open the door and run...")
            time.sleep(2)
            type("'Take him down!' shouted a voice.'")
            mixer.music.load("Gunfire.mp3")
            mixer.music.play(1)
            type("You hear gunfire behind you...")
            time.sleep(2)
            type("You turn a corner and are met with a crowd of people")
            time.sleep(2)
            mixer.music.load("GunsReady.mp3")
            mixer.music.play(1)
            type("You are then instantly surrounded by security guards...")
            time.sleep(2)
            type("You raise your hands and get down on the ground...")
            time.sleep(4)
            clear()

        print("")
        type("'He is attempting to resist!' you hear a voice shout")
        time.sleep(2)
        type("'Find that memory now!' shouted a woman")
        time.sleep(2)
        type("'Stop resisting! It's the only way to help you!' you hear the woman shout")
        time.sleep(2)
        type("You concentrate and let the memories flow...\n")
        mixer.music.load("Battle.Of.The.Heroes.mp3")
        mixer.music.play(10)

        current_room = forth_room
        time.sleep(2)

        type("You prayed this was the last memory...\n")

        current_room.get_details()
        time.sleep(4)

        type("No")
        time.sleep(2)
        type("Why?")
        time.sleep(2)
        type("Why would they choose this memory?")
        time.sleep(2)
        type("You look at the person sitting opposite you and recognise her...")
        time.sleep(2)
        type("Emily. The woman who betrayed your heart...")
        time.sleep(2)
        type("You wanted nothing more than to lunge at her and kill her...")
        time.sleep(2)
        type("But you knew you had to let the memory flow")
        time.sleep(2)
        type("You can't change the past...")
        time.sleep(2)
        type("One of the resturant staff came up to you with their card machine to pay")
        time.sleep(2)
        type("You pay and the staff member goes to fetch some drinks")
        time.sleep(2)
        type("'On the house' he says")
        time.sleep(2)
        type("You thank him and turn to face Emily")
        time.sleep(2)
        type("You both raise your glasses and take a drink")
        time.sleep(2)
        type("Your throat suddenly burns and you clutch at your chest...")
        time.sleep(2)
        type("Emily begins to laugh...")
        time.sleep(2)
        type("You stand and attempt to walk out...")
        time.sleep(2)
        type("You collapse onto the floor...")
        time.sleep(2)
        mixer.music.load("GunsReady.mp3")
        mixer.music.play()
        type("You roll over onto your back and see dozens of guns pointing at you")
        time.sleep(2)
        type("You close your eyes...")
        clear()


        current_room = fifth_room
        time.sleep(2)
        print("")
        type("I found it! shouted a voice")
        time.sleep(2)
        type("Focus on that memory! replied a woman")
        time.sleep(2)
        type("'Last memory...'' you think to yourself...")
        time.sleep(2)
        type("You don't think you can survive much longer...")
        mixer.music.load("Battle.Of.The.Heroes.mp3")
        time.sleep(2)

        print("")

        current_room.get_details()

        time.sleep(4)
        type("Breathing calmly, you lean your head back. You don't want to see the needles enter your body.")
        time.sleep(2)
        type("Held tightly against a weird looking machine, you suddenly find yourself being rotated backwards so you are led down")
        time.sleep(2)
        type("'Test Subject 66 is ready for Preliminary Tests!'' you hear a voice call out")
        time.sleep(2)
        type("'Preparing injections.' another voice says")
        time.sleep(2)
        type("You hear the machine whirring...")
        time.sleep(2)
        type("You close your eyes and breath gently...")
        time.sleep(2)
        type("'Injecting Subject.' said one of the voices")
        time.sleep(2)
        type("You may have had injections before but these were painful")
        time.sleep(2)
        type("The pain only lasted a few seconds...")
        time.sleep(2)
        type("'Test Subject 66 accepted primary injections. Preparing secondary.' said the first voice")
        time.sleep(2)
        type("'Its not over?' you think to yourself as the machine whirred again")
        time.sleep(2)
        type("'Injecting Subject.' said the second voice")
        time.sleep(2)
        type("Before you could brace youself, you suddenly felt a burning sensation over your entire body")
        time.sleep(2)
        type("You begin to yell out in pain")
        time.sleep(2)
        type("'Secondary Injections complete!' cried the first voice")
        time.sleep(2)
        type("'Why am I still burining alive?' you thought to yourself")
        time.sleep(2)
        type("It took at least 30 seconds for the burning to stop but it felt like an eternity")
        time.sleep(2)
        type("When it finally did stop, one of the people approached you")
        time.sleep(2)
        type("'Test Subject 66 accepted Secondary Injections...")
        time.sleep(2)
        type("Breathing is stable...")
        time.sleep(2)
        type("One last injection just to finish up'")
        time.sleep(2)
        type("You keep your eyes welded shut as you wait for the final step to complete")

        clear()

        time.sleep(4)
        print("")
        type("Your eyes fly open and you scream in pain as the neural implant is removed from your neck")
        time.sleep(2)
        type("'Thank you!' said a woman's voice. The woman was running towards you.")
        time.sleep(2)
        type("You open your eyes to see the woman you saw earlier")
        time.sleep(2)
        type("'Emily!' you shout. You try to lunge at her")
        time.sleep(2)
        type("Still equipped into the machine though, you can't move and you try to catch your breath")
        time.sleep(2)
        type("'A deal is a deal. Reverse the effects and cleanse me.' you say")
        time.sleep(2)
        type("The woman nods and goes to get something. You wait for her to return")
        time.sleep(2)
        type("When she does return, she has something behind her back")
        time.sleep(2)
        type("'We have identified the scientists who experimented on you through their voices.' she said")
        time.sleep(2)
        type("'We would like to thank you for your cooperation.' she smiled")
        time.sleep(2)
        type("'Why was I on this station in the memory?' you ask")
        time.sleep(2)
        type("'It appears that it was at this very station where you became you. Therefore, we have what we need.' the woman said")
        time.sleep(2)
        type("'It is time for us to help you.'")
        time.sleep(2)
        type("You await for something to happen...")
        Victory()
        dead = True

    while dead == True:
        time.sleep(3)
        mixer.music.stop()
        type("Thank you for playing!\n")
        time.sleep(2)
        type("Remember to read the epic novel online now!")
        time.sleep(2)
        exit()
