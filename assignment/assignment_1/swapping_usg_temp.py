a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(f"before swapping a={a},b={b}",sep=",")
temp=a
a=b
b=temp
print(f"after swapping a={a},b={b}",sep=",")

"""
output:
enter a value:50
enter b value:100
before swapping a=50,b=100
after swapping a=100,b=50
"""
