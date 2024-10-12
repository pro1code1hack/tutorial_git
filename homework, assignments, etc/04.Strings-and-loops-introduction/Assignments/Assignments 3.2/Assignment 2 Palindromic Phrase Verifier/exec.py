# Objective: Develop a program that checks whether a word is a palindrome (reads the same backward as forward).

word = "radar"
word1= "adar"
if word[:] == word[::-1]:
    print(word[:])
    print(word[::-1])
    print("Yes") 