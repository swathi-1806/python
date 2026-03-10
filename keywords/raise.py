age =int (input("enter your age:"))
if age < 0:
    raise ValueError("invalid age: ")
else:
    print("your age is", age)