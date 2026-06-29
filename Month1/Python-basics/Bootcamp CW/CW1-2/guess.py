import random

secretNumber = random.randint(1,5)
guess=1

while True:                                                         
    guess = int(input("Enter number"))
    if guess ==secretNumber:
        print("Congratulations")
        break
    
    elif guess < secretNumber:
        print("Try again")
        

    
