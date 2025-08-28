size = input("ENTER YOUR ORDER SIZE : ")
user = input("DO YOU WANT EXTRA SHOT ? (type true/false):").lower()
if user == "true":
    print("your coffee is",size,"size with extra shot")
elif user == "false":
    print("your coffee is",size,"without extra shot")
else:
    print("we are not that type of coffee 😅")
