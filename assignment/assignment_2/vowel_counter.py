input=input("enter your message:")
s=input.lower()

a=s.count('a')
e=s.count('e')
i=s.count('i')
o=s.count('o')
u=s.count('u')  
print(f"number of vowels: {a+e+i+o+u}")

"""
output:
enter your message:python is easy programming language
number of vowels: 11]
"""