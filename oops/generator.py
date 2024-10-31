


def SquaresOfFirstFive():
    n=1
    while n <=5:
        yield n*n
        n+=1

a=SquaresOfFirstFive()
# a=iter(list(range(1,6)))
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(type(a))
b=1
for i in a:
    print(i," ",b)
    b+=1



