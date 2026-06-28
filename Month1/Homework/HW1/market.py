# Manages the stocks of a market
# Info should be saved in a dictionary 
# key = name of item
# value = quantity
# add, sell, search, show, save, report, exit
# add => gets name and amount, and adds them
#   if the item existed before it should only add to the amount
# sell => gets name and amount, and reduct it from the stocks
#   if there is not enough in stock print("not enough")
# search => get name and say how many left
# show => every item and quantity
# save => save info in a txt
# format => milk - 12
# report => all of items in stock
#           amount of items in stock
#           item with the most quantity
#           item with the least quantity
# exit => exit


def main():
    # make the empty dictionary
    stock = {}

    # Show instruction
    print("Welcome to the market, What would you like to do?")
    while True:
        #get the choice
        choice = get_choice("Would you like to add, sell, search, show, save, report or exit? ")

        #compare the choice and call the needed function
        # add, sell, search, show, save, report, exit
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

#gets choice and makes sure it is valid
def get_choice(prompt):
    while True:
        valid = ["add","sell","search","show","save","report","exit"]
        choice = input(prompt).strip().lower()
        if choice in valid:
            return choice
        else:
            print("\tYour choice was invalid")


# add => gets name and amount, and adds them
#   if the item existed before it should only add to the amount
def add(stock):
    while True:

        name = get_name("Name of the item: ")
        amount = get_int("How many to stock:")

        for item, quantity in stock.items():
            if item == name:
                amount += quantity
        

        stock[name] = amount
        
        if input("Do you want to continue(y/n): ") != "y":
            break
    

# sell => gets name and amount, and reduct it from the stocks
#   if there is not enough in stock print("not enough")  
def sell(stock):
    flag = 0
    name = get_name("What item did you sell: ")
    sold = get_int("How many were sold: ")
    for item, quantity in stock.items():
        if item == name:
            flag =1
            if quantity >= sold:
                stock[name] = quantity - sold
            else:
                print("\tNot enough in stock")
    if flag == 0:
        print("\tCould not find the item")




# search => get name and say how many left
def search(stock):
    flag = 0
    name = get_name("Name of the item you are looking for: ")
    for item, quantity in stock.items():
        if item == name:
            flag =1
            print(f"\tYou have {quantity} in stock.")
    if flag == 0:
        print("\tCould not find the item")



# show => every item and quantity
def show(stock):
    for item, quantity in stock.items():
        print(f"\t{item} - {quantity}")

# save => save info in a txt
# format => milk - 12
def save(stock):
    open("stock.txt",'w').close()
    for item,quantity in stock.items():
        with open("stock.txt","a") as file:
            file.write(f"{item} - {quantity}\n")


# report => all of items in stock
#           amount of items in stock
#           item with the most quantity
#           item with the least quantity
def report(stock):
    show(stock)
    most(stock)
    least(stock)

def most(stock):
    high = 0
    for quantity in stock.values():
        if high < quantity:
            high = quantity
    for item, quantity in stock.items():
        if quantity == high:
            print(f"You have the most amount of {item}")

def least(stock):
    low = 100000000000000000000000
    for quantity in stock.values():
        if low > quantity:
            low = quantity
    for item, quantity in stock.items():
        if quantity == low:
            print(f"You have the least amount of {item}")

def get_name(prompt):
    while True:
        name = input(prompt).strip().title()
        if name != "":
            return name
        else:
            print("You did not enter the name.")

def get_int(prompt):
    while True:
        try:
            amount = int(input(prompt))
            return amount
        except ValueError:
            print("Invalid value.")


if __name__ == "__main__":
    main()