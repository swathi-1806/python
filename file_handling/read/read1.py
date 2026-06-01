f= open("C:/Users/swath/Desktop/python/my_python/file_handling/t1.bin", "wb")
f.write(b"101010\n"
        b"111111\n"
        b"101001\n")
f.close()

f= open("C:/Users/swath/Desktop/python/my_python/file_handling/t1.bin", "rb")    
content = f.read()
print(content)
f.close()

"""
=======================================================================================================
101010
111111
101001
=======================================================================================================
"""
