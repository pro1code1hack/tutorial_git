#Weight Category Determination
print("##"*20)

user_number = int(input("Please enter your weight if you weigh less than 69 kilograms: "))

if user_number < 60:
  print(f"Your weight is \'{user_number}\' what means you are \'Lightweight\'")
elif user_number >= 60 and user_number < 64:
  print(f"Your weight is \'{user_number}\' what means you are \'First Middleweight\'")
elif user_number >= 65 and user_number < 69:
  print(f"Your weight is \'{user_number}\' what means you are \'Middleweight\'")