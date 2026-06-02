f = open("C:/Users/swath/Desktop/git_repositories/python/file_handling/other_practices(split&strip)/file2.txt", "w")
f.write("pyhron is a open source language\n"
        "python is a high level language\n"
        "python is a interpreted language\n")
f.close()

f = open("C:/Users/swath/Desktop/git_repositories/python/file_handling/other_practices(split&strip)/file1.txt", "r")
content = f.read()
for line in content:
    print(line)
   
f.close()

"""
====================================================================
f.read() returns the entire file as one string.
for line in content:

Python iterates through the string one character at a time

we have to use  methods like 
- read line by line using readline() or readlines()
- split the content into lines using splitlines() or split("\n")
- use strip() to remove any leading or trailing whitespace characters from each line

====================================================================

p
y
h
r
o
n
 
i
s
 
a
 
o
p
e
n
 
s
o
u
r
c
e
 
l
a
n
g
u
a
g
e


p
y
t
h
o
n
 
i
s
 
a
 
h
i
g
h
 
l
e
v
e
l
 
l
a
n
g
u
a
g
e


p
y
t
h
o
n
 
i
s
 
a
 
i
n
t
e
r
p
r
e
t
e
d
 
l
a
n
g
u
a
g
e


p
y
t
h
o
n
 
i
s
 
a
 
o
b
j
e
c
t
 
o
r
i
e
n
t
e
d
 
l
a
n
g
u
a
g
e


p
y
t
h
o
n
 
i
s
 
a
 
e
a
s
y
 
t
o
 
l
e
a
r
n
 
l
a
n
g
u
a
g
e


w
e
 
u
s
e
 
p
y
t
h
o
n
 
s
c
r
i
p
t
i
n
g
 
l
a
n
g
u
a
g
e
 
f
o
r
 
v
e
r
i
f
i
c
a
t
i
o
n
"""