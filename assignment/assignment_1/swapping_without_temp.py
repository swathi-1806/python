a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(f"before swapping a={a},b={b}",sep=",")
a=a+b
b=a-b
a=a-b
print(f"after swapping a={a},b={b}",sep=",")

"""
output:-
enter a value:5
enter b value:10
before swapping a=5,b=10
after swapping a=10,b=5
"""
