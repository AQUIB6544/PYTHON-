import random
import os
import re

while(1<2):
    print("\n")
    print("ROCK,PAPER,SCISSOR - SHOOT !")
    Userchoise = input("ENTER YOUR CHOISE : \n 1-> for Rock : \n 2-> for paper : \n 3-> for scissor: \n 4-> for exit :")
    if (not re.match(r'\d',Userchoise)) or (len(Userchoise)!=1):
        print ("PLEASE CHOOSE A DIGIT :")
        print("1-> for Rock : \n 2-> for paper : \n 3-> for scissor: \n 4-> for exit :")
        continue

    print("YOUR CHOISE IS :"+Userchoise)
    if (Userchoise == "4"):
        print("EXITING GAME.....")
        break
choise =