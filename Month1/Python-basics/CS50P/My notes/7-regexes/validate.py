# Library of regular expression
import re

email = input("What is your email?: ").strip()

# Check if the string has an @ and .com
# if "@" in email and ".com" in email:
#     print("Valid")
# else:
#     print("Invalid")

# Split the email into username and domain name
# userName, domain = email.split("@")

# if (userName) and (domain.endswith(".com")):
#     print("valid")
# else:
#     print("Invalid")


#USING re.search 
#CHecking if @ is in email
# if re.search("@", email)

#----@---.com
# We can use ..* instead of .+ to get characters before and after @
# Checking if it ends with .com(we put a backslash to make sure the code does not mistake . of .com with the regex.)
# r stands for raw and works like fstring
# ^ is start of string and $ is end of string
if re.search(r"^.+@.+\.com$", email):
    print("Valid")
else:
    print("Invalid")

