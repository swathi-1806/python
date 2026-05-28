"""
Checks whether all elements of A are present in B.
"""

A = {1, 2}
B = {1, 2, 3, 4}
C = {10,"apple"}

D= A.issubset(B)
E= B.issubset(C)
print(D)
print(E)
"""
True
False
"""
