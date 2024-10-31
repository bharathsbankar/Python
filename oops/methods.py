
class Student:
    clg="jit"
    university="VTU"
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3


    def __str__(self):
        return self.name+" "+self.clg

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls ):
        return  cls.university +" , "+cls.clg



    @staticmethod
    def fact(n):
        if n==0:
            return 1
        else:
            return n*Student.fact(n-1)

s1=Student("bharath",12,5,34)
s2=Student("arun",21,4,43)
Student.clg="JICM"
s1.clg="ksit"
print(s1.info() , s1.clg)
print(Student.clg,Student.info())
print(Student.fact(s2.m2))
