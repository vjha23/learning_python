# file io basics
"""
"r"- open file for reading - default
"w"- open a file for wrinting
"x"- create file if not exists
"a"-add more content to a file
"t"-text mode - default
"b"-binary mode
"+"- read and write both
"""
"""f=open("vijay.txt","rt")  # here f is a file pointer in which open returns to this file pointer
content=f.read(12)
print(content)
f.close() # closing file always a good option
"""
# for reading line by line file
"""f=open("vijay.txt")
content=f.read()

#for line in content:
 #   print(line) # it will print line by line
f.close()
f=open("bunty.txt","r+") # r+ for read and write both
f.write("my name is bunty")
print(f.read())
f.close
"""
"""f=open("vijay.txt")
#print(f.tell()) # basically it tells about the file pointers where it lies
print(f.readline())
#print(f.tell())
f.seek(0) # seek func used to reset the file pointer from the position
print(f.readline())# so we have to run again and again in this to avoid this we use
#print(f.tell())
f.close()
"""
# opening file with block
with open("vijay.txt") as f: # benifit of using this we dont have to close the file
    a=f.read(4)
    print(a)


