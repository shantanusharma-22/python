#list
marks=[90,80,70,60]#list can store integer,float,string
print(marks[0]) #accessing list element through index
#list slicing
#list name (starting index:ending index) ending index is not included  ,starting from 0 to indexing 
#list method 
list= [2,1,3]
list.append(4)#add one element at the end 
print(list)
list.sort()#sort list in ascending order
print(list)
list.sort(reverse=True)#sort list in decending order 
print(list)
list.reverse()# reverses the list 
print(list)
list.insert(2,4)#insert element at index
print(list)
list.remove(1) #remove the first occurence of element 
print(list)
list.pop(3) #remove element at the index 
print(list) 

#tuples
#tuples are immutable 
tup =(1,2) #tup()
print(tup)
tup = ()#it is a valid tuple 
tup = (1,)#we have to put commom to make it considered as tuple  otherwise it is concidered as integer
#tuple method
tup = (2,1,3,1)
print (tup.index(1))#returns index of first occurence 
print (tup.count(1))#counts total occurence 

#q1
movies = []
mov = input("enter 1st movies")
mov1 = input("enter 2st movies")
mov2 = input("enter 3st movies")
movies.append(mov)
movies.append(mov1)
movies.append(mov2)
print(movies)

#q2
list = [1,2,3,2,1]
copy_list = list.copy()
copy_list.reverse()
if(copy_list == list):
    print("palindrome")
else:
    print("not a palindrome")
    
#Q3
tup = ("c","d","A","A","b","b","A")
print(tup.count("A"))









