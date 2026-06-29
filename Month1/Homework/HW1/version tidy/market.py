# Market Stock Manager
#
# A simple inventory management program that stores items
# and their quantities in a dictionary. Users can add,
# sell, search, display, save, and generate reports
# about the current stock.

# Run the main menu and process user commands.
def main():
    stock = {}

    print("Welcome to the market, What would you like to do?")
    while True:
        choice = get_choice("Would you like to add, sell, search, show, save, report or exit? ")

        match choice:
            case "add":
                add(stock)
            case "sell":
                sell(stock)
            case "search":
                search(stock)
            case "show":
                show(stock)
            case "save":
                save(stock)
            case "report":
                report(stock)
            case "exit":
                print("Goodbye!")
                return
        print()

# Prompt the user until they enter a valid menu option.
def get_choice(prompt):
    VALID_CHOICES = ("add","sell","search","show","save","report","exit")
    while True:

        choice = input(prompt).strip().lower()
        if choice in VALID_CHOICES:
            return choice
        else:
            print("\tYour choice was invalid")
            print()

# Add one or more items to the inventory.
# If an item already exists, increase its quantity.
def add(stock):
    while True:

        name = get_name("Name of the item: ")
        amount_to_add = get_int("How many to stock:")

        stock[name] = stock.get(name, 0) + amount_to_add
        
        if input("Do you want to continue(y/n): ") != "y":
            break

# Sell an item by reducing its quantity.
# Remove the item if its quantity reaches zero.
def sell(stock):
    name = get_name("What item did you sell: ")
    amount_to_sell = get_int("How many were sold: ")

    if name not in stock:
        print("\tCould not find item.\n")
        return

    if stock[name] < amount_to_sell:
        print("\tNot enough:")
        return
    stock[name] -= amount_to_sell
    remove_empty(stock,name)

# Search for an item and display its current quantity.
def search(stock):
    name = get_name("Name of the item you are looking for: ")

    if name in stock:
        print(f"\tYou have {stock[name]} in stock")
    else:
        print("\tCould not find the item")

# Display every item currently stored in the inventory.
def show(stock):
    if not stock:
        print("\tNo items.")
        return
    for item, amount in stock.items():
        print(f"\t{item} - {amount}")

# Save the current inventory to a text file.
def save(stock):

    with open("stock.txt","w") as file:
        for item,amount in stock.items():
            file.write(f"{item} - {amount}\n")
    print("\tStock saved.")

# Display a summary of the inventory, including:
# - all items in stock
# - total quantity of items
# - item with the highest quantity
# - item with the lowest quantity
def report(stock):
    if not stock:
        print("Stock is empty")
        return
    show(stock)
    amount_of_stuff(stock)
    most(stock)
    least(stock)

# Display the total quantity of all items in stock.
def amount_of_stuff(stock):
    print(f"\tYou have {sum(stock.values())} items in total.")

# Display the item with the highest quantity
def most(stock):
    item = max(stock, key=stock.get)
    print(f"\tYou have the most amount of {item}")

# Display the item with the lowest quantity.
def least(stock):
    item = min(stock, key=stock.get)
    print(f"\tYou have the least amount of {item}")

# Prompt until the user enters a non-empty item name.
def get_name(prompt):
    while True:
        name = input(prompt).strip().title()
        if name != "":
            return name
        else:
            print("You did not enter the name.")

# Prompt until the user enters a valid integer.
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid value.")

# Remove an item from the inventory if its quantity reaches zero.
def remove_empty(stock, name):
    if stock[name] == 0:
        del stock[name]

if __name__ == "__main__":
    main()