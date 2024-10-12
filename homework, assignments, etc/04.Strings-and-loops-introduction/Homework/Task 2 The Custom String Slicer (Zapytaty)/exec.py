print("Input:")
string = input("Enter a string: ")
start_index = int(input("Enter a start index: "))
end_index = int(input("Enter a stop index: "))
add_step = input("Do you want to add a step ((Y)es/(N)o)? ").casefold()

if add_step == "yes" or add_step == "y":
    step = int(input("Enter step: "))
else:
    step = 1

print(string[start_index:end_index:step])