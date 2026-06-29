# An app that let's user manage their library
# menu => add , search , show , exit
# add => title of book and author in a dictionary
# search => get title of book and show the author
# show => show every book
# exit => exit the app

def main():
    # An empty library
    library = {}

    # instruction
    print("Welcome to your library, What would you like to do? ")

    # compare the choice to the options 
    while True:
        choice = get_choice()
        match choice:
            case "add":
                add(library)
            case "search":
                search(library)
            case "show":
                show(library)
            case "exit":
                print("Goodbye!")
                return

# Getting choice and making sure it is valid
def get_choice():
    VALID_CHOICES = ("add", "search", "show", "exit")

    while True:
        choice = input("Add, Search, Show or Exit? ").strip().lower()

        if choice in VALID_CHOICES:
            return choice
        
        else:
            print("Invalid command.")

# Adds a book to the dictionary
def add(library):
    while True:
        title = not_empty("What is the title of the book?: ")
        author = not_empty("Who is the author of the book?: ")

        library[title] = author

        # So we don't have to type add everytime, or I could make it so that it continues going on until the user gives and empty string for the name, but I already wrote it soooooooo
        if input("Do you want to continue(y/n): ").strip().lower() != "y":
            break


#Check that the input is not empty
#prompt = "What is the .... of the book?: "
def not_empty(prompt):
    while True:
        value = input(prompt).strip().title()
        if value:
            return value
        print("Input cannot be empty.")


# Searches for a book in dictionary
def search(library):
    # flag = 0
    title = input("What book are you looking for: ").strip().title()
    # for title, author in library.items():
    #     if title == book:
    #         print(f"Author's title is {author}")
    #         flag +=1
    # if flag == 0:
    #     print("book was not found.")
    if title in library:
        print(f"Author's name is {library[title]}.")
    else:
        print("Book was not found.")


# Prints all item in dictionary
def show(library):
    if not library:
        print("Library is empty.")
        return

    # for title,author in library.items():
    #     print(f"title: {title}, Author: {author}")
    for i, (title, author) in enumerate(library.items(), start=1):
        print(f"{i}- Title: {title}, Author: {author}")
    


if __name__ == "__main__":
    main()