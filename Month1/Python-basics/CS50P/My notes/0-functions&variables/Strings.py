#print("Hello, world")

#Quotes inside of quotes with single quotes and double quotes
print('Hello, "friend"')

#Quotes using an escape characters
print("Hello, \"friend\"")
print("----------------------")

#Ask user for their names
name = input("What is your name? ")

#Say hello to user
#Puts a space there automatically
print("Hello,", name)

#We have to put space in there manually
print("Hello,"+ name)

#putting name inside with fstring
print(f"Hello,{name}")

#How to write prints without it going to the next line
print("Hello, ",end="")
print(name)

#To check what seperater does
print("Hello,", name, sep="???")
print("----------------------")

#How to remove whitespace from string
name = name.strip()
#How to turn the first character into a capital one
name = name.capitalize()
print(f"Hello,{name}")

#How to title  based capitalization
name = name.title()
print(f"Hello,{name}")

#How to both capitalize and remove whitespace at the same time
name = name.strip().title()
print(f"Hello,{name}")

#best way to write this whole code 
newName = input("Enter new name: ").strip().title()
print(f"Hello,{newName}")  

#split name into first name and last name
first,last = newName.split(" ") 
print(f"Hello,{first}")