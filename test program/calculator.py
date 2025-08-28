# SIMPLE CALCULATOR 
# TAKE INPUTS
user_input1 = float(input("ENTER YOUR FIRST NUMBER :- "))
user_input2 = input("ENTER OPERATOR ( + , - , * , / , % ,): ")
user_input3 = float(input("ENTER YOUR SECOUND NUMBER :- "))
# CALCULATION
if user_input2 == "+" :
    print("YOUR ADDITION IS:- ",user_input1+user_input3)
elif user_input2 == "-" :
    print("YOUR SUBTRACTION IS:- ",user_input1-user_input3) 
elif user_input2 == "*" :
    print("YOUR MULTIPLICATION IS:- ",user_input1*user_input3)
elif user_input2 == "/" :
    if user_input3!=0:
        print("RESULT:", user_input1/user_input3)
    else:
        print("ERROR: DIVISION BY ZERO NOT ALLOWED.")
elif user_input2 == "%" :
    if user_input3 !=0:
        print("RESULT",user_input1%user_input3)
    else:
        print("ERROR: MODULUS BY ZERO NOT ALLOWED.")
else:
    print("INVALID OPERATOR ! PLEASE USE + , - , * , /  or % ")

