#Jake Eaton

from os import system, name

def clear():
    if name =='nt':
        _ = system('cls')

    else:   #MacOS and Linux Clear Command
        _ = system('clear')
