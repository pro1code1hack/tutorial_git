#The Name Corrector

print("---"*20)
print("Hello! Let\'s check if you write your name correct")
user_name = input("Please, enter your name: ")

correct_user_name = user_name.casefold()
correct_user_name = user_name.capitalize()

if correct_user_name == user_name:
  print(f"You write your name \'{user_name}\' and it\'s correct!")
else:
  print(f"You write your name \'{user_name}\' but it have mistake. Correct name: {correct_user_name}")