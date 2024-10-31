# from functools import reduce
#
# a=list(range(0,10))
# print(a)
# evens=list(filter(lambda x:x%2==0,a))
#
# print(
#     evens)
# b=reduce(lambda a,b:a+b,evens)
# print(b)
#####################################
# c=filter(lambda x:x%2==1,range(0,10))
# print(tuple(c))
# from functools import reduce
# n=int(input("enter a number:"))
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print("using recursion :",fact(n+1))
# print("using lambda func :",reduce(lambda a,b:a*b,range(1,n+2)))
# a=3
# b=3
# print(id(a) == id(b),"a",id(a),"b",id(b))#2490756476368
# a+=1
# b-=4
# print(id(a) == id(b),"a",id(a),"b",id(b),id(3),id(10),id(24),id(-4))
a=5
print(a,id(a))
a+=3
print(a,id(a))