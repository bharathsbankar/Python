def pattern():
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
if __name__=="__main__":
    pattern()
    print(" on branch1")