print("Let's check if you understand me, shall we? :)")
x = float(input("Enter such a number that is between -30 and -2 inclusively for both of the digits. Or, if you wish, you might like to put a number that is between 7 and 25. Your call: "))

if x >= -30 and x <= -2:
    print('The number %s belongs to the interval [-30, -2], you understood me well ;)' % (x))
elif x >= 7 and x <= 25:
    print("Second one, I see. Okay ;)")
else:
    print("Sadly, but you did not understand me. I am going to cry ;(")