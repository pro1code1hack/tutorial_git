# Objective: Create a program that can convert a given string into either uppercase or lowercase based on the user's choice.

text = input("Enter your text: ")
choice = input("Choose (U)pper or (L)ower: ")

if choice.lower() == "u":
    print(text.upper())
elif choice.lower() == "l":
    print(text.casefold())
else:
    print("Enter P or L, not other letters ;)")