
import random

secretNumber = random.randint(1,20)
tries = 0
guess = 0

while guess != secretNumber and tries!=5:                                                        
    
    tries += 1
    guess = int(input("Guess the number: "))
    
    if guess > secretNumber:
        print("lower")
    
    elif guess < secretNumber:
        print("higher")

if guess== secretNumber:
    print(f"You have guessed the number in {tries} guesses")
else:
    print("You failed")
    
