a=open("file.txt","r")
#open(filename,mode)
"""
modes
w-write
r-read
a-append
r+ : read or write
rb : read binary
wb : write binary
"""""
b=open("file1.txt","w")
for data in a:
    b.write(data)
