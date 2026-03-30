#temperature converter

t=int(input("enter temperature:"))
u=input("enter unit of temperature (C/F/k):")
if u=="C":
    f=(t*9/5)+32
    k=t+273.15
    print(f"temperature in fahrenheit is:{f}F")
    print(f"temperature in kelvin is:{k}K")
elif u=="F":
    c=(t-32)*5/9    
    k=(t-32)*5/9+273.15
    print(f"temperature in celsius is:{c}C")
    print(f"temperature in kelvin is:{k}K")
elif u=="k":
    c=t-273.15
    f=(t-273.15)*9/5+32
    print(f"temperature in celsius is:{c}C")
    print(f"temperature in fahrenheit is:{f}F")
else:
    print("invalid unit of temperature")

"""
OUTPUT:-

enter temperature:32
enter unit of temperature (C/F/k):C
temperature in fahrenheit is:89.6F
temperature in kelvin is:305.15K
"""
