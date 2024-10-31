class Student:
    college = "jit"#class variable which will be common to all objects
    def __init__(self,name,m1,m2,m3):

        self.name = name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def __str__(self):
        return self.name+" "+self.college

    def fact(self,n):
        Student.factoria_l(n)

    @staticmethod
    def factoria_l(n):
        if n == 0:
            return 1
        else:
            return n * (n - 1)
a=Student("bharath",12,23,54)
b=Student("ajja",34,43,23)
print(a.name)
print(a.college)
a.college="ksit"
Student.college="RNsit"
print(f"b.name {b.name} , b.college {b.college}")
print(a.factoria_l(5))


print(a.college)
print(a)