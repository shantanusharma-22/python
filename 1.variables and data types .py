print('hello world') #to print the the input 
a='shraddha' #here "a" is variable contain string shraddha 
print(type(35)) #type function is used to find which kind of data type is this :in this case data type is integer shown as 'int' type,+ve,-ve,0
print(type('shantanu sharma')) #in this case data type is string shown as 'str'
print (type (33.53)) #this case data type is float shown as 'float'
print(type (True )) #this case data type is boolean shown as 'bool'   in this type first letter is capital ,type True,False
print(type (None) )#this case data type is none shown as 'None' type ,None

#for comment we use '#'
a=10
b=2

#arithmatic operator
print(a+b) #10+2
print(a-b) #10-2
print(a/b) #10/2
print(a*b)  #10*2
print(a%b)   #a/b ka remainder hota ha 
print(a**b)  #a ki poweer b hota ha

#relational operator
print (a==b)#equal to 
print (a!=b) #not equal to 
print (a>b) #greater than
print (a<b) #less than 
print (a>=b)#greater than equal to 
print(a<=b) #less than equal to 

#assignment operator
c=30 #assign the variable the value 
c+=b #here we use assignment operator in this case we c+b= ko likhne ka short way ha 
print (c) 
c-=b
print(c)#here we use assignment operator in this case we c-b= ko likhne ka short way ha
c*=b
print (c) #c*b=
c/=b
print(c) #c/b=
c%=b
print(c) #c%b=
c**=b
print(c) #c**b=

#logical operator
q=True
print(not q)#output ka revers print hota ha 
print (5<6 and 5==6 )#and operator me true tab hota ha jab (both values are true)
print (5<6 or 5==6)#or operator me true tab hota ha jab (singlr one or both are true)

#type conversion
#automatically
d=2
e=4.25
print(d+e) #automatically change the data type to  int to float

#type casting 
#manually conversion 
x,y=1,"2"
z=int(y) # here we turn the data type y which is string to an integer manually 
print (x+z)
input ("st") #this function is to accept values give by user and the result will always be string
int(input("first no")) #int input means the result will always be be integer
float(input ("secound no ")) #float input means the result will always be float no

#Q1
first=int(input("enter first no "))
secound=int (input("enter secound no"))
print ("sum",first+secound)

#Q2
side=int(input("enter side of the square"))
print ("area of the square",side**2)

#Q3
f=float(input("1 number"))
k=float (input("2 number"))
print ("average of the two number",(f+k)/2)

#Q4
q=int(input ("a"))
w=int(input ("b"))
print (q>=w)