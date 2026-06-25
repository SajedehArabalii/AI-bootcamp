password = "911"

while True:
    userpass = input("Enter your password: ")
    if password == userpass:
        print("Welcome")
        break
    else:
        print("another password")
