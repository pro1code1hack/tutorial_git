city1 = input("City1 name: ")
city2 = input("City2 name: ")
city3 = input("City3 name: ")

length_city1 = len(city1)
length_city2 = len(city2)
length_city3 = len(city3)

#The city with the longest name
if length_city1 > length_city2 and length_city1 > length_city3:
    print("%s has the longest name!" % (city1))
elif length_city2 > length_city1 and length_city2 > length_city3:
    print("%s has the longest name!" % (city2))
else:
    print("%s has the longest name!" % (city3))

#The city with the shortest name
if length_city1 < length_city2 and length_city1 < length_city3:
    print("%s has the shortest name!" % (city1))
elif length_city2 < length_city1 and length_city2 < length_city3:
    print("%s has the shortest name!" % (city2))
else:
    print("%s has the shortest name!" % (city3))


# Ця програма - повний кринж. Я знаю, що я нагімнокодив. Сто відсотків можна
# скоротити її + зробити більш оптимізованою. Але я поки що щось занадто дубовий
# для цього