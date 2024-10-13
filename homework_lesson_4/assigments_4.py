#The Substring Counter

print("---"*24)
user_long_word = input("Hello! Please, write your word ot sentences: ")
user_check_word = input("Please, enter a group of letter or word what you want to count: ")

count = user_long_word.count(user_check_word)

print(f"We found \'{count}\' times \'{user_check_word}\' letters in \'{user_long_word}\'")