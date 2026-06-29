# Get 5 numbers from user and find the biggest one
m = 0
for i in range(5):
    a= int(input("Enter next number: "))
    if a>m:
        m = a
print(m)
