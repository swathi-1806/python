a=5
b=10
#addition
addition=a+b
print("ADDITION:{}+{}={}".format(a,b,addition))

#subtraction
subtraction=b-a
print("SUBTRACTION:{}-{}={}".format(b,a,subtraction))

#multiplication
multiplication=a*b
print("MULTIPLICATION:{}*{}={}".format(a,b,multiplication))

#division
division=a/b
print("DIVISION:{} / {} = {}".format(a, b, division))

#modulus
modulus=b%a
print("MODULUS:{} % {} = {}".format(b, a, modulus))     

#floor division
floor_division=b//a 
print("FLOOR DIVISION:{} // {} = {}".format(b, a, floor_division))

#exponentiation
exponentiation=b**a
print("EXPONENTIATION:{} ** {} = {}".format(b, a, exponentiation))    

"""
output:
ADDITION:5+10=15
SUBTRACTION:10-5=5
MULTIPLICATION:5*10=50
DIVISION:5 / 10 = 0.5
MODULUS:10 % 5 = 0
FLOOR DIVISION:10 // 5 = 2
EXPONENTIATION:10 ** 5 = 100000
"""
