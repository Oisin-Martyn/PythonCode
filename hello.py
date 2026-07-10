#Ask user for their name
name = input("What's your name? ")

#Remove whitespace from string and capitalize user's name
name = name.strip().title()

#Say Hello to user
print(f"hello, {name}")
