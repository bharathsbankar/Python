class University:
    university="VTU"
    def __init__(self,degree):
        self.degree=degree
        self.clg=self.College()
    def show(self):
        print(self.university,self.degree)
    class College:
        def __init__(self,name="jit"):
            self.college=name
        def show(self):
            print(self.college)
s1=University("B.tech")
c1=s1.clg
s1.show()
c1.show()

