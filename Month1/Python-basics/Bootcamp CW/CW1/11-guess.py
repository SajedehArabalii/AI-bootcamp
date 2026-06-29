# Guess the number game
import random

secretNumber = random.randint(1,10)

while True:                                                         
    guess = int(input("Enter number"))
    if guess ==secretNumber:
        print("Congratulations")
        break
    
    elif guess < secretNumber:
        print("Try again")
        

    
