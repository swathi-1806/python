"""
we use split() to split the line into words and it will return a list of words in the line. we can iterate through the list of words and print each word in a new line.
without split()
pyhton is a open source language
with split()
pyhton
is
a
open
source
language
and we can also use splitlines() to split the content into lines and it will return a list of lines in the content. we can iterate through the list of lines and print each line in a new line.
without splitlines()    
pyhton is a open source language
with splitlines()
pyhton is a open source language
"""

f = open("C:/Users/swath/Desktop/git_repositories/python/file_handling/other_practices(split&strip)/file2.txt", "w")
f.write("pyhron is a open source language\n"
        "python is a high level language\n"
        "python is a interpreted language\n")
f.close()

f = open("C:/Users/swath/Desktop/git_repositories/python/file_handling/other_practices(split&strip)/file1.txt", "r")
for line in f:
    line = line.strip()
for word in line:
    word = word.split()
    print(line)
   
f.close()