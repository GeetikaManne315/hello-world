import random

choice = random.randint(1,100)
guess = None
tries = 0

while (guess != choice):
    print("Guessing the number game3")
    guess = int(input("Your Guess: "))
    tries = tries + 1
    if(guess > choice):
        print("Too high")
    elif(guess < choice):
        print("Too low")
    elif(guess == choice):
        print('Sucess')
        break
    else:
        print('invalid')
        break
        
        
print("Succeded in" , tries , "tries")
    
    