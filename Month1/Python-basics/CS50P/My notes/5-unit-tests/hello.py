def main():
    name = input("What is your name?: ")
    print(hello(name))

#You cannot test a function that does not have a return
def hello(to="world"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()