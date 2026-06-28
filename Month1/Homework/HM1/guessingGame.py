#5 guessing chances
#if guess < num print "bigger"
#if guess > num print "smaller"
#if guess == num print "You got it."
#Only 5 tries or you will lose
import random

def main():
    # Declaring variables
    high = 10
    low = 1
    rounds = 5
    tries = 0

    # Instruction
    print("Let's play guess the number.\nI choose and you guess\nYou have 5 tries")

    #make a random number
    num = random.randint(low,high)

    # Make a loop of 5 tries
    while tries<rounds:
        #Get number from user
        guess = get_guess(low, high)
        tries += 1
        #compare the numbers
        if compare(num, guess):
            print(f"You got it in {tries} tries")
            return
    print(f"You lost! The number was {num}.")


# Gets the guess and makes sure it is valid
def get_guess(low,high):
            while True:
                try:
                    guess = int(input("Enter a number: "))
                    if low <= guess <= high:
                        return guess
                    else:
                        print("Number should be between 1 and 100: ")
                except ValueError:
                    print("Please Enter a valid number between 1 and 100.")


# Compare guess with the secret number and print a hint.
def compare(num, guess):
    if guess < num:
        print("Higher")
        return False
    elif guess > num:
        print("Lower")
        return False
    else:
        return True


if __name__ == "__main__":
    main()
    
