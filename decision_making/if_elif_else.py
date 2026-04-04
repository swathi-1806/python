total_marks=int(input("enter total marks:"))
if total_marks>=80:
    print("grade A")        
elif total_marks>=65:
    print("grade B")    
elif total_marks>=45:
    print("grade C")     
else:
    print("grade F(failed)")
"""
output:
enter total marks:80
grade A
------------------------------
enter total marks:65
grade B
------------------------------
enter total marks:55
grade C

enter total marks:33
grade F(failed)
"""