#Objective: Develop an interactive game with a mini plot twist.

print("Zaraz ja budu zalyvaty tobi lokshynu v vukha")
choice = input("(P)ohodzhujusja, (N)e pohodzujusja *Khana CMD jakshcho (N) ;)\n")

if choice.lower() == "p":
    print("Molodec' ;)")
else:
    print("bad, bad")

print("You are going through the forest. You see a beautiful mushroom. Consume it?")
choice = input("(C)onsume, (N)i\n")

if choice.lower() == "c":
    print("You ate the mushroom. In a few hours of traveling you puked a few times and died")
else:
    print("You skipped such a tasty-looking product. Maybe it was a good decision ^o^")