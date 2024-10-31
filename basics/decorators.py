#
#
def abc(a, b):

    return a/b,a*b
def decorate(func):
    def inne(a, b):
        if a<0 :
            a=-a
        if b<0 :
            b=-b
        return func(a,b)
    return inne
print(f"before {list(abc(-5,2))}")
abc1=decorate(abc)#function is assigned to function
print("type of abc",type(abc1))
print(f"after {list(abc1(-5,2))}")






