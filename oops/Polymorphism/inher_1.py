# ---------duck typing--------------

class A:
    @staticmethod
    def execute():
        print("A executed")

class B:
    def execute(self):
        print("B executed")
class C:
    def func(self,obj):
        A.execute()
        
obj_A=A()
obj_B=B()
obj_C=C()
obj_C.func(obj_A)