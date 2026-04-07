year=int(input("enter the year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is a leap year")    
else:   
     print(year,"is not a leap year")

"""
output:
enter the year: 2004
2004 is a leap year
----------------------
enter the year: 2026
2026 is not a leap year
"""