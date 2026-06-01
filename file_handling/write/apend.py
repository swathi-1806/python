## append : it is used to erite the dat into the file in won't override

# ================================================================================================

"""
a file consists of data

This is my first file handling program in python
I am learning how to read and write files in python
File handling is an important concept in programming
With file handling, we can create, read, update, and delete files in python
File handling is a powerful tool for data storage and manipulation in python
"""
# ================================================================================================

f = open("C:/Users/swath/Desktop/python/my_python/file_handling/t1.txt", "a")

f.write("1001\n"
        "1010\n"
        "FFFF\n"
        "EF11\n"
        "10AB\n"
        "ABCD\n"     
)

f.close()

"""
now file consists of :

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

        
