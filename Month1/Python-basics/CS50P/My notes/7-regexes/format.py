import re

name = input("What is your name?: ").strip()

# imagine the user inputs last name before first name, like Arabali, Sajedeh
# if ","  in name:
#     last,first = name.split(", ")
#     name = f"{first} {last}"

# () has the ability to capture
# star does the job of strip() here
# matches = re.search(r"^(.+), *(.+)$", name)/ sent it to after if

# := walrus operator , both assigns a value and asks a boolean question
if matches := re.search(r"^(.+), *(.+)$", name):
    # last,first = matches.groups()
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")
