# # if not 1<2:
# #     print("1")
# # elif 2<3:
# #     print("2")
# # else:
# #     print("else cond")
#####################################3
# # x={1,2,3,3,4,-1}
# # for i in [1,"bharath","tatha","siddarooda ajja","ajjaru","bharathi ajjaru"]:
# #     print(i)
# # i='b h'
# # if i[1]==' ':
# #     print("yeah!")
# # else :
# #     print("nope!!")
# ################################
# for i in range(1,3):
#     print(i," ", end=" ")
#     for j in range(1,5):
#         if 1>2:
#            break
#         if j==2:
#             break
#         # else:
#         #     print("hi",j ,end="|  ")
#     else:
#         print("yeap!!")
#
#     print()
# #######################################
# for i in  range(4,0,-1):
#     for j in range(0,i):
#         print("hi",end=" ")
#     print()
########################################3
# # prime number
# a = int(input("enter a number")[:3])
# count=0
# for i in range(1,a):
#     if a%i==0:
#         count+=1
# if count > 1:
#     print(a,'is not prime')
# else:
#     print(a," is prime")
#
# #########################
# #array reversing
# from math import ceil, floor
#
# a=[1,2,3,4,'hi']
# print("initial",a)
# end= floor(len(a)/2)
# b=len(a)-1
# for i in range(end):
#     temp=a[i]
#     a[i]=a[b]
#     a[b]=temp
#     b-=1
# print("final",a)

###############################
# from numpy import *
# a=array([1,2,3])
# b=array([1,2,3])
# print(a," ",id(a))
# b=a.copy()
# print(b," ",id(b))
# print(" -- ")
# b[1]=5
# print(a)
# print(b)

########################################
#
# a={1:"bharath",2:"avi"}
# print(a[2])
# a[2]='avi-2'
# print(a[2])
# b=1,2,3
# print(b[0])
# print(b[1])
# print(b[2])
#
#
# for i in b:
#     print(i)
################################
# a={1,2,2,3}
# print(a)
# a.remove(3)
# print(a)
# a.add('asas')
# print(a)
print(5|7)


