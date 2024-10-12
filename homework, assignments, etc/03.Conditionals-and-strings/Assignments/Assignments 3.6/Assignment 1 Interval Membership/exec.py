print("Let's check if you understand me, shall we? :)")
x = float(input("Enter such a number that is between -3 and 7 inclusively for both of the digits: "))
print(x)
if x >= -3 and x <= 7:
    print('The number %s belongs to the interval [-3, 7], you understood me well ;)' % (x))
else:
    print("Sadly, but you did not understand me. I am going to cry ;(")