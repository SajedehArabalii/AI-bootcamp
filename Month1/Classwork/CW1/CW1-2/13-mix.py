# Sum of 2 numbers
# Biggest number
# Check if the 2nd number is odd or even
def checkNumbers(num1,num2):
    print("sum: ", num1 + num2)
    if num1>num2:
        print("max: ", num1)
    else:
        print("max: ", num2)
    if num2 % 2 == 0:
        print("Second number is even.")
    else:
        print("Second number is odd.")

checkNumbers(2,3)