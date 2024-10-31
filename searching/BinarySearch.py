#for binary search the elements must be sorted
#binary search is applicable only for natural numbers
#n=lenth of list
#low=0,high=n-1
#mid=(low+high)//2
b=int(input("enter number of elements : "))
list=list(range(b))
print(list)
key=int(input("enter a key to search in a list : "))
pos=-1
def search(list,key):
    low=0
    high=len(list)-1
    global a
    a=0
    while low<=high:
        mid=(low+high)//2

        if list[mid]==key:
            a += 1

            globals()["pos"]=mid
            return True

        elif list[mid]<key:
            a+=2

            low=mid+1
        else:
            a+=2
            high=mid-1


if search(list,key):
    print(key,"found at position : ",pos+1)
else:
    print(key,"not found")

print("number of comparisons  for list ",len(list), " using binary search would be : ",a)




