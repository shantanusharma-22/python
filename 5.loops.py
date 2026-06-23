#loops 
#used to repeat instruction
#while loops 
#while condition : #some work 
count = 1
while count<=5 :
    print("hello")
    count = count +1

#Q1
i=1
while i <=100:
    print(i)
    i+=1

#Q2
i=100
while i >= 1 :
    print(i)
    i-=1

#Q3
n=int(input("enter no : "))
i=1
while i <= 10:
    print(n*i)
    i+=1

#Q4
nums=(1,4,9,16,25,36,49,64,81,100)
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1

#Q5
nums=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(nums):
    if(nums[i]==x):
        print("found at idx",i)
    else:
        print("finding")
    i+=1

#break used to terminate the loop 
i=1
while i <= 5:
    print(i)
    if (i == 3):
        break
    i+=1
print("end of loop")

#continue terminates execution in the current iteration & continues execution of the loop with the next iteration 
i=1
while i <= 5:
    if (i == 3):
        i+=1
        continue
    print(i)
    i+=1

#for loops are used for squential transversal
#for loops

#for el in list :#some work 
num=[1,2,3,4,56,7,9]
for el in num:
    print(el)

#for loop with else 
#for el in list:#somework
#else:#work when loop ends 
num=[1,2,3,4,56,7,9]
for el in num:
    if (el==56):
     print("found")
     break
    print(el)
else:
    print("end")

#Q1
num=[1,4,9,16,25,36,49,64,81,100]
for el in num:
    print(el)

#range returns a sequence of numbers,starting from 0 by default ,increment by 1 by default and stops before a specified number 

for i in range(10):#range(stop)
    print(i)

for i in range(2,10):#range (start,stop)
    print(i)

for i in range (2,10,2):#range(start,stop,step)
    print(i)

#PASS IS A NULL STATEMENT THAT DOES NOTHING 
for i in range(5):
    pass
#Q1
n = 10
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("total sum=",sum)

#Q2
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial =",fact)