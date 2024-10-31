#to print the sum of n natural numbers using recursion
def recur(n):
    if(n==1):
        return 1
    else:
        return n+recur(n-1)

    pass

n=100
print(recur(n))