#This gets 2 strings so the plus puts these strings adjacent to each other, and you can put other characters than numbers inside
x = input("Enter first number: ")
y = input("Enter second number: ")
sum = x+y

print("String form= ",sum)
print("----------------------")

#Turning strings to integers
sum = int(x)+ int(y)
div = int(x)/ int(y)
print("Turned to integer= ",sum)
print("----------------------")

#Division and rounding numbers
print("Division of integers= ",div)
print("Rounded division= ", round(div,2))
print(f"Rounding using fstring= {div:.2f}")

print("----------------------")

#This gets 2 integers so the + sums them up and limits you into entering numbers
x = float(input("Enter first float number: "))
y = float(input("Enter second float number: "))
print("Get float from start= ",x+y)
print("Round the sum= " , round(x+y))
print("----------------------")

#for big numbers you can seperate them by comma
x = int(input("Enter first big number: "))
y = int(input("Enter second big number: "))
sum = x+y
print("Without seperaters= ",sum)
print(f"With seperaters= {sum:,}")

