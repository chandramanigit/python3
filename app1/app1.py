import json
import difflib
from difflib import get_close_matches
data= json.load(open("H:\\PYTHON_2018\\PROJECTS\\Project1_dictionary\\data.json"))  # reading the data file and converting to dict format
def dict_search(word):  #defining function
    word=word.lower()  #converting string to lower case
    if word in data:
        result=data[word]  #storing result in LIST format under one variable
        a=len(result)  #now cheking lenth of list to display line by line using while loop
        i=0
        while i < a:
            print(i+1 , result[i])
            i=i+1
    else:
        print("not found")

w = input("enter the word:")
dict_search(w)
