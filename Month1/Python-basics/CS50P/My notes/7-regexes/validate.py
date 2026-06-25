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
#if re.search(r"^.+@.+\.com$",email): validated even if there were 2@
# if re.search(r"^[^@]+@[^@]+\.com$", email): Excludes @ 
# \w instead of a-zA-Z0-9_
# Flag = re.ignorecase
# if re.search(r"^[\w]+@[\w]+\.com$",email,re.IGNORECASE):it does not support domains that contain 2 or more .s




# The pattern explained:
# ^\w+          -> Starts with one or more alphanumeric characters
# @             -> A literal @ symbol
# (\w+\.)+      -> Matches "something followed by a dot" one or more times (e.g., "sub." or "sub.domain.")
# (com|edu|gov) -> Matches the final top-level domain
if re.search(r"^(\w|\.)+@(\w+\.)+(com|edu|gov|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
