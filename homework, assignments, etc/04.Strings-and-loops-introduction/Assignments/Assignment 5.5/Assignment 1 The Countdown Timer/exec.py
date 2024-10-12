import time

t = int(input("Enter the countdown time: "))

print("The bomb will explode in %s seconds!" %(t))

for i in range(t, 1, -1):
    t -= 1
    time.sleep(1)
    print(t)

user_input = input("Quick! Which wire to cut? (R)ed or (B)lue?\n")
print(user_input.lower())

if user_input.lower() == "b" or user_input.lower() == "blue":
    print("You cut the blue wire...")
    time.sleep(2.5)
    print("The bomb has been defused. Congratulations, you saved the day!")
elif user_input.lower() == "r" or user_input.lower() == "RED":
    print("You cut the red wire...")
    time.sleep(0.5)
    print("BEEP")
    time.sleep(1.0)
    print("BOOM!!! The bomb exploded")