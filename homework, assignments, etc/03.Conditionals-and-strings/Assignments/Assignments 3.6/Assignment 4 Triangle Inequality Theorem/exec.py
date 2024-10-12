length1 = float(input("side 1: "))
length2 = float(input("side 2: "))
length3 = float(input("side 3: "))

if (length1 + length2 > length3) and (length1 + length3 > length2) and (length2 + length3 > length1):
    print("YES")
    print("Dobre")
else:
    print("NO")
    print("Tikaj z mista")