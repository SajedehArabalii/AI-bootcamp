items = []
while True:
    item = input("Enter an item: ")
    if item == "exit":
        break
    items.append(item)
print("Your list", items)