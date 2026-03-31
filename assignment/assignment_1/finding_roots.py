a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
root1=0
root2=0
d=b**2-(4*a*c)
root1=((-b)+(d**0.5))/(2*a)
root2=((-b)-(d**0.5))/(2*a)         
print(f"roots=({root1},{root2})")


"""
output:-
enter a value:1
enter b value:-3
enter c value:2
roots=(2.0,1.0)
"""
