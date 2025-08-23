print("JBMNMJ")

'''🔍 Topics Covered->
✅ What is a tuple?
✅ Tuple syntax and creation
✅ Accessing elements by index (positive and negative indexing)
✅ Tuple immutability explained
✅ Looping through tuples
✅ Membership check using in operator
✅ Tuple slicing (positive & negative)
✅ Creating single-element tuples (with and without comma)
✅ Built-in tuple methods: 1.count() 2.index()
✅ Difference between tuples and lists'''

#💡2.Tuples in Python->

# it's a build-in datatype that gives freedom to create immutable sequences of values
# it can store elements of different primitive datatypes(like integer,float,String,boolean)
# tuples are Immutable        tupl=(1,2,8,5)
# In Python, tuples are immutable sequences — that means once you create a tuple, you can't change its content (no adding, removing, or modifying elements). 
# Tuples are created using parentheses ().

#💡Syntax of tuples creation-> name_of_tuple=(elements)---here elements are differentiate by "," 
tup=("Rishabh",19,94.5,True)
print(tup)
#Output-> ('Rishabh', 19, 94.5, True)

print(type(tup))
#Output-> <class 'tuple'>

print(tup[0]) # here you can access the elements by their index because it has same indexing system as string {index starting from (0)}
#Output-> Rishabh

print(len(tup)) # here you get a length of tuple by len()
#Output-> 4

'''tup[0]="Rishi" # here in python it's not allowed to change the element of tuple using their index no. because it's immutable
print(tup)
#Error-> 'tuple' object does not support item assignment'''

# print(tup[5]) here it's throw error
#Output-> IndexError: tuple index out of range

#💡Looping through a tuple
t = ("a", "b", "c")
for item in t:
    print(item)
'''#Output-> a
             b
             c
'''

#💡Check existence
t = ("apple", "banana", "cherry")
print("banana" in t)  
#Output-> True
print("mango" in t)   
#Output-> False 

#💡In Python tuple-Slicing is possible. It's Similar Like a String,list Slicing

print(tup[0:2]) # here also 0 is included & 2 is excluded          ---{Positive Slicing}
#Output-> ('Rishi', 19)

print(tup[-4:-2])                                                 #---{Negative Slicing}
#Output-> ('Rishi', 19)

'''
Showing the indexing system in Python for strings,list,tuple,etc
     [   0        1   2   3 ]---Positive indexing
list=["Rishabh",19,94.5,True]
     [  -4       -3  -2  -1 ]---Negative indexing

'''

# In tuples if you want to make a single element tuple then always use "," at the end for showing that it's is tuple
#💡for ex.->
tup1=(87)
print(type(tup1))
#Output-> <class 'int'> 
# here if you make a tuple of single element without write "," at the end it consider as int value

tup2=(87,)
print(type(tup2))
#Output-> <class 'tuple'> 
# So in this way you can declare a single element tuple in python

#💡tuple Methods->
tup=(2,1,3,1)

#💡1.tup.index(element) # it returns index of first occurrence of the given value
print(tup.index(1)) # here it return the index of 1 at first occurrence in the tuple
#Output-> 1

#💡2.tup.count(element) # it return the count of total occurrence in the tuple
print(tup.count(1))
#Output-> 2


# I know it"s look similar as list and their properties but their is slightly difference because list is mutable & tuple is immutable in python
'''Python tuple ke officially sirf 2 hi built-in methods hote hain:
◾ count(value) – Returns the number of times the value occurs
◾ index(value) – Returns the first index of the given value
Inke alawa aur koi method nahi hota tuple ke liye.'''
# for more knowledge go through the Python Documentation


