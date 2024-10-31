from numpy import *
# arr1=array([
#     [1,2,3],
#     [4,5,6]
# ])
# print(arr1.ndim)#shows dimension of array
# print(arr1.shape)#shows no  of (rows , columns)
# print(arr1)
# arr2=arr1.flatten()#it will convert 2d array to 1d array
# print(arr2)#which is 1d array
# #reshape() is used to convert 1d array to multi dimensiion array
#
# print(id(arr2))
#
# arr3=arr2.reshape(3,2)
# print("arr3i",id(arr3))
# arr3=arr3.flatten()
# print("arr3",id(arr3),arr3)
# print("arr2",id(arr2),arr2)
# # arr1=arr.reshape(3,2)
# # print("converted array",arr3)
# arr1=array([1,2,3,4,5,6,7,8])
# arr3=arr1.reshape(2,2,2)
# print("arr3",id(arr3)," ",arr3)
#
# arr2=array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print("arr1",id(arr1)," ",arr1)
# print("arr2",id(arr2)," ",arr2,"dimension: ",arr2.shape)
def matrix_3d_display(arr):
    if len(arr.shape)==3:
        a,b,c=arr.shape
        print("3d array")

        for i in range(a):
            print(i, "frame,(zaxis)")
            for j in range(b):
                for k in range(c):
                    print(arr[i,j, k],end=" ")
                print()
    else:
        print("2d array")

arr1=array([[[1,2],[3,4]],[[5,6],[7,8]]])
matrix_3d_display(arr1)
# m=matrix('1,2,3;4,5,6;7,8,9')
# n=matrix('10,11,12;13,14,15;16,17,18')
# print(m)
# print(n)
# print("diagonal matrix",diagonal(m))
# print("m+n",m+n)
# print("m*n",m*n)
#
