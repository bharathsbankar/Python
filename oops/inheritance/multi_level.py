class A:
    def func(self):
        print("A")
class B(A):
    def funcb(self):
        print("B")

class C(B):
    def funcc(self):
        print("C")
    def __str__(self):
        return f"multilevel inheritance"
obj = C()
print(obj)