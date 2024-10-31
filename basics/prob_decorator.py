'''Q)count the sum of odd and even elements ina list'''
p=range(0,100)
print(f"sum of numbers from 0 to 99 : {sum(p)} , id {id(p)}")
def decor_evenfunc(sum):
    def inner_func(p):
        # p=p.copy()
        print(f"id(p) in decorating : {id(p)} ")
        p=list(filter(lambda x:x%2==0,p))
        print(f"id(p) after filtering : {id(p)} ")
        return sum(p)
    return inner_func
print(f"id(sum) before decorating : {id(sum)} ")
sum=decor_evenfunc(sum)
print(f"id(sum) after decorating : {id(sum)} ")
print("sum of even numbers from 0 to 99 : ",sum(range(0,100)))

# print(f"sum {sum(range(1,100,2))}")