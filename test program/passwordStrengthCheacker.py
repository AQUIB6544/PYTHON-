password = input("ENTER YOUR PASSWORD:  ")
password__length = len(password)
if len(password) <=6:
    print("YOUR PASSWORD IS WEAK : ")
elif len(password) <= 10:
    print("YOUR PASSWORD IS MEDIUM")
else:
    print("YOU PASSWORD IS STRONG")