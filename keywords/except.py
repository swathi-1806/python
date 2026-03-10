try:
  x = int(input("enter the value:"))
  y=10/x
except zeroDivisionError:
  print("division by zero error")
except valueError:
  print("invalid input")
finally:
  print("programm completed")

"""
Enter number: 5
Program finished
-----------------------
Enter number: 0
Division by zero error
Program finished
----------------------
Enter number: x
Invalid input
Program finished
"""
