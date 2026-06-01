
f = open("C:/Users/swath/Desktop/python/my_python/file_handling/t1.txt", "w")

f.write("welcome to india\n"
        "india is a beautiful country\n"
        "india is known for its rich culture and heritage\n"
        "india is a land of diversity and unity\n"
        "india is a country of festivals and celebrations\n" 
)
f.close()

f = open("C:/Users/swath/Desktop/python/my_python/file_handling/t1.txt", "r")
content = f.read()f = open("C:/Users/swath/Desktop/python/my_python/file_handling/t1.txt", "r")
content = f.read()
print(content)
f.close()
print(content)
f.close()
