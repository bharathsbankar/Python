file = open("data.txt", "r")
# file.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n10")
total = 0
for line in file:
    total += int(line.strip()) # Convert each line to an integer and add to total

file.close()
print("The sum of the numbers is:", total)