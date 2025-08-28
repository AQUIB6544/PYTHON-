age = int(input("ENTER YOUR age :-  "))
day = str(input("ENTER DAY :-  "))
day1 = "sunday"
day2 = "monday"
day3 = "tuesday"
day4 = "wednesday"
day5 = "thuresday"
day6 = "friday"
day7 = "staturday"

price = 12 if age >= 18 else 8

if day == "wednesday":
    price -= 2 
print(price)