# class Student:
#     def __init__(self,name,usn):
#         self.name_s=name
#         usn_s=usn
#         print(f"student of object  with name {self.name_s} and usn {usn_s} created")
#     name_s=""
#     usn_s=""
#     print("hiiiiiiiii")
# s1=Student("bharath",'1jt21cs026')
# s2=Student("akshay","1jt21cs008")
# print(s1.name_s)
# s1.name_s="ani"
# print(s1.__init__("sriki","1jt21cs028"))
from numpy import array
class Matrix:
    def __init__(self,r,c):
        self.r=r
        self.c=c
    def __str__(self):
        return f"row={self.r} and column={self.c}"
    def create(self,list):
        print(f"list : {list} , list id({id(list)}) ")
        self.list=list
        self.list[0]=10
        print(f"list : {list} , list id({id(list)}) ")
        print(f"self.list : {self.list} , self.list id({id(self.list)}) ")
        # print(list)
        list=array(list)
        list=list.reshape(self.r,self.c
                     )
        print(list,list.shape)
m1=Matrix(2,3)
print(m1)
a=m1.r*m1.c
mat=list()
for i in range(a):
    value=int(input("enter the value"))
    mat.append(value)
print(f"<mat> -> list : {mat} , list id({id(mat)}) ")
m1.create(mat)
print(f"<mat> -> list : {mat} , list id({id(mat)}) ")