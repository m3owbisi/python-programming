# dictionary in python
# "key":value
dict={
    "name":"shradha",
    "cgpa":9.6,
    "marks":[98,97,95],
}
# dict["name"],dict["cgpa"],dict["marks"]
# dict["key"]="value" # to assign or add new
info={
    "key":"value",
    "name":"apna college",
    "learning":"coding",
    "age":35,
    "is_adult":True,
    "marks":94.4,
    "subs":["c","cpp","csharp","python"],
    "topics":["dictionaries","sets"],
    12.99:95.99,
    5:7
}
print(info)
print(type(info))
print(info["name"])
print(info["learning"])
print(info["subs"])
print(info["topics"])
# print(info["last-name"])
info["name"]="hiral panchal"    # overwrite
info["first-name"]="hiral"  
info["last-name"]="panchal"
print(info)
null_dict={}
print(null_dict)
null_dict={
    "channel":"apna college",
}
print(null_dict)

# nested dictionaries
student={
    "name":"shradha",
    "score":{
        "chem":98,
        "phy":97,
        "math":95,
    },
    "subject":["chem","phy","math"],
}
# student["score"]["math"]
print(student)
print(student["subject"])
print(student["score"]["chem"])

# dictionary methods
# myDict.keys()   # returns all keys
# myDict.values() # returns all values
# myDict.items()  # returns all (key,val) pairs as tuples
# myDict.get("key")   # returns the key according to value
# myDict.update(newDict)  # inserts the specified items to the dictionary
print(info.keys())
print(list(info.keys()))
print(len(info.keys()))
print(len(list(info.keys())))
print(info.values())
print(list(info.values()))
print(len(list(info.values())))
print(info.items())
print(list(info.items()))
print(len(list(info.items())))
pairs=list(student.items())
print(pairs[0])
# d["key"]  ->  value
# d.get("key")  ->  value
print("before")
print(student["name"])  # error
print(student.get("name"))  # no error -> none
print("after")
print("hi")
print("welcome to")
print("apna college")
print("we are learning coding for")
print("python")
student.update({"city":"delhi"})
print(student)
new_dict={"name":"hiral","city":"mumbai"}
student.update(new_dict)
print(student)
new_dict.update({"state":"maharashtra"})
print(new_dict)

# set in python
# nums={1,2,3,4}
# set2={1,2,2,2}
# repeated elements stored only once, so it resolved to {1,2}
# null_set=set()  # empty set syntax
collection={1,2,3,4,5,6,7,"seven"}
print(collection)
print(type(collection))
collection={1,2,2,2}
print(collection)
print(type(collection))
print(len(collection))  # total number of items
collection={}   # empty dictionary
print(type(collection))
collection=set()   # empty set
print(type(collection))

# set methods
# set.add(el) # adds an element
# set.remove(el)  # removes the elem an
# set.clear() # empties the set
# set.pop()   # removes a random value
collection=set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(2)
print(collection)
collection.remove(1)
print(collection)
# collection.remove(7)
# print(collection)
collection.add("apna college")
collection.add((1,2,3,4))
# collection.add([1,2,3,4])
print(collection)
print(collection.pop())
print(len(collection))
collection.clear()
print(len(collection))

# set methods
# set.union(set2) # combines both set values & returns new
# set.intersection(set2)  # combines common values & returns new
set1={1,2,3,4}
set2={3,5,6,7}
print(set1)
print(set2)
print("union of a set:")
print(set1.union(set2)) # {1,2,3,4,5,6,7}
print("intersection of a set:")
print(set1.intersection(set2))  # {3}

# lets practice
"""
Store following word meanings in a python dictionary:
table:"a piece of furniture","list of facts & figures"
cat:"a small animal"
"""
dictionary={
    "table":["a piece of furniture","list of facts & figures"],
    "cat":"a small animal",
}
print(dictionary)
"""
You are given a list of subjects for students.
Assume one classroom is required for 1 subject.
How many classrooms are needed by all students.
"python","java","cpp","python","javascript","java","python","java","cpp","c"
"""
subjects={"python","java","cpp","python","javascript","java","python","java","cpp","c"}
print(subjects)
print(len(subjects))
"""
WAP to enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary & add one by one.
Use subject name as key & marks as value.
"""
marks={}
x=int(input("enter phy: "))
marks.update({"phy":x})
x=int(input("enter chem: "))
marks.update({"chem":x})
x=int(input("enter math: "))
marks.update({"math":x})
print(marks)
"""
Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)
"""
values={9,9.0,9.75,8,8.0,"9.0",}
print(values)
values={
    ("int",9),
    ("float",9.0),
}
print(values)