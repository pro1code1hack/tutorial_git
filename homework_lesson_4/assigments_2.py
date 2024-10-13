#Palindromic Phrase Verifier

print("---"*20)
print("Hello! It\'s a program to detect palindrome word")
user_word = input("Please, enter a word which you want to check: ")

revers_word = user_word[::-1]

if revers_word == user_word:
  print(f"Your word \'{user_word}\' is a palindrome")
else:
  print("Your word isn\'t a palindrome")