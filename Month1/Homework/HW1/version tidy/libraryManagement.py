# Library Manager
#
# A simple program that stores books and their authors using
# a dictionary. Users can add books, search by title, view
# the entire library, or exit the program.

def main():
    library = {}

    print("Welcome to your library, What would you like to do? ")

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

# Prompt the user until they enter a valid menu option.
def get_choice():
    VALID_CHOICES = ("add", "search", "show", "exit")

    while True:
        choice = input("Add, Search, Show or Exit? ").strip().lower()

        if choice in VALID_CHOICES:
            return choice
        
        else:
            print("Invalid command.")

# Add one or more books to the library.
# Each book title is used as the dictionary key,
# and its author is stored as the value.
def add(library):
    while True:
        title = not_empty("What is the title of the book?: ")
        author = not_empty("Who is the author of the book?: ")

        library[title] = author

        if input("Do you want to continue(y/n): ").strip().lower() != "y":
            break

# Prompt until the user enters a non-empty string.
def not_empty(prompt):
    while True:
        value = input(prompt).strip().title()
        if value:
            return value
        print("Input cannot be empty.")

# Search for a book by title and display its author.
def search(library):
    title = input("What book are you looking for: ").strip().title()

    if title in library:
        print(f"Author's name is {library[title]}.")
    else:
        print("Book was not found.")

# Display every book currently stored in the library.
def show(library):
    if not library:
        print("Library is empty.")
        return

    for i, (title, author) in enumerate(library.items(), start=1):
        print(f"{i}- Title: {title}, Author: {author}")
    

if __name__ == "__main__":
    main()