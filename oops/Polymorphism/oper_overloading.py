# a=5
# b=6
# print(a+b)#==int.__add__(a,b)
# print(int.__add__(a,b))

################################3

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        obj=Student(m1,m2)
        return obj

    def __mul__(self, other):
        m1=self.m1*other.m1
        m2=self.m2*other.m2
        obj =Student(m1, m2)
        return obj
    def __lt__(self, other):
        return self.m1<other.m1

class Stud:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

s11=Student(15,65)
s22=Stud(25,53)
s33=s11+s22
s4=s11*s22
print("s33.m1=",s33.m1)
print("s4.m2=",s4.m2)
if s11<s22:
    print("s11<s22")
else:
    print("s22<s11")

