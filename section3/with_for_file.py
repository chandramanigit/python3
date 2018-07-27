#this script shows how can we use with to work with file

with open("example.txt" , "w") as myfile:
    myfile.write("writing to my file")

# by using with method we dont need to close the file as required in below
"""
myfile = open("example1.txt" , "w")
myfile.write("ting using old method")
myfile.close()
"""
