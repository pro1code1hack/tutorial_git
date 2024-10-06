#8.
#Task 4:
# s = str(input("Enter the name of a soccer team: "))

# print(s, "is a champion!")

#Task 5:
# s1 = str(input())
# s2 = str(input())
# s3 = str(input())

# print(s1)
# print(s2)
# print(s3)

#Task 6:
# s1 = str(input())
# s2 = str(input())
# s3 = str(input())

# print(s3)
# print(s2)
# print(s1)


#6.
#Task 1: Unit converter
# num = float(input("Enter a length in inches: "))

# print("Lenght in centimeters equals:", (num*2.54))

#Task 2: Temperature converter
# tmp = float(input("Enter a temperature on Fahrenheit: "))

# print("Temperature in Celsius is:", ((tmp-32)*5/9), "C")

#Task 3: Simple interest calculatore
# principals_amount = float(input("Enter the principals: "))
# rate = float(input("Enter the rate: "))
# period = float(input("Enter the period: "))
# simple_interests = (principals_amount*rate*period)/100

# print("Simple interest is:", simple_interests)

#Assignment 3.6
#Assignment 1: Interval Membership
# x = int(input("Enter the X: "))
# if x >= -3 and x <= 7:
# 	print("The number", x ,"belongs to the interval [-3, 7]")
# else:
# 	print("The number", x ,"dont belongs to the interval [-3, 7]")

#Assignment 2: Interval Membership p.2
# x = int(input("Enter the X: "))
# if x >= -30 and x <= -2:
# 	print("The number", x ,"belongs to the interval [-30, -2]")
# elif x >= 7 and x <= 25:
# 	print("The number", x ,"belongs to the interval [7, 25]")

#Assignment 3: Weight category determination
# weight = int(input("Enter the boxer's weight in kg: "))
# if weight <= 60:
# 	print("Lightweight")
# elif weight > 60 and weight <= 64:
# 	print("First Middleweight")
# elif weight > 64 and weight <= 69:
# 	print("Middleweight")
# else:
# 	print("Data is incorrect")

#Assignment 4: Triangle inequality theorem
# num1 = int(input("Enter the first side: "))
# num2 = int(input("Enter the second side: "))
# num3 = int(input("Enter the third side: "))

# if num1 < (num2+num3) and num2 < (num1+num3) and num3 < (num2+num1):
# 	print("YES")
# else:
# 	print("NO")

#4.4 Assignment
#Assignment 1:
# city1 = str(input("Enter the name of the first city: "))
# city2 = str(input("Enter the name of the second city: "))
# city3 = str(input("Enter the name of the third city: "))

# ln1 = len(city1)
# ln2 = len(city2)
# ln3 = len(city3)

# if ln1 > ln2 and ln2 > ln3:
# 	print(city1)
# 	print(city2)
# 	print(city3)
# elif ln2 > ln1 and ln1 > ln3:
# 	print(city2)
# 	print(city1)
# 	print(city3)
# elif ln3 > ln2 and ln2 > ln1:
# 	print(city3)
# 	print(city2)
# 	print(city1)

#Assignment 2:
# s = str(input("Enter a line: "))
# if s == "Saturday" or s == "Sunday":
# 	print("YES")
# else:
# 	print("NO")

#Assignment 3:
# s = str(input("Enter an email: "))
# if "@" in s and "." in s:
# 	print("YES")
# else:
# 	print("NO")

#6. Homework
#Task 1:
# pswd = str(input("Enter your password: "))

# if len(pswd) >= 8:
# 	print("Strong")
# elif len(pswd) >= 6 and len(pswd) < 8:
# 	print("Medium")
# elif len(pswd) < 6:
# 	print("Weak")

#Task 2:


#Task 3:
# city1 = str(input("Enter the first city: "))
# city2 = str(input("Enter the second city: "))
# city3 = str(input("Enter the third city: "))

# print("Your travel itinerary:", city1, "->", city2, "->", city3)

#-----------------------------------------------------------------------------------------

# ###f string

# number = int(input("Enter a number: "))

# for i in range(1, 11):
# 	print(f"{number} * {i} = {number*i}")

#Homework 7.
#Task 1:
# print("1.Encrypt Message")
# print("2.Decrypt Message")
# method = int(input("Chose a method: "))


# res = ""

# if(method == 1):
# 	msg = str(input("Enter a message: "))
# 	for el in msg:
# 		res += str(ord(el))
# 		res += " "
# elif(method == 2):
# 	msg = int(input("Enter an encrytped message: "))
# 	res+=str(chr(msg))

# print(res)

#Task 2:
# str = str(input("Enter a message: "))
# indx1 = int(input("Enter start index: "))
# indx2 = int(input("Enter end index: "))
# flag = input("Do you want to add a step (yes/no)?: ")

# if(flag == "yes"):
# 	step = int(input("Enter step: "))
# 	print(f"The sliced string with step is: {str[indx1:(indx2+1):step]}")
# else:
# 	print(f"The sliced string is: {str[indx1:indx2]}")

# str = "www.example.com"
# str1 = str[6:]
# res = str[:7]

# for i in range(len(str1)):
# 	if str1[i] == '.':
# 		res+="."
# 	else:
# 		res+="."
# print(res)

#10. Homework
#Task 1:
# flag = int(input("Menu:\n1.Add an item\n2.Remove an item\n3.Modify an item\n"))

# ls = []

# if flag == 1:
# 	n = input("Enter the item to add: ")
# 	ls.append(n)
# 	print(ls)
# elif flag == 2:
# 	n = input("Enter the item to remove: ")
# 	ls.pop(ls.index(n, 0, len(ls)))
# 	print(ls)
# else:
# 	n = input("Enter the item to modify: ")
# 	n1 = input("Enter the new item: ")
# 	ls[ls.index(n, 0, len(ls))] = n1
# 	print(ls)

#Task 2:
# ls = list(input("Enter a list of numbers(without spaces: "))

# start = int(input("Enter start index for slicing: "))
# end = int(input("Enter end index for slicing: "))

# print(f"The sliced list is: {ls[start:end]}")

