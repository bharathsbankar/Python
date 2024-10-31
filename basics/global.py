def bcd():
    print("bcd func call",n)

def abc():
    print("function call")
    global n
    n=5

    bcd()
abc()
print(n)
