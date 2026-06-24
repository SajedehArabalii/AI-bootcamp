# import random imports everything in library random, and we should say random.choice
# How to import certain functions from library, and we do not have to specify which choice by saying random.choice
from random import choice
from random import randint
from random import shuffle

#Chooses between items of a list
coin = choice(["heads","tails"])
print(coin)
print("----------------------")

#Chooses a number between a and b
x = randint(1,10)
print(x)
print("----------------------")

#Makes the order random
cards = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
shuffle(cards)
print(cards) 
print("----------------------")


