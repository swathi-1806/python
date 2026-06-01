"""
# always we have to use "/" while giving path 
# if we use "\" then it will give error--> in this case we can use  is (r"C:\Users\swath\Desktop\projrcts\sv project\memory\common.sv", "r")

f = open("C:/Users/swath/Desktop/projrcts/sv project/memory/common.sv", "r")
content = f.read()
print(content)
f.close()
"""


f = open(r"C:\Users\swath\Desktop\projrcts\sv project\memory\common.sv", "r")
content = f.read()
print(content)
f.close()
