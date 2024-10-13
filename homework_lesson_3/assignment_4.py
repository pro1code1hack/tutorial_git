#Triangle Inequality Theorem
print("##"*20)
print("Please enter 3 sides of triangle using integers")

first_side = int(input("Please enter lenght of first side: "))
second_side = int(input("Please enter lenght of second side: "))
third_side = int(input("Please enter lenght of third side: "))

if first_side + second_side > third_side and first_side + third_side > second_side and second_side + third_side > first_side:
  print("A triangle with the indicated sides exists")
else:
  print("A triangle with the indicated sides can\'t exist")