#multiple inputs
name,branch=input("enter name and branch:").split()
print(name,branch)

#convert multiple inputs to integer
a,b=map(int,input("enter two numbers:").split())
print(a,b)

#list_inputs
numbers=list(map(int,input("enter numbers:").split()))
print(numbers)


"""
output:
---------------------------------
enter name and branch:swathi ece
swathi ece
---------------------------------
enter two numbers:5 10
5 10
---------------------------------
enter numbers:2 4 6 8 10 12 14
[2, 4, 6, 8, 10, 12, 14]
----------------------------------

"""
