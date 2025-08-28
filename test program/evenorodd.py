try:
   A = float(input("ENTER A NUMBER:-"))

   if(A%2==0):
    print("NUMBER IS EVEN")
   else:
    print("NUMBER IS ODD")
except ValueError:
  print("Please enter a valid integer.")