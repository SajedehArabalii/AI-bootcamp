#We want our codes to flow top to bottom, so in ordeer to make it work we make a main function, put other functions after it, and call main on bottom of the code, so that the code understand functions that were written after it.

#To call a function we put the name of the function followed by parantesis
#Inside the parantesis we put the value of parameters
def main():
    hello()
    name = input("What is your name? ")
    hello(name)
    
    #We can put the value returned from calculater in a variable
    result = squared()
    print("Squared= ",result)

#We use def to define a function
#The parameter is name which is entered when the code is being called
#We can put a set value for parameter in case the user did not enter a value
def hello(name='World'):
    print("Hello, ", name)

#Return the result so that it can be used in the main function
def squared():
    x = int(input("Enter number: "))
    #x *=x
    #x**2
    return x*x

#The main being called
main()