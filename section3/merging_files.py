import glob2
from datetime import datetime
filenames = glob2.glob("file*.txt")  # listing file in directory
now = datetime.now()  # creating time delta object
temp=now.strftime("%Y-%m-%d-%H-%M-%S-%f")  # time delta object in string formate store in temp variable to be use as file name
with open(temp+".txt" ,"w") as myfile:  #this do open a file to write with .txt extension
    for f in filenames:
        with open(f , "r") as tempf:  # this open file to read whcih we are going to wirte
            myfile.write(tempf.read() + "\n") # final approach
