#dictionary 
#dictionary are used to store data values in key:value pair and their unordered ,mutable(changeable)&don't allow duplicate keys 
dict = {
    "name" : "shantanu",
    "cgpa" : 9.6,
    "marks" : [98,54,87]
}
#dict["key"] = "value" to assign or add new
print(dict ["name"])

#nested dictionary
dict = {
    "name" : "shantanu",
    "cgpa" : 9.6,
    "marks" : {
        "phy":98,
        "chem" : 87,
        "maths" :99
    }
}
print(dict["marks"]["maths"])
dict = {
    "name" : "shantanu",
    "cgpa" : 9.6,
    "marks" : [98,54,87]
}
print(dict.keys())#returns all keys 
print(dict.values())#returns all values 
print(dict.items())#returns all (key,val) pairs as tuples
print(dict.get("name"))#returns the key according to value 
newdict = {"city" : "delhi","age":16}
dict.update(newdict)
print(dict)#inserts the specific items to the dictionary 

#set
#it is the collection of all unordered items and unique and immutable
nums = {1,2,2,3,3,5}#repeated elements stored only once so it resolve to {1,2,3,5}
print(nums)
null_set = set() #empty set syntax
nums2 = {2,3,6,5,4,8,9,2,5,2,}
nums2.add(1)
nums2.add("shantanu")
nums2.add((1,2,3))
print(nums2)
nums2.remove(2)#removes the element 
print(nums2)
nums2.clear()#empties the set 
print(nums2)
nums3 = {2,3,6,5,4,8,9,2,4,9,7,3,4,5,2,}
nums3.pop()#removes a random value 
print(nums3)
print(nums2.union(nums3))#combines both set values and return new
print(nums2.intersection(nums3))#combines both set values and return new 

#Q1
dict ={
    "table":["a piece of furniture","list of figures & facts "],
    "cat" : "a small animal"
}
print(dict)

#Q2
marks = {}
x=int(input("enter phy : "))
marks.update({"phy":x})
y=int(input("enter chem : "))
marks.update({"chem":y})
z=int(input("enter py : "))
marks.update({"py":z})
print(marks)

#Q3
me ={9,"9.0"}
print(me)