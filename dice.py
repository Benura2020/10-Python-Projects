"""
Dice simulation using random module in python
Steps :
Ask user to roll or not
Roll dice
Print the dice structure
"""

import random

print(" Welcome to the Rolling Dice simulator")
print("")
print("")

user_decision = input("Do you want to roll the Dice (y/n)  ")

while user_decision.lower() == "y":
    number = random.randint(1,6)

    if number == 1:
        print("      ")
        print("      ")
        print("  0   ")
        print("      ")
        print("      ")
    elif number == 2:
        print("      ")
        print("     0")
        print("      ")
        print("0     ")
        print("      ")
    elif number == 3:
        print("      ")
        print("     0")
        print("  0   ")
        print("0     ")
        print("      ")
    elif number == 4:
        print("      ")
        print("0    0")
        print("      ")
        print("0    0")
        print("      ")
    elif number == 5:
        print("      ")
        print("0    0")
        print("  0   ")
        print("0    0")
        print("      ")
    else:
        print("      ")
        print("0    0")
        print("0    0")
        print("0    0")
        print("      ")

    user_decision = input("Do you want to roll the Dice (y/n)")

    if user_decision != "y":
        print("Quiting !!!!")
        exit()
