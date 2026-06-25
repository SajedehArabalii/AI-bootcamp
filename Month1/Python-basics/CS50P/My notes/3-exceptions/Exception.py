#Syntax error: unterminated string literal
#syntax error= problem with arrangement of words
#unterminated= started something but did not stop it
#string literal=  text written inside quotes like "hello" or 'hi'
#You started a string with a quote, but the closing quote is missing, so the program reached the end of the line/file without finishing the string
#TRY DOES NOT WORK FOR SYNTAX ERROR

#ValueError: invalid literal for int() with base 10:'cat'
#ValueError = the value given to a function is the right type but not acceptable
#invalid = not allowed or not usable
#int() = a function that converts something into an integer
#base 10 = normal decimal numbers (0–9)
#You tried to convert 'cat' into an integer using int(), but it isn’t a number, so Python can’t convert it.
try:
    x = int(input("What is x?: "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer.")


#NameError = A name that python does not recognize
#Try is an statement and not a function
while True:
    try:
        x = int(input("What is x?: "))
        #you can break here and delete else completely
    except ValueError:
        pass
    else:
        break    
print(f"x is {x}")

#THIS IN FUNCTION MODE iN FUNCEXCEPTION