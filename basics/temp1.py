# from numpy import *
# # def abc(x):
# #     x+=1
# #     print("x",id(x))
# # a=10
# # abc(a)
# # print("a",id(a))
# set={1,2,3,3}
# set2=set.copy()
# set2.add(5)
# print(set)
# print(set2)
#
# print(id(set))
# print(id(set2))
#
# a=1
# print(a," ",id(a))
# def func():
#     a=10
#     print(a," ",id(a))
# func()
# print("outside func:",a)
s=[]
top=-1
size=None
def push(item):
    global top

    if top < size-1:
        top += 1
        s.insert(top,item)

    else:
        print("stack overflow")
def pop():
    global top
    s.pop()
    top-=1

def display():
    global top
    for i in range(0,top+1):
        print(s[i])
size=int(input("enter length of stack")[:2])
#item=int(input("enter the item to push"))
push(10)
push(20)
push(30)
push(40)
print(s)
display()
pop()
display()

