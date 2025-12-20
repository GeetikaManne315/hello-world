import random

print(" Welcome to the Dice Roller Simulator!")

while True:
    decision = input("Do you want to roll the dice? (y/n): ").lower()
    
    if decision == "y":
        dice = random.randint(1, 6)
        print(f" You rolled a {dice}!")
        
        roll_again = input("Do you want to roll again? (y/n): ").lower()
        if roll_again != "y":
            print(" Thanks for playing!")
            break
    elif decision == "n":
        print(" Maybe next time!")
        break
    else:
        print(" Please enter 'y' or 'n'.")




