


#################################################

# # code for number of comparisons in bubble sort for n elements
# from functools import reduce
# def Comparisons_BubbleSort(n):
#     res=reduce(lambda a,b : a+b ,range(1,n))
#     return res
# a=int(input("enter number of elements :"))
# print(f"number of comparisons in buuble sort for {a} elements would be :{Comparisons_BubbleSort(a)}")
#
# ##########################################
# #code to check number of comparisons in bubble sort for n elements using recursion
#
def func(n):
    if n==1:
        return 1
    else:
        return n+func(n-1)

# print(f"no. of comparisons for {a} elements would be {func(a-1)}")
#
#
# ##################################################

#bubble sort implementation
list=[1,4,2,5,3]
print(f"list {list}")
def bubbleSort(list):
    global a
    a=0
    for i in range(1,len(list)):
        for j in range(len(list)-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                a+=1

    return list
compar=func(len(list)-1)
print(f"list  after sorting : "
      f"{bubbleSort(list)}"
      f"\nand number of comparisons taken is {compar} \n and no.. of swapings is {a} for {len(list)} elements ")
