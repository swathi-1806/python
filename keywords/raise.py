age =int (input("enter your age:"))
if age < 0:
    raise ValueError("invalid age: ")
else:
    print("your age is", age)

"""
enter your age:21
your age is 21
---------------------
enter your age:-5
ValueError: invalid age:
"""

