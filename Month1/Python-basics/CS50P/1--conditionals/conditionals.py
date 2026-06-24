#Compare using if
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x<y:
    print(f"{x} is lower than {y}")
elif x>y:
    print(f"{y} is lower than {x}")
else:
    print("They are equal") 
print("----------------------")

#Check just if x and y are equal
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x<y or y<x:#        if x!=y:
    print("They are not equal")
else:
    print("They are equal")
print("----------------------")

#Grade
score = int(input("Score: "))
if 90 <= score <= 100:
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
elif score>=0:
    print("F")
else:
    print("Invalid")
print("----------------------")

#Even or Odd
x = int(input("Enter number: "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
print("----------------------")

#Even or odd with function
def is_odd(n):
    return n%2

if is_odd(x):
    print("Odd")
else:
    print("Even")
print("----------------------")

#Even or odd with function
def is_even(n):
    # if n%2==0:
    #     return True
    # else:
    #     return False
    return True if n%2==0 else False 
    #return (n%2==0)

if is_even(x):
    print("Is Even")
else:
    print("Is Odd")
print("----------------------")

# Hogwarts house system
name = input("What is your name: ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffendor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")