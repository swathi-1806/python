"""
===================================================================================================================================================================================================
if we dont use strip() then it will print the line with the new line character(\n) and it will print an empty line after each line because of the new line character(\n) at the end of each line.
if we use strip() then it will remove the new line character(\n) at the end of each line and it will print the lines without any empty lines in between.
===================================================================================================================================================================================================
"""

f = open("C:/Users/swath/Desktop/git_repositories/python/file_handling/other_practices(split&strip)/file2.txt", "w")
f.write("pyhron is a open source language\n"
        "python is a high level language\n"
        "python is a interpreted language\n")
f.close()

f = open("C:/Users/swath/Desktop/git_repositories/python/file_handling/other_practices(split&strip)/file1.txt", "r")
for line in f:
    line = line.strip()
    print(line)
   
f.close()

"""
without strip()
pyhron is a open source language

python is a high level language

python is a interpreted language

python is a object oriented language

python is a easy to learn language

we use python scripting language for verification
------------------------------------------------------
with strip()
pyhron is a open source language
python is a high level language 
python is a interpreted language
python is a object oriented language
python is a easy to learn language
we use python scripting language for verification
"""
