n=7


def fib(n):
    a,b=0,1
    if n>=1:
        print(a,end=" ")
    if n>=2:
        print(b,end=" ")
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=" ")

fib(n)
print()
def fib_adv(num):

    if(num==1 ):
        print(0,end=" ")
    elif num==2:
        print(1,end=" ")
    else:
        a, b = 0, 1
        for i in range(2,num+2):
            c=a+b
            if(c>=num):
                print(b,end=" ")
                break;
            else:
                a=b
                b=c
fib_adv(n)



