import sys

#Checking if the user gave both arguments, name of the program and their own name
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
#if we want to add 2 words in the same argument we should use ""
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    #In the terminal you say python fileName argument
    print("Hello, my name is", sys.argv[1]) 


