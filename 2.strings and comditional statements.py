str1='shantanu' #it is a string that stores data type 
str2="raam"
str3="'ghjgjhg'"
print (str1+str2)#this operation is called concatenation
print (len(str1))#here len is used to find length of string 
str4="ram.\n shan "#here \n is a escaping sequence character which is used to to change the paragraph
print (str4)
str5="st\tsr"#\t helps to tab space between them
print(str5)
#indexing position it start from 0 here 
str7="apna-shool"
print(str7[2]) #here str7[2]is "n"
#str7='b' is not allowed
str="bhavyta sharma "
print(str[1:4])#the selected part from the string is selected is called slicing the counting start from 0 and it count from left to write
print(str[-3:-1])#slicing through negative index it start from -1 and from right to left 

#string function
print (str.endswith("ma")) #return true if string ends with substr
print(str.capitalize()) #capitalize 1st char
print(str.replace("a","b")) #replaces all occurance of old with new
print (str.find("a")) #return the 1st index of 1st occurance
print (str.count("a"))#count the occurance of substr in string

#Q1
name=input("enter your name")
print(len(name))

#conditional statements
#if-elif-else(syntax)
var="b"
if (var == "a") :       #if(condition):,statement1
    print("apple") 
elif(var=="b"):
    print("ball")

 #Q1
marks=int(input("Enter your number :"))
if(marks>=90):
    print("grade:A")
elif(90>marks>=80):
    print("grade:B")
elif(80>marks>=70):
    print("grade:c")
elif(70>marks>=60):
    print("grade :d")
else:
    print("fail")


#nesting 
if(var=="a"):
    if(var=="b"):
        print("ball")
    else:
        print("apple")

#Q1
a=int(input ("number"))
if(a % 2==0):
    print("even")
else:
    print("odd")

 #Q2
b=int(input("enter 1 no:"))
c=int(input("enter 2 no:"))
d=int(input("enter 3 no:"))
if(b>c and b>d):
    print("1 is greatest")
elif(c>d):
    print("2 is greatest")
else:
    print("3 is greatest")
    
#Q3
e=int(input("enter the no"))
if(e%7==0):
    print("multiple of 7")
else:
    print("not multiple")