# Rock, paper, scissors
import random

print("'r' for rock, 'p' for paper and 's' for scissors")

playerWins = 0
computerWins = 0
player = 'null'

while player != "exit":
    
    computer = random.choice(['r','p','s'])
    player = input("rock, paper, scissors: ")
    
    if player == computer:
        print("It's a draw")
    
    elif (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        playerWins += 1
        print(f"player {player} : computer {computer}")

    
    elif (computer == 'r' and player == 's') or (computer == 's' and player == 'p') or (computer == 'p' and player == 'r'):
        computerWins += 1
        print(f"player {player} : computer {computer}")


print(f"Player {playerWins}: Computer {computerWins}")

