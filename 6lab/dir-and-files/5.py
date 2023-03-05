import os

#path = open("new_file.txt", "x")

list = ["a","b"]

with open("new_file.txt", "w") as file:
    file.writelines([x + "\n" for x in list])
    file.close