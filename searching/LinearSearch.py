b=int(input("enter number of elements : "))
list=list(range(b))
print(list)
key=int(input("enter a key to search in a list : "))

def search(list,key):
    global i

    for i in range(len(list)):
        if list[i]==key:

            return True
    return False

if search(list,key):
    print(key,"found at position : ",i+1)
else:
    print(key,"not found")
#worst case is when element is found at either last position in alist or not present at all
print("number of comparisons  is : ",i+1)


