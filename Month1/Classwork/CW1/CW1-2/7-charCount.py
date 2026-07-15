# Get a string and say how many character it has
word = input("Enter a word: ")
count = 0
for letter in word:
    count+=1
print("Number of characters: ",count)