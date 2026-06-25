txt = input("Enter a string:")
count = 0
for letter in txt:
    if letter in "aeiouAEIOU":
        count += 1
print("Number of vowels: ",count)