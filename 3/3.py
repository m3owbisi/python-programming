# lists in python
mark0=12.3
mark1=94.4
mark2=87.5
mark3=95.2
mark4=66.4
mark5=45.1
marks=[12.3,94.4,87.5,95.2,66.4,45.1]
print(marks)
print(type(marks))
# marks=[87,64,33,95,76]    # marks[0],marks[1]
# student=["karan",85,"delhi"]  #student[0],student[1]
# student[0]=["arjun"] # allowed in python
# len(student)    # returns length
print(marks[0])
print(marks[1])
print(len(marks))
student=["karan",95.4,17,"delhi"]
print(student)

# difference between strings and lists in python
# str="hello"
# print(str[0])
# str[0]='y'
# print(str)
student[0]="arjun"
print(student)
# print(student[5])

# list slicing
# list_name[starting_idx:ending_idx]  # ending idx is not included
# marks=[87,64,33,95,76]
# marks[1:4] is [64,33,95]
# marks[:4] is same as marks[0:4]
# marks[1:] is same as marks[1:len(marks)]
# marks[-3:-1] is [33,95]
marks=[85,94,76,63,48]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

# list methods
# list=[2,1,3]
# list.append(4)  # adds one element at the end   [2,1,3,4]
# list.sort() # sorts in ascending order  [1,2,3]
# list.sort(reverse=True) # sorts in descending order [3,2,1]
# list.reverse()  # reverses list [3,1,2]
# list.insert(idx,el) # insert element at index
list=[2,1,3]
list.append(4)
print(list)
# print(list.sort())
# list=list.sort()
# list.sort
print(list.sort())
print(list)
print(list.sort(reverse=True))
print(list)
list=["banana","litchi","apple"]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list=['a','d','e','f','c','b']
list.reverse()
print(list)
list.insert(6,'g')
print(list)
list=[2,1,3]
list.insert(1,5)
print(list)
# list=[2,1,3,1]
# list.remove(1)  # removes first occurrence of element   [2,3,1]
# list.pop(idx)   # removes element at idx
list=[2,1,3,1]
list.remove(1)
print(list)
list.pop(2)
print(list)

# tuples in python
# tup=(87,64,33,95,76)    # tup[0],tup[1]
# tup[0]=43   # not allowed in python
# tup1=()
# tup2=(1,)
# tup3=(1,2,3)

# difference between tuples and lists in python
tup=(2,1,3,1)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1])
# tup[0]=5
tup=()
print(tup)
print(type(tup))
tup=(1,)
print(tup)
print(type(tup))
tup=(1)
print(tup)
print(type(tup))
tup=(1.0)
print(tup)
print(type(tup))
tup=("hi")
print(tup)
print(type(tup))
tup=(1,2,3,4)
print(tup)
print(type(tup))

# tuple slicing
tup=(1,2,3,4)
print(tup[1:3])

# tuple method
# tup=(2,1,3,1)
# tup.index(el)   # returns index of first occurrence tup.index(1) is 1
# tup.count(el)   # counts total occurrences  tup.count(1) is 2
tup=(2,1,3,1)
print(tup.index(1))
print(tup.count(1))

# lets practice
"""
WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
"""
movie_list=[]
movie1=input("enter first movie: ")
movie2=input("enter second movie: ")
movie3=input("enter third movie: ")
movie_list.append(movie1)
movie_list.append(movie2)
movie_list.append(movie3)
# movie=input()
# movie_list.append(movie)
# movie_list.append(input())
print(movie_list)   # shutter island lucy primer
"""
WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
[1,2,3,2,1] [1,"abc","abc",1]
"""
# list=[1,2,3]
# list.copy()
# list.reverse()
list1=[1,2,3,2,1]
list2=[1,2,3,4]
list3=[1,"abc","abc",1]
list4=['m','a','a','m']
copy_list=list2.copy()
copy_list.reverse()
if(copy_list==list2):
    print("is palindrome")
else:
    print("is not palindrome")
"""
WAP to count the number of students with the "A" grade in the following tuple.
["C","D","A","A","B","B","A"]
"""
grade=("C","D","A","A","B","B","A")
print(grade.count("A"))
"""
Store the above values in a list & sort them from "A" to "D".
"""
grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)