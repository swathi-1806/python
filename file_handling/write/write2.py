"""
a t1,txt file consistes of below data 
instead of append(a) if we use write ("w") then the the entire data (content) will be replaced by new data

This is my first file handling program in python
I am learning how to read and write files in python
File handling is an important concept in programming
With file handling, we can create, read, update, and delete files in python
File handling is a powerful tool for data storage and manipulation in python1001
1010
FFFF
EF11
10AB
ABCD

"""

f = open("C:/Users/swath/Desktop/python/my_python/file_handling/t1.txt", "w")

f.write("welcome to india\n"
        "india is a beautiful country\n"
        "india is known for its rich culture and heritage\n"
        "india is a land of diversity and unity\n"
        "india is a country of festivals and celebrations\n" 
)
f.close()

f = open("C:/Users/swath/Desktop/python/my_python/file_handling/t1.txt", "r")
content = f.read()
print(content)
f.close()


"""
output:
welcome to india
india is a beautiful country
india is known for its rich culture and heritage
india is a land of diversity and unity
india is a country of festivals and celebrations
"""
