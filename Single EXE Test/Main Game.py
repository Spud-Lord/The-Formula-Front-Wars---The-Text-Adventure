import time
import os
from os import system, name
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
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

def clear():
    if name =='nt':
        _ = system('cls')

def Victory():
    type("The woman pulls the device from behind her back and fires it four times")
    mixer.music.load("4xPistolShot.mp3")
    mixer.music.play()
    time.sleep(2)
    type("Your arms and legs begin to bleed and you yell out in pain")
    time.sleep(2)
    type("'We have no further use for you and we cannot risk you revealing what has happened here' said Eve")
    time.sleep(2)
    type("'Don't worry. You will forget what happened to you.' she walked away still holding the gun and you could do nothing...")
    time.sleep(2)
    type("As you slowly bleed out, you waited for the darkness to consume you...")
    time.sleep(2)
    type("'Destroy the Aorus and ensure there are no survivors' Eve called")
    time.sleep(2)
    type("'No...' you whisper. But you quickly realise there is nothing you can do for your ship and crew...")
    time.sleep(2)
    type("Eventually...")
    time.sleep(2)
    type2("You...")
    time.sleep(2)
    type2("Felt...")
    time.sleep(2)
    type2("Nothing...\n")
    dead = True


def Death():                                        #Defines all indented code as Death
    mixer.init()
    mixer.music.load("imperial_alert.mp3")          #Loads and plays the mp3 file
    mixer.music.play(1)

    type("'Critical Failure!' you hear a voice shout")
    time.sleep(2)
    type("Your mind suddenly starts to flash with memories and your body aches in pain")
    time.sleep(2)
    type("'Memory Overload! The implant is being resisted!'")
    time.sleep(2)
    type("'Release the implant!' a woman shouts")
    time.sleep(2)
    type("You shout in pain as the neural implant is removed from the back of your neck")
    time.sleep(2)
    type("You feel your blood flowing down your neck as you are set free")
    time.sleep(2)
    type("You collapse onto the cold solid floor beneath you and pant heavily")
    time.sleep(2)
    type("'You resisted. You changed the memory.' said a woman above you. You try to look up at the woman")
    time.sleep(2)
    type("'I am sorry. But unless you follow our orders, you can not live.' you can just make out a gun pointing at your head")
    time.sleep(2)
    type("You hold up your hand, shaking")
    time.sleep(2)
    type("'Wait a minute!' you say weakly. But it didn't stop the inevitable...")
    mixer.music.load("PistolShot.mp3")
    mixer.music.play()
    time.sleep(2)
    type("You don't even feel the shot...")
    time.sleep(2)
    type("You don't even feel yourself hit the ground...")
    time.sleep(2)
    type2("You feel nothing...")
    exit()                                          #Force exits the program


type("Welcome\n")
time.sleep(2)
type("Please remember this is still in Beta and may never have a full 1.0 release\n")
time.sleep(2)
type("If you spot any bugs other than those mentioned in the Release Notes, please let me know")
time.sleep(2)
type("All releases and the Source Code can be found on GitHub using the link: https://github.com/Spud-Lord/The-Formula-Front-Wars---The-Text-Adventure")
time.sleep(2)
type("Read the book as it is released at https://www.wattpad.com/story/245646734-the-formula-front-war-part-of-the-world-space")
time.sleep(2)
type("The Text Adventure will start in 10 seconds...")
mixer.init()
mixer.music.load("10SecondCountdown.mp3")                                    #Plays mp3 file
mixer.music.play(1)
time.sleep(10.5)
clear()

print("")
type("You feel youself being dragged along the floor")
time.sleep(2)
type("You can't see... are you blindfolded? Or just blind?")
time.sleep(2)
type("You hear faint shouting as you are pulled up and sat down on a chair")
time.sleep(2)
type("The shouting gets louder as you begin to wake up")
time.sleep(2)
type("You suddenly sit bolt upright and realise that you have been chained to the chair")
time.sleep(2)
type("'Hello?!' you shout. No reply...")
time.sleep(2)
type("'Anyone?' Still no reply...")
time.sleep(2)
type("'I demand to know what I am doing here!' you call out. Now there was nothing but silence...")
time.sleep(2)
type("'All will be revealed.' said a woman's voice suddenly")
time.sleep(2)
type("The blindfold is removed from your eyes and you squint with the sudden light being shined in your face.")
time.sleep(2)
type("You try to look straight ahead and see a figure standing there")
time.sleep(2)
type("'What is your name?' the woman asked")
name = input(">> ")                 #Takes an input from the user
type("'My name is "+name+"' you say")       #Prints the speech with the users name that they just inputted
time.sleep(2)
type("'Welcome to the Artemis "+name+". A science research station orbiting Jupiter.'")
time.sleep(2)
type("You manage to make out the slim figure of the dark haired woman. She looked familiar but you couldn't think properly to work it out. You look around at the massive room and see two guards holding rifles on either side of you")
time.sleep(2)
type("'I have spent enough time in space. I'd quite like to go home thank you.' you say")
time.sleep(2)
type("'But you have nothing on Earth. Why go back?' she asked")
time.sleep(2)
type("She was right... since you lost your job, you have been alone, no family, no home...")
time.sleep(2)
type("'Because there I can forget about the past and move on with life. I have done my work to expand humanity into the stars. Why can't you just let me die in peace?' you reply.")
time.sleep(2)
type("'That is why you are here.' she says")
time.sleep(2)
type("You look at her, puzzled. She leans closer to you and whispers 'Your past.'")
time.sleep(2)
type("She stood up straight once again. She clicked her fingers. You feel the chains loosen.")
time.sleep(2)
type("You leap on this advantage and drive your hand right into throat of one of the guards and took the gun from him")
time.sleep(2)
type("You point the gun at the other guard. The woman never moved as this happened")
time.sleep(2)
type("'Put the gun down!' shouted the guard. You don't move as the guard continues to tell you to put your gun down")
time.sleep(2)
type("'As you can see, you are no ordinary human' said the woman")
time.sleep(2)
type("'Somewhere in your past, something happened to you that changed your genetic makeup. It made you faster, stronger, smarter. But it also drove you insane.'")
time.sleep(2)
type("You look at the woman. 'We can help you.' she says.")
time.sleep(2)
type("You lower the gun and the other guard does the same. 'How will you help?' you ask")
time.sleep(2)
type("'We work for Admiral James Osbourne. He wants to know how you became like this. Then we will help reverse the effects and cleanse your memory of everything we make you relive.' she says.")
time.sleep(2)
type("The name Osbourne was familiar to you but you couldn't think of why. 'What will it cost?' you ask.")
time.sleep(2)
type("'It will only cost your strength and willpower to relive memories until we find the right one' she walks over to you. 'We want to help you "+name+".'")
time.sleep(2)
type("You are tempted by this offer... but the name Osbourne still rings a bell...")
time.sleep(2)
type("You realise where and immediately react. You raise the gun and point it directly at the other guard and pull the trigger. Nothing...")
time.sleep(2)
type("You feel something hit your chest and you fall backwards... never feeling yourself land... 'You are so predictable' whispered a voice")
time.sleep(2)
type("You wake up to feel yourself lying down on something metal... a table? You try to move and realise your hands are spread out and they have been clamped down along with your legs")
time.sleep(2)
type("'What is this?' you call. This time you got an immediate answer")
time.sleep(2)
type("'This is the machine that will allow us to access your memories.' the same woman said.")
time.sleep(2)
type("'I will not give up my memories to a rebellion!' you protest.")
time.sleep(2)
type("'Well this 'rebellion' as you call it simply wants to create more like you so we can win the war against Earth.")
time.sleep(2)
type("The machine began to rotate you forward until you were upright. You hear the machine moving behind you and you suddenly feel very scared")
time.sleep(2)
type("'We are going to install a neural implant. Be warned. It is going to feel odd and may even be painful.'")
time.sleep(2)
type("'Wait a minute!' you protest. But it was too late. You feel something very small enter the back of your neck and you begin to cry out in pain.")
time.sleep(2)
type("You feel blood dripping down your neck and back as something entered the wound")
time.sleep(2)
type("'Please stop this!' you cry out. The woman didn't flinch as you feel something touch around your brain.")
time.sleep(2)
type("As quick as it started, the pain stopped. Blood continued to fall however.")
time.sleep(2)
type("'Prepare for us to enter your mind.' the woman turned around and began to walk away. 'Begin memory tap process!' she called.")
time.sleep(2)
type("You close you eyes and prepare for the worst. You hear screams, shouting, crying, laughing as you are flooded with memories")
time.sleep(2)
type("'Please stop!' you shout. But it didn't stop. Until...")
time.sleep(3)
clear()


first_room = Room("The old ruins of an ancient Castle")
first_room.set_description("You recognise the old castle as the place you lost your friend. She fell from the tallest tower. The castle has remained closed ever since. But wasn't it destroyed recently?")

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
    type("You suddenly find yourself focussing on one memory...\n")

    time.sleep(2)

    current_room.get_details()

    time.sleep(4)

    print("")

    type("You can't figure out why the people want to see this memory but you proceed")
    time.sleep(2)
    type("You walk forwards and reach the tall doors where a guard stops you")
    time.sleep(2)
    type("'Welcome! Can I see your ticket please?'")
    time.sleep(2)
    type("You hand the guard your ticket and you are moved over to a group")
    time.sleep(2)
    type("Soon after, you walk with the group through the doors and you are left to explore")
    time.sleep(2)
    type("You look around. Your friend is meant to be here...")
    time.sleep(2)
    type("You spot her at the top of the ruins taking selfies")
    time.sleep(2)
    type("You smile and begin to explore. How are you going to get there?")
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
        type("You arrive next to her and she shows you some of the pictures she took")
        time.sleep(2)
        type("You took the phone from her to get a better look")
        time.sleep(2)
        type("Suddenly, someone turns and pushes your friend over the wall of the tallest tower...")
        time.sleep(2)
        type("You try to grab her but it is too late...")
        time.sleep(2)
        type("She didn't even scream...")
        time.sleep(2)
        type("You couldn't look as she hit the ground...")
        time.sleep(2)
        type("You turned to face the person who did it but they had already run off")
        time.sleep(2)
        type("You felt lost...")
        time.sleep(2)
        type("You climbed onto the wall and prepared to jump...")
        time.sleep(2)

    current_room = second_room

    type("You suddenly find yourself focussing on another memory...\n")
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
    type("You could choose the uncompiled Beta which will have all the features but will most likely be slower...")
    time.sleep(2)
    type("Or you could choose the compiled program which won't have all the features but will be much faster...")
    time.sleep(2)
    type("Type Beta or Compiled depending on which program you want to run\n")
    answer2 = input("")
    if answer2.lower() == "compiled":
        type("")
        type("The memory corrupts...")
        time.sleep(2)
        type("You can't see anything")
        time.sleep(2)
        type("Your brain and neck aches in pain...")
        time.sleep(2)
        Death()
        dead = True

    elif answer2.lower() == "beta":
        print("")
        type("You remember that the Beta program had the features needed to crack the code of the freezer")
        time.sleep(2)
        type("You wait what feels like an eternity for the program to finish before you quickly unplug the computer, screw up the control panel and leave the supermarket")
        time.sleep(2)
        type("As you leave, you just think of the amount of food that would now go to waste")
        time.sleep(2)
        type("But it would be the supermarket who will be yelled at")
        time.sleep(2)
        type("After all, everyone will think they turned off the freezer...")

    current_room = third_room

    type("Yet another memory filled your brain...")

    print("")

    current_room.get_details()

    print("")
    time.sleep(4)
    type("Why on earth do they want this memory?")
    time.sleep(2)
    type("Sitting at your desk, you placed the AMTel CPU into its socket...")
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
    type("You recognise the voice of your boss and begin to panic...")
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
    type("You look at the person sitting opposite oyou and recognise her...")
    time.sleep(2)
    type("Eve. The woman who betrayed your heart...")
    time.sleep(2)
    type("You wanted nothing more than to lunge at her and kill her...")
    time.sleep(2)
    type("But you knew you had to let the memory flow")
    time.sleep(2)
    type("You can't change the past...")
    time.sleep(2)
    type("One of the resturant staff came up to you with their card machine to pay")
    time.sleep(2)
    type("You pay and the staff member goes and fetches some drinks")
    time.sleep(2)
    type("On the house he says")
    time.sleep(2)
    type("You thank him and turn to face Eve")
    time.sleep(2)
    type("You both raise your glasses and take a drink")
    time.sleep(2)
    type("Your throat suddenly burns and you clutch at your chest...")
    time.sleep(2)
    type("Eve begins to laugh...")
    time.sleep(2)
    type("You stand and attept to walk out...")
    time.sleep(2)
    type("You collapse onto the floor...")
    time.sleep(2)
    type("You roll over onto your back and see dozens of guns pointing at you")
    time.sleep(2)
    type("You close your eyes...")


    current_room = fifth_room
    time.sleep(2)
    print("")
    type("I found it! shouted a voice")
    time.sleep(2)
    type("Focus on that memory! replied a woman")
    time.sleep(2)
    type("Last memory... you think to yourself...")
    time.sleep(2)
    type("You don't think you can survive much longer...")
    time.sleep(2)

    print("")

    current_room.get_details()

    time.sleep(4)
    type("Breathing calmly, you lean your head back to not see what is going on")
    time.sleep(2)
    type("Held tightly against a weird looking machine, you suddenly find yourself being rotated backwards so you are led down")
    time.sleep(2)
    type("Test Subject 66 is ready for Preliminary Tests you hear a voice call out")
    time.sleep(2)
    type("Preparing injections another voice says")
    time.sleep(2)
    type("You hear the machine whirring...")
    time.sleep(2)
    type("You close your eyes and breath gently...")
    time.sleep(2)
    type("Injecting Subject said one of the voices")
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
    type("Test Subject 66 completed Secondary Injections...")
    time.sleep(2)
    type("Breathing is stable...")
    time.sleep(2)
    type("One last injection just to finish up")
    time.sleep(2)
    type("You keep your eyes welded shut as you wait for the final step to complete")

    time.sleep(4)
    print("")
    type("Your eyes fly open and you scream in pain as the neural implant is removed from your neck")
    time.sleep(2)
    type("'Thank you!' said a woman's voice. The woman was running towards you.")
    time.sleep(2)
    type("You open your eyes to see the woman you saw earlier")
    time.sleep(2)
    type("'Eve!' you shout. You try to lunge at her")
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
    type("'We would like to thank you for your cooperation.'")
    time.sleep(2)
    type("'Why was I on this station in the memory?' you ask")
    time.sleep(2)
    type("'It appears that it was this very station where you became you. Therefore, we have what we need.' the woman said")
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
