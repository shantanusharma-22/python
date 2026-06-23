#File i/o in python
#python can be used to perform operation on a file.(read & write data)
#open,read&close file 

#we have to open a file beffore reading or writing 
f=open("file__name","mode")
data=f.read()
f.close() 

#r-open for reading (default)
#w-open for writing,trucating the file first
#x-create a new file and open it for writing 
#a-open for wrriting,appending to the end of the file if it exists
#b-binary mode
#t-text mode(default)
#+-open a disk file for updating (reading and writimg)

#reading a file 
data = f.read()   #read entire file
data = f.readlines()  #reads one line at a time

#writing to a file
f = open("demo.txt","w")
f.write("this is a new line") #overwrites the entire file

f =open("demo.txt","a")
f.write("this is a new line") #adds to the file

#with syntax
with open ("demo.txt","a") as f:
    data = f.read()
#deleting a file
#using the os module module 
#module(like a code library) is a file written by another programmer that generally has a function we can use
from fileinput import filename
import os
os.remove(filename)

#q1
with open("practice.txt","r") as f:
    data = f.read() 

new_data=data.replace ("java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

#q2
word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) !=-1):
        print("found")
    else:
        print("not found")

#q3
def check_for_line():
    word = "learning"
    data = True
    line_no =1
    with open ("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1

#q4
num = ""
for i in range(len(data)):
    if (data[i]==","):
        print(int(num))
        num=""
    else:
        num+=data[i]
