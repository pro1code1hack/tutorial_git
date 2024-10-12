# p=input()
# print(p[::-1])
#----------------
# palind=input()
# if(palind==palind[::-1]):
#     print("Palindrome")
# else:
#     print("NO")
#----------------
# name=input()
# print(name.casefold().capitalize())
#----------------
# st="hellohellohello"
# print(st.count('ell'))
#----------------
# sentence=input()
# widt=input()
# print(sentence.center(widt))
#----------------
# sent = input()
# choice=input("upper or lower:")
# if choice=='upper':
#     print(sent.upper())
# elif choice=='lower':
#     print(sent.casefold())
# else:
#     print("incorrect choice!")
#----------------
# urlAd=input()
# if("https://"==urlAd[0:8]):
#     print("No need to correct")
# else:
#     print("Corrected:","https://"+urlAd)
#----------------
# w=input()
# for i in range(len(w)):
#     print(ord(w[i]),end=" ")
# ch=input("encrypt or decrypt:")
# if ch=='encrypt':
#     num=int(input("Enter the num of messages to encrypt:"))
#     for i in range(num):
#         word=input()
#         for char in word:
#             print(ord(char),end=" ")
#         print("")  
# elif ch=="decrypt":
#     num=int(input("Enter the num of messages to decrypt:"))
#     for i in range(num):
#         word=input()
#     for j in range(num):
#         for k in range(len(word)):
#             print(chr(word[k]),end="")
#         print("")  
# else:
#     print("Incorrect value!")
#---------------
# st=input()
# start=int(input("Enter start index:"))
# stop=int(input("Enter stop index:"))
# choice=input("Do you want to add a step (y/n)?")
# if choice=="y":
#     step=int(input("Enter a step:"))
#     print("The sliced string with step",step,":",st[start:stop:step])
# elif choice=="n":
#     print("The sliced string:",st[start:stop])
# else:
#     print("Incorrect value")
#---------------
# name=input("Enter your name:")
# pet=input("Enter your pet:")
# dest=input("Choose a destination:")
# print(f"{name}, along with his loyal {pet}, set out on an adventure to the {dest}. [Continue the story...]")
#---------------
# urlAd=input()
# print(urlAd[:7]+'...'+urlAd[-4:])
#---------------
# while True:
#     print(f"Input\n1. Start Game \n2. Load Game \n3. Exit")
#     opt=int(input("Choice:"))
#     if opt==3:
#         break
# print("Exiting the program")
#---------------
# c=0
# while c!=20:
#     c+=1
#     if(c%2!=0):
#         continue   
#     print(c)
#---------------
# num=int(input("Enter the num:"))
# if num<2:
#     print("Is not prime!")
# else:
#     for i in range (2,int(num**0.5)+1):
#         if num % i == 0:
#             print("Is not prime!")
#             break
#     else: 
#          print("Is prime!")
#---------------
# code = 12345
# while True:
#     ans=int(input("Enter code:"))
#     if ans!=code:
#         print("You entered wrong pass")
#     else:
#         break
# print("Correct! You've escaped!")
#----------------
# while True:
#     age = input("Enter your age:")
#     if age.isdigit():
#         age=int(age)
#         print(f"Age:{age}")
#         break
#     else:
#         print("Incorrect answer")
#----------------
# for hour in range(12,-1,-1):
#     for minute in range(59,-1,-1):
#         for second in range(59,-1,-1):
#             print(f"{hour} hours {minute} minutes {second} seconds")
#----------------
# rows=int(input("Enter the number of rows for the triangle:"))
# for i in range(1,rows+1):
#     print("*"*i)
#----------------
# rows=int(input("Enter the number of rows:"))
# cols=int(input("Enter the number of cols:"))
# for i in range(1,rows+1):
#     for j in range(cols):
#         print(i+j,end="")
#     print()
#----------------
# import random
# ran=random.randint(0,15)
# while True:
#     num=input()
#     if num.isdigit():
#         num=int(num)
#         if num==ran:
#             print("You guessed!")
#             break
#         else:
#             print("Enter 'exit' to leave or number to guess:",end="")
#             continue
#     elif num=="exit":
#         print(f"The correct number was {ran}> Better luck next time!")
#         break
#--------------
# rows=int(input("Enter the number of rows for the triangle:"))
# k=1
# for i in range(1,rows+1):
#     for j in range(rows):
#         print(i*k,end="")
#         k+=1
#     print()
# !!!!!!!!!!!!!!!
#--------------
# fact=int(input())
# f=0
# for i in range(1,fact+1):
#     i*=i
#     f=i
# print(f)
#--------------
# l1=[]
# while True:
#     print(f"Menu: \n1. Add an item\n2. Remove an item\n3. Modify an item\n4. Exit")
#     ch=int(input())
#     if ch==1:
#         it1=input("Enter an item to add:")
#         l1.append(it1)
#     elif ch==2:
#         it2=input("Enter an item to remove:")
#         l1.remove(it2)
#     elif ch==3:
#         it3=input("Enter an item to modify:")
#         it4=input("Enter new item:")
#         i=l1.index(it3)
#         l1[i]=it4
#     elif ch==4:
#         break
# print(l1)
#--------------
# ip=input()
# l_ip=ip.split(".")
# if len(l_ip)!=4:
#     print("Incorrect ip")
# else:
#     for i in range(len(l_ip)):
#         if l_ip[i].isdigit():
#             l_ip[i]=int(l_ip[i])
#             if l_ip[i]>=256 or l_ip[i]<=0:
#                 print("Incorrect ip")
#                 break
#             else:
#                 print(f"Your ip: {ip}")
#                 break
#--------------
# sl=input()
# sl_l=sl.split(" ")
# start=int(input("Enter start index for slicing:"))
# last=int(input("Enter last index for slicing:"))
# sliced=sl_l[start:last]
# print("Sliced list:", sliced)
#--------------
# info=[]
# name=input("Your name:")
# age=int(input("Your age:"))
# hobby=input("Enter your hobbies:")
# food=input("Enter your favourite food:")
# hobby_l=hobby.split(" ")
# food_l=food.split(" ")
# info.append(name)
# info.append(age)
# info.append(hobby_l)
# info.append(food_l)
# print(f"Name:{info[0]}\nAge:{info[1]}\nHobbies:{info[2]}\nFoods:{info[3]}")
#--------------
        


