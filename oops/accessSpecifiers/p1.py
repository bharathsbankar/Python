#access specifiers
#public:
    #public members can be accessed by any members from same or different class
    #by default all members were public
#protected:
    #protected members can be accessed fro either same class or sub class only
    #'_' character must be used as prefix to define members as protected
    #ex:_name;def _abx()
#private:
    #private members can be accessed from same class only
    #'__' character must be used as prefix to define members as private
    #ex:__name;def __abx()

class A:
    def __init__(self):
        self.name="bharath"
    def _aFunc(self,var):
        print("A ",var)
    pass
class B(A):
    def bFunc(self,var):
        print("B ",var)
        print("---",A.name)
    pass
class C:
    def cFunc(self,var):
        print("C ",var)
        A._aFunc(obj,var)
    pass
if __name__=="__main__":
    obj=B()
    o=A()
    # C.cFunc("hello")
    obj.bFunc("hi")

    # print(A.aFunc(obj,"hi"))
    pass