# Number Guessing Game
#
# The player has five chances to guess a randomly generated number.
# After each incorrect guess, the program indicates whether the
# secret number is higher or lower.

import random

def main():
    # Game settings
    high = 10
    low = 1
    rounds = 5
    tries = 0

    print("Let's play guess the number.\nI choose and you guess\nYou have 5 tries")

    # Generate the secret number
    num = random.randint(low,high)

    # Keep asking for guesses until the player wins or runs out of tries
    while tries<rounds:
        guess = get_guess(low, high)
        tries += 1
        if compare(num, guess):
            print(f"You got it in {tries} tries")
            return
    print(f"You lost! The number was {num}.")

# Prompt the user until they enter a valid integer
# Within the allowed range
def get_guess(low,high):
            while True:
                try:
                    guess = int(input("Enter a number: "))
                    if low <= guess <= high:
                        return guess
                    else:
                        print(f"Number should be between {low} and {high}: ")
                except ValueError:
                    print("Please Enter a valid number between 1 and 100.")

# Compare the player's guess with the secret number.
# Returns True if the guess is correct; otherwise prints
# a hint and returns False.
def compare(num, guess):
    if guess < num:
        print("Higher")
        return False
    if guess > num:
        print("Lower")
        return False
    else:
        return True


if __name__ == "__main__":
    main()     
    
