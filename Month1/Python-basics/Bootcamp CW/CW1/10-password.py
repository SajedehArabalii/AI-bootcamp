# We have a set password, user cannot get in until they put it in
password = "911"

while True:
    userpass = input("Enter your password: ")
    if password == userpass:
        print("Welcome")
        break
    else:
        print("another password")
