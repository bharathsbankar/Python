a=121
a=str(a)
b=[]
length=len(a)
for i in range(-1,-(length+1),-1):

    b.append(a[i])
    # print(b)
b="".join(b)
# print(a)
# print(b)
if(a==b):
    print(f"{a} is pallindrome")
else:
    print( f"{a} is not pallindrome")
#####################################################
# def func(string):
#     string=string.capitalize()
#     a=string.find("python")
#     b=[]
#     if(a!=-1):
#         b.append(string[0:a])
#         print(b)
#         b.append("data science")
#         print(b)
#         b.append(string[a+6:])
#         print(b)
#         return "".join(b)
# print(func("i love python and java"))
##############################################3
# def func(str1):
#     str1=str1.casefold()
#     str1=str1.replace("Python","Data Science")
#     str1=str1.capitalize()
#     print(str1)
# func("we learn Python everyday")

