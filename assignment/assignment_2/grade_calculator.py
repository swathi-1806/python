t=int(input("enter the telugu marks(t/100):"))
h=int(input("enter the hindi marks(h/100):"))
e=int(input("enter the english marks(e/100):"))
m=int(input("enter the maths marks(m/100):"))
s=int(input("enter the science marks(s/100):"))

total_marks=t+h+e+m+s
avg_marks=total_marks/5
percentage=(total_marks/500)*100
grade=""
if percentage>=80:
    grade="A"
elif percentage>=60:
    grade="B"   
elif percentage>=40:
    grade="C"
else:    grade="Fail"
print(f"total marks: {total_marks}")
print(f"average marks: {avg_marks}")
print(f"percentage: {percentage}%")
print(f"grade: {grade}")
