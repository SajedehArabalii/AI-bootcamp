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
        print()

#gets choice and makes sure it is valid
def get_choice(prompt):
    VALID_CHOICES = ("add","sell","search","show","save","report","exit")
    while True:
        #Because it is a constant so we use tuples

        choice = input(prompt).strip().lower()
        if choice in VALID_CHOICES:
            return choice
        else:
            print("\tYour choice was invalid")
            print()

# add => gets name and amount, and adds them
#   if the item existed before it should only add to the amount
def add(stock):
    while True:

        name = get_name("Name of the item: ")
        amount_to_add = get_int("How many to stock:")

        # for item, quantity in stock.items():
        #     if item == name:
        #         amount += quantity
        # stock[name] = amount

        #.get():Give me this value if it exists, otherwise give me zero
        stock[name] = stock.get(name, 0) + amount_to_add
        
        if input("Do you want to continue(y/n): ") != "y":
            break

# sell => gets name and amount, and reduct it from the stocks
#   if there is not enough in stock print("not enough")  
def sell(stock):
    name = get_name("What item did you sell: ")
    amount_to_sell = get_int("How many were sold: ")
    # flag = 0
    # for item, quantity in stock.items():
    #     if item == name:
    #         flag =1
    #         if quantity >= sold:
    #             stock[name] = quantity - sold
    #         else:
    #             print("\tNot enough in stock")
    # if flag == 0:
    #     print("\tCould not find the item")

    #Getting rid of flag
    #Getting rid of for
    #Accessing every value using stock[name]
    if name not in stock:
        print("\tCould not find item.\n")
        return
    # if stock[name] >= amount_to_sell:
    #     stock[name] -= amount_to_sell
    #     remove_empty(stock,name)
    # else:
    #     print("\tNot enough.")
    if stock[name] < amount_to_sell:
        print("\tNot enough:")
        return
    stock[name] -= amount_to_sell
    remove_empty(stock,name)

# search => get name and say how many left
def search(stock):
    name = get_name("Name of the item you are looking for: ")
    # flag = 0
    # for item, amount in stock.items():
    #     if item == name:
    #         flag =1
    #         print(f"\tYou have {amount} in stock.")
    # if flag == 0:
    #     print("\tCould not find the item")
    # print()

    if name in stock:
        print(f"\tYou have {stock[name]} in stock")
    else:
        print("\tCould not find the item")

# show => every item and quantity
def show(stock):
    if not stock:
        print("\tNo items.")
        return
    for item, amount in stock.items():
        print(f"\t{item} - {amount}")


# save => save info in a txt
# format => milk - 12
def save(stock):
    #Opens file over and over which is bad
    # open("stock.txt",'w').close()
    # for item,quantity in stock.items():
    #     with open("stock.txt","a") as file:
    #         file.write(f"{item} - {quantity}\n")

    with open("stock.txt","w") as file:
        for item,amount in stock.items():
            file.write(f"{item} - {amount}\n")
    print("\tStock saved.")

    

# report => all of items in stock
#           amount of items in stock
#           item with the most quantity
#           item with the least quantity
def report(stock):
    if not stock:
        print("Stock is empty")
        return
    show(stock)
    amount_of_stuff(stock)
    most(stock)
    least(stock)


def amount_of_stuff(stock):
    print(f"\tYou have {sum(stock.values())} items in total.")

def most(stock):
    # high = 0
    # for quantity in stock.values():
    #     if high < quantity:
    #         high = quantity

    #gets the highest amount of value
    # high =  max(stock.values())

    # for item, quantity in stock.items():
    #     if quantity == high:
    #         print(f"You have the most amount of {item}")

    item = max(stock, key=stock.get)
    print(f"\tYou have the most amount of {item}")

def least(stock):
    # low = 100000000000000000000000
    # low = float("inf") is the better version of above and it means infinity

    # for quantity in stock.values():
    #     if low > quantity:
    #         low = quantity

    #gets the lowest amount of value
    # low = min(stock.values())

    # for item, quantity in stock.items():
    #     if quantity == low:
    #         print(f"You have the least amount of {item}")

    item = min(stock, key=stock.get)
    print(f"\tYou have the least amount of {item}")

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
            return int(input(prompt))
        except ValueError:
            print("Invalid value.")

def remove_empty(stock, name):
    if stock[name] == 0:
        del stock[name]

if __name__ == "__main__":
    main()