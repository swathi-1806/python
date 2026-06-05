
f = open("C:/Users/swath/Desktop/git_repositories/python/file_handling/other_practices(split&strip)/file4.txt", "w")
f.write("pyhron is a open source language\n"
        "python is a high level language\n"
        "python is a interpreted language\n")
f.close()

f = open("C:/Users/swath/Desktop/git_repositories/python/file_handling/other_practices(split&strip)/file4.txt", "r")
for line in f:
    line = line.strip().split()
    print(line)
   
f.close()

"""
output:
['pyhron', 'is', 'a', 'open', 'source', 'language']
['python', 'is', 'a', 'high', 'level', 'language']
['python', 'is', 'a', 'interpreted', 'language']

"""