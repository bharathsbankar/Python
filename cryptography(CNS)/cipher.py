# if "a"=="A":
#     print("true")
# else:
#     print("false")
#######################
from numpy.lib.recfunctions import join_by
def func():
    upperCase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowerCase='abcdefghijklmnopqrstuvwxyz'
    # if not upperCase.islower():
    #     print("upper")
    # else:
    #     print("lower")
    text=input("Enter the text")
    cipher=list()
    for i in text:

        if i.isupper():
            for j in upperCase:
                if i==j:

                    a=(upperCase.index(j)+3)%26
                    print(upperCase[a],end=" ")
                    cipher.append(upperCase[a])
                    break
        else:
            for j in lowerCase:
                if i==j:
                    a=(lowerCase.index(j)+3)%26
                    print(lowerCase[a],end=" ")
                    cipher.append(lowerCase[a])
                    break

    print()
    cipher="".join(cipher)
    print(f"cipher text : {cipher}")

if __name__=='__main__':
    func()
