# Objective: Create an app which checks user's password and based on your rules states if it's secure or not.

user_password = input("Enter password you want to evaluate: ")

#Strong
#1. minimum 8 characters
#2. contains at least one uppercase letter,
#3. contains at least one lowercase letter,
#4. contains at least one number,
#5. contains at least one special character (e,g., !@#$%^&*)
#Medium
#1. minimum 6 characters
#2. contains at least one letter(uppercase or lowercase)
#3. contains at least one number.
#Weak
#Anything shorter than 6 characters or not meeting medium requirements

special_characters = "!@#$%^&*"

# Check if Strong
if (len(user_password) >= 8 and
    any(char.islower() for char in user_password) and
    any(char.isupper() for char in user_password) and
    any(char.isdigit() for char in user_password) and
    any(char in special_characters for char in user_password)):
    print("Strong password")

# Check if Medium
elif (len(user_password) >= 6 and
      any(char.isalpha() for char in user_password) and
      any(char.isdigit() for char in user_password)):
    print("Medium password")

# Anything else is Weak
else:
    print("Weak password")