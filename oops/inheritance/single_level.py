#single level inheritance
class A:
    def func(self):
        print("A")
class B(A):
    def func(self,name):#overriding
        self.name=name
        print("B",self.name)
b=B()
b.func(
    "bharath")

