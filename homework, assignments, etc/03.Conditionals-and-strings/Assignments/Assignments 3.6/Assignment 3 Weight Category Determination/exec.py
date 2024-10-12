weight = float(input("Weight of the boxer: "))

if weight < 30:
    print("This boxer will be disqualified ;) thank you for messaging us!")
elif weight >= 30 and weight <= 60:
    print("Lightweight")
elif weight > 60 and weight < 65:
    print("First Middleweight")
elif weight >= 65:
    print("Middleweight")