import sys
if len(sys.argv)<2:
    sys.exit("Too few arguments")

#Starts at arg 1 till the end, this is called slicing
# arg 0 is the name of the program
for arg in sys.argv[1:]:
    print("Hello my name is", arg)
print("----------------------")

#not the last one
for arg in sys.argv[1:-1]:
    print("Hello my name is", arg)