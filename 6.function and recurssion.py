#function block of statements that performs a specific task 
# def i(a,b,c,d,e,f):#function call
#     #some work 
#     return i
def sum(a,b):
    s=a+b
    return s
print(sum(2,3))

#built in function 
# print()
# len()
# type()
# range()

#Q1
list=(1,2,3,4,5,6,7,8,9)
def list_len(list):
    print(len(list))
list_len(list)

#Q2
list=(1,2,3,4,5,6,7,8,9)
def list_len(list):
    print(len(list))
    for i in list:
        print(i,end="")
list_len(list)

#Q3
def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(fact)
cal_fact(5)

#Q4
def converter(usdval):
    inrval=usdval*83
    print(usdval,"usd=",inrval,"inr")
converter(44)

#Q5
def num(n):
    if(n%2==0):
        print("no is even ")
    else:
        print("no is odd")
num(9)

#recurrsion when a function calls itself repeeatedly 
#print n to 1 backword 
def show (n):
    if(n==0):
        return
    print(n)
    show (n-1)
show (10)

#returns n!
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(4))

#Q1
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n
sum = calc_sum(10)
print(sum)

#Q2
lists = ("An,annla","vsakdkad","eknasdknak")
def i(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    i(list,idx+1)
i(lists)