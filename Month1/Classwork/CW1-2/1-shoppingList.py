# Get names of items until user enters exit and put them in list
items = []
while True:
    item = input("Enter an item: ")
    if item == "exit":
        break
    items.append(item)
print("Your list", items)