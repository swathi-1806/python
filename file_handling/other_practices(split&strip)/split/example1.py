f = open("C:/Users/swath/Desktop/git_repositories/python/file_handling/other_practices(split&strip)/file1.txt", "w")
f.write("pyhron is a open source language\n"
        "python is a high level language\n"
        "python is a interpreted language\n"
        "python is a object oriented language\n"
        "python is a easy to learn language\n"
        "we use python scripting language for verification\n")
f.close()

f = open("C:/Users/swath/Desktop/git_repositories/python/file_handling/other_practices(split&strip)/file1.txt", "r")
for line in f:
    #print(line)
    line = line.strip()  # Remove any trailing newline characters
    print(line)
f.close()

"""
pyhron is a open source language
python is a high level language
python is a interpreted language
python is a object oriented language
python is a easy to learn language
we use python scripting language for verification

"""