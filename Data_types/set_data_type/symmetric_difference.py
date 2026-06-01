## removes the common elements

x = {"a","b","c",3,4}
y= {1,2,3,"c"}
z= x.symmetric_difference(y)
print(z)

"""
{1, 2, 4, 'a', 'b'}
"""
