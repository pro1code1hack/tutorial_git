#Interval Membership p.2
print("##"*20)

user_number = int(input("Please enter your number: "))

#interval [-5, 5]
if user_number >= -5 and user_number <= 5:
  is_user_number_be_in_first_interval = True
else:
  is_user_number_be_in_first_interval = False

#interval [0, 18]
if user_number >= 0 and user_number <= 18:
  is_user_number_be_in_second_interval = True
else:
  is_user_number_be_in_second_interval = False

#interval [0, 25]
if user_number >= 0 and user_number <= 25:
  is_user_number_be_in_third_interval = True
else:
  is_user_number_be_in_third_interval = False

if is_user_number_be_in_first_interval == True and is_user_number_be_in_second_interval == True and is_user_number_be_in_third_interval == True:
  print(f"Your number \"{user_number}\" belongs to the intervals [-5, 5], [0, 18] and [0, 30]")
elif is_user_number_be_in_first_interval == True and is_user_number_be_in_second_interval == True:
  print(f"Your number \"{user_number}\" belongs to the intervals [-5, 5] and [0, 18]")
elif is_user_number_be_in_first_interval == True and is_user_number_be_in_third_interval == True:
  print(f"Your number \"{user_number}\" belongs to the intervals [-5, 5] and [0, 30]")
elif is_user_number_be_in_second_interval == True and is_user_number_be_in_third_interval == True:
  print(f"Your number \"{user_number}\" belongs to the intervals [0, 18] and [0, 30]")
else:
  print(f"Your number \"{user_number}\" isn\'t in every interval")