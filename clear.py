#Jake Eaton

from os import system, name     #Imports system and name of os module

def clear():
    if name =='nt':     #Windows Clear Command
        _ = system('cls')

    else:   #MacOS and Linux Clear Command
        _ = system('clear')
