"""
Returns True → if both sets have no common elements
Returns False → if at least one element is common
"""

a = {1, 2, 3}
b = {4, 5, 6}
c = a.isdisjoint(b)
print(c)


"""
output
True
"""
