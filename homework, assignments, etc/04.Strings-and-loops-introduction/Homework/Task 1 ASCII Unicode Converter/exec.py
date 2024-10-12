# We haven't learnt the topic of lists, arrays, dictionaries. I assume that I need to play along and try to do it without them.

#preparation
message = None
i = 1

# Menu
print("This is an encryptor and decryption application. Enjoy")
choice = input("# (1). (E)ncrypt Messages\
               2. (D)ecrypt Messages\n>> ")


# Encrypt path
if choice.casefold() == "e" or choice == "1":
    message = int(input("Enter the number of messages to encrypt: "))
    if message == 0:
        input("Press Enter to close the program: ")
    elif message >= 1:
        for a in (1, message):
            message_to_encrypt = input("Enter message %s:\n>> " %(a))
            print("Encrypted message %s:" %(a), end = " ")
            for b in message_to_encrypt:
                print(ord(b), end = " ")
            print("\n")


# Decrypt path
elif choice.casefold() == "d" or choice == "2":
    message = int(input("Enter the number of messages to decrypt: "))
    if message == 0:
        input("Press Enter to close the program: ")
    elif message >= 1:
        for a in range(1, message + 1):
            message_to_decrypt = input("Enter message %s (space-separated numbers):\n>> " % (a))
            encrypted_numbers = message_to_decrypt.split()
            for num in encrypted_numbers:
                print(chr(int(num)), end="")
            print("\n")
#Else
else:
    print("Are you sure you are not mistaken? :)")