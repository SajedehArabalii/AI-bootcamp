age = int(input("What is your age?"))

if age<13:
    print("Child")
elif age>=13 and age<=19:
    print("Teen")
elif age>= 20 and age<=60:
    print("Adult")
else:
    print("Old")