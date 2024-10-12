# 1. Preparation
# 1.1. personal
name = None
companion = None
destination = None
food = True
flask = True
drink = True

#1.2. 
location_1 = "forest"
location_2 = "beach"

#Main
name = input("Choose your character's name: ")
companion = input("Choose a companion (dog/cat): ")
destination = input(f"Choose a destination ({location_1}/{location_2}): ")

print(f"{name}, along with her loyal {companion}, set out on an adventure to the {destination}.")

print("")