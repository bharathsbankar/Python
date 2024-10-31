import os
filename = "data.txt"
try:
    if os.path.exists(filename):
        file = open(filename, "r")
        print(file.read())
        file.close()
    else:
        print(f"The file {filename} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")