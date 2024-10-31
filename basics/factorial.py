x=int(input("enter a number :")[:2])


def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
    print(result,id(result))
    return result



result=fact(x)
print(result, id(result))

print(f"factorial result is {result}")