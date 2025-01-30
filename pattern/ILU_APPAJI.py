def I():
    for i in range(4):
        #character :I
        for j in range(5):
            if i == 0 or i == 3:
                print("I", end="  ")
            elif i != 0 and i != 3 and j == 2:
                print("I", end="  ")
            else:
                print(" ", end="  ")
        #character :heart
        for j in range(5):
            if i == 0 and j % 2 != 0:
                print(" *", end="  ")
            elif i == 1 and j % 2 == 0:
                print(" *", end="  ")
            elif i == 2 and j % 2 != 0:
                print(" *", end="  ")
            elif i == 3 and j == 2:
                print(" *", end="  ")
            else:
                print("  ", end="  ")
        #character : U
        for j in range(5):
            if j == 0 or j == 4:
                print("U", end="  ")
            elif i == 3:
                print("U", end="  ")
            else:
                print(" ", end="  ")
        print()
    print()
def appaji():
    for i in range(4):
        # character: A
        for j in range(7):
            if i == 0 and j == 3:
                print("A", end="  ")
            elif i == 1 and j in [2, 4]:
                print("A", end="  ")
            elif i == 2 and j in [1, 2, 3, 4, 5]:
                print("A", end="  ")
            elif i == 3 and j in [0, 6]:
                print("A", end="  ")
            else:
                print(" ", end="  ")
        # character : p
        for j in range(2, 5):
            if j == 2:
                print(" P", end="  ")
            elif j == 4 and i < 3:
                print(" P", end="  ")
            elif j == 3 and i % 2 == 0:
                print(" P", end="  ")

            else:
                print("  ", end="  ")

        # character : P
        for j in range(2, 5):
            if j == 2:
                print(" P", end="  ")
            elif j == 4 and i < 3:
                print(" P", end="  ")
            elif j == 3 and i % 2 == 0:
                print(" P", end="  ")

            else:
                print("  ", end="  ")
        # character : A
        for j in range(7):
            if i == 0 and j == 3:
                print("A", end="  ")
            elif i == 1 and j in [2, 4]:
                print("A", end="  ")
            elif i == 2 and j in [1, 2, 3, 4, 5]:
                print("A", end="  ")
            elif i == 3 and j in [0, 6]:
                print("A", end="  ")
            else:
                print(" ", end="  ")
        # character : J
        for j in range(5):
            if i==0:
                print(" J", end="  ")
            elif i in [1,2] and j==2:
                print(" J", end="  ")
            elif i==3 and j<3:
                print(" J", end="  ")
            else:
                print("  ", end="  ")
        #character:I
        for j in range(5):
            if i == 0 or i == 3:
                print("I", end="  ")
            elif i != 0 and i != 3 and j == 2:
                print("I", end="  ")
            else:
                print(" ", end="  ")


        print()



if __name__=="__main__":
    print("-----------------------------------------------------------------------------------------------------")
    I()
    print("-----------------------------------------------------------------------------------------------------")
    appaji()
    print("-----------------------------------------------------------------------------------------------------")

