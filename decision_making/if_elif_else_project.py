"""
-->create a basic calculator programm that performs addition , subtraction, multiplication, and division
-->ask the user to enter two numbers and choose an operation
-->display the result accordingly
"""
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
operation=input("choose an operation (+, -, *, /):")
if operation=="+":
    result=num1+num2
    print(f"addition: {result}")
elif operation=="-":
    result=num1-num2
    print(f"subtraction: {result}")
elif operation=="*":
    result=num1*num2
    print(f"multiplication: {result}")
elif operation=="/":
    if num2!=0:
        result=num1/num2
        print(f"division: {result}")
    else:
        print("error: division by zero is not allowed")
else:
    print("invalid operation")

    
"""
output:
enter first number:100
enter second number:50
choose an operation (+, -, *, /):+
addition: 150
---------------------------------------
enter first number:100
enter second number:50
choose an operation (+, -, *, /):-
subtraction: 50
---------------------------------------
enter first number:100
enter second number:50
choose an operation (+, -, *, /):*
multiplication: 5000
---------------------------------------
enter first number:100
enter second number:50
choose an operation (+, -, *, /):/
division: 2.0
----------------------------------------
enter first number:100
enter second number:0
choose an operation (+, -, *, /):/
error: division by zero is not allowed
"""