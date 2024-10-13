#Interval Membership

user_number = int(input("Please enter your number: "))

if user_number >= -5 and user_number <= 5:
  print(f"Your number \"{user_number}\" belongs to the interval [-5, 5]")
elif user_number > 5:
  print(f"Your number \"{user_number}\" more per interval [-5, 5]")
else:
  print(f"Your number \"{user_number}\" less per interval [-5, 5]")