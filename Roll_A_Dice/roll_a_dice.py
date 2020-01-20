# Import the random library
from random import randint
flag = True
while flag:
    print("You have rolled",randint(1,6))
    print("Would you like to roll again?")
    flag = ("y" or "yes") in input().lower() 
    # The user can input "Y" or 'y' or "yes" or "yeS". Because we are taking input and then converting it to lower before comparison. 
    # Hence, it is more user friendly!
