"""duck typing"""

class A:
    @staticmethod
    def execute():
        print("A executed")
        return 2
class B:
    def execute(self):
        print("B executed")
class C:
    def func(self,obj):
        b=A.execute()
        print(b)
obj_A=A()
obj_B=B()
obj_C=C()
obj_C.func(obj_A)