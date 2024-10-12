# https://  7
user_link = input("Input a full URL link: ")

if ("https://" in user_link) and (user_link[0:8] != "https://"):
    print("You put https:// in the wrong position :o Let me fix it for you:")
    user_link = "https://" + user_link.replace("https://", "")
    print(user_link)
elif ("https://" not in user_link):
    print("You forgot your https:// !!! Let me fix it for you:")
    user_link = "https://" + user_link
    print(user_link)

# it would be cool to check for .com, .net, etc. But the assignment doesn't ask me to do it, so I won't :P