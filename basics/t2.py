# # # def func(list):
# # #     list=list.copy()
# # #     list[0] = 3
# # #     print("kst:",id(list) , list)
# # #
# # #     pass
# # # k=[1,2,3,4,5,6]
# # # print("k1:",id(k),k)
# # # func(k)
# # # print("k2:",id(k),k)
# # # print(f"id(k)={id(k)} and id(k[0])={id(k[0])}")
# # # sum=lambda a,b:a+b
# # # print(sum(4,8))
# # a=5
# # print(f"a : {a} \nid(a)={id(a)}")
# # a=6
# # print(f"a : {a} \nid(a)={id(a)}")
# # b=5
# # print(f"b : {b} \nid(b)={id(b)}")
# #
# #
# # def abc(x):
# #     return x%2==0
# # a=list(filter(abc,range(1,10)))
# # print(a)
# nb=dict(zip(['a','b','c'],list(range(1,4))))
# print(f"before function call- n : {nb} , id(n)={id(nb)}")
# def a(n):
#     n= n.copy()
#     n['a']=30
#     print("after function call",n,id(n))
# a(nb)
# print("after function call",nb,id(nb))
from array import *
arr=array('i',[])
size=int(input("enter the length of array"))
for i in range(0,size):
    val=int(input("enter the value"))
    arr.append(val)
sear_val=int(input("enter the value to be searched"))
try:
    index=arr.index(sear_val)
    print(f"sear_val : {sear_val} , index {index}")
except ValueError:
    print("value not found")
###
# my_list = [1, 2, 3, 4, 6, 7]
# a=int(input("enter the index value"))
# try:
#     print(my_list[a])
# except IndexError:
#     print("The index value is out of the range")
# ###############