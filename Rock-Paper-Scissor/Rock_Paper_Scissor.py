# module for color text 
# https://pypi.org/project/termcolor/
# You can  download this module from above link
import random
from termcolor import colored, cprint

cprint(f"    Snake Water Gun GAME    ","blue","on_cyan",attrs=['bold'])
name = input("What should we call you: ")
print(f"Welcome {name} to Snake (🐍) Water (⚗) and Gun game (🔫)")
game_on = True
while game_on:
    comp_ch = random.choice(['s','w','g'])
    print("choose s for snake (🐍), w (⚗) for water and g (🔫) for gun: ",end="")
    user=input().lower()
    if (user == comp_ch):
        print("Draw")
        pass
    elif(user == 'w'):
        if (comp_ch == 'g'):
            cprint("You win","green")
        elif(comp_ch == 's'):
            cprint("You lose","red")
        print ("You win")
    elif (user=='g'):
        if (comp_ch == 's'):
            cprint("You win","green")
        elif(comp_ch == 'w'):
            cprint("You lose","red")
    elif (user=='s'):
        if (comp_ch == 'g'):
            cprint("You win","green")
        elif(comp_ch == 'w'):
            cprint("You lose","red")
    else:
        cprint("Please! Enter correct option","red")
    yOrN=input("Do you want to play again ?(Y/N)").lower()
    if yOrN=='n':
        game_on =  False
