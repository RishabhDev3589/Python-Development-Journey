print("JBMNMJ")

# In Python:- 
# 1.Lists are Mutable           list=["rishabh",32,94.5,True,...]
# 2.Dictionary are Mutable      dict={"keys":values,...}
# 3.Strings are Immutable       str1=("Rishabh","32","94.5",..)
# 4.tuples are Immutable        tupl=(1.2.8,5)

# 1.Lists in Python->
# it's is a build-in datatype that stores set of values
#it can store elements of different primitive datatypes(like integer,float,String,boolean)

#Syntax of lists creation-> name_of_list=[elements]---here elements are differentiate by "," 
list=["Rishabh",19,94.5,True]
print(list)
#Output-> ['Rishabh', 19, 94.5, True]

print(type(list))
#Output-> <class 'list'>

print(list[0]) # here you can access the elements by their index because it has same indexing system as string {index starting from (0)}
#Output-> Rishabh

print(len(list)) # here you get a length of list by len()
#Output-> 4

list[0]="Rishi" # here in python it's allowed to change the element of list using their index no. because it's mutable
print(list)
#Output-> ['Rishi', 19, 94.5, True]

# print(list[5]) here it's throw error
#Output-> IndexError: list index out of range

# In Python List-Slicing is possible. It's Similar Like a String Slicing

print(list[0:2]) # here also 0 is included & 2 is excluded          ---{Positive Slicing}
#Output-> ['Rishi', 19]

print(list[-4:-2])                                                 #---{Negative Slicing}
#Output-> ['Rishi', 19]

'''
Showing the indexing system in Python for strings,list,etc
     [   0        1   2   3 ]---Positive indexing
list=["Rishabh",19,94.5,True]
     [  -4       -3  -2  -1 ]---Negative indexing

'''

#list Methods->
lists=[2,1,3]

# 1.list.append()-> it add one element at the end of the list
lists.append(4)
print(lists)
#Output-> [2, 1, 3, 4]

# 2.list.sort()-> it sorts the data in ascending order in the original list
print(lists.sort()) # this method returns none value because it make changes in original list
#Output-> None
print(lists)
#Output-> [1, 2, 3, 4]

# IMP.:-strings mey methods print karney par updated value return hota hai par list mey methods hamey none value return kartey hai kyuki ye hamarey original list mey direct changes kartey hai

# 3.list.sort(reverse=True) # it sort the data in descending order in the original list * ye int key sath strings ya character ko bhi reverse kar skhta hai
lists.sort(reverse=True)
print(lists)
#Output-> [4, 3, 2, 1]

# 4.list.reverse() # it reverse the list
lists.reverse()
print(lists)
#Output-> [1, 2, 3, 4]

# 5.list.insert(index,element) # here it insert element at that specific index
lists.insert(3,8)
print(lists)
#Output-> [1, 2, 3, 8, 4]
# here it insert the value on that index which you give in command without disturbing the upcoming list elements

# 6.list.remove(value) #removes first occurrence of element
lists.remove(8)
print(lists)
#Output-> [1, 2, 3, 4]

# 7.list.pop(index) # removes element at that specific index
lists.pop(2) # ye directly uss index par jaakey value ko delete karta hai
print(lists) 
#Output-> [1, 2, 4] 

# I know there is a multiple methods in python for list but i explain only imp. method which is use generally and mostly  
# for more knowledge go the Python Documentation
