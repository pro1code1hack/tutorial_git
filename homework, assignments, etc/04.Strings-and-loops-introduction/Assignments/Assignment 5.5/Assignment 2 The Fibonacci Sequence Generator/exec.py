number = int(input("Enter the number you would like to see: "))
a = 0
b = 1
result = None

for i in range(1, number):
    print(a, end = " ")
    print(b, end = " ")
    a += b
    b += a
