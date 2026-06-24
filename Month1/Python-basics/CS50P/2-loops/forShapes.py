#How to make a column using for
for _ in range(3):
    print("#")
print("----------------------")

print("#\n"*3,end="")
print("----------------------")

#How to make a row
print("?" * 3)
print("----------------------")

#How to make a square
for i in range(3):
    for j in range(3):
        print("# ", end="")
    print()
print("----------------------")

for _ in range(3):
    print("# "*3, end="")
