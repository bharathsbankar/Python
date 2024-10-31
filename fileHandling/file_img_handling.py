#copy image from bhar,jpg to new.jpgk

a=open("bhar.jpg","rb")
#rb=read binary
b=open("new.jpg","wb")
for i in a:
    b.write(i)
