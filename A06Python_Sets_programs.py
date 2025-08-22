print("JBMNMJ")
'''
📘 Topics Covered →
✅ What is a Set in Python?
✅ Set Syntax and Creation
✅ Data Type Compatibility (Mutable vs Immutable in Sets)
✅ Duplicate Handling in Sets
✅ Unordered Nature of Sets (No Indexing)
✅ Empty Set Creation (set() vs {})
✅ Set Mutability (Modifiable Container, Immutable Elements)
✅ Set Methods
✅ Practical Use Cases with Comments and Examples
'''

#💡4.Sets in Python->
# Set is the collection of the unordered items.
# Each element in the Set must be Unique & Immutable 
# In Set we can Store Multiple datatype Value.{like:-Int,Float,String,Boolean,Tuples}
# But As we know each element of Set must be Immutable So that's Reason In Set we can't store List or Dictionary.
# Sets doesn't have indexing system.
# IMPORTANT-> Set is Mutable{We can add or remove element from the set} But Element of Set is Immutable.

#💡Syntax of set creation-> name_of_set={values,...}---here values are differentiate by "," 
collection={1,2,3,8,9}
print(type(collection))
#Output-> <class 'set'>
print(collection)
#Output-> {1, 2, 3, 8, 9}

#💡Suppose we have a set with Duplicate Value Let's See->
coll={1,3,9,3,9,3,2,6}
print(coll)
#Output-> {1, 2, 3, 6, 9} 
print(len(coll)) # here len() is used to find the length of set
#Output-> 5
# here you can see Python Ignore the duplicates values of set without throwing an error

coll1={1,2,2,2,"Hello","World","World"} 
print(coll1)
#Output-> {'World', 2, 'Hello', 1}
coll1={1,2,2,2,"Hello","World","World",4} 
print(coll1)
#Output-> {1, 2, 'World', 4, 'Hello'}

#💡Here you can see when you try to print the set multiple times it change the order of sequence Because the set is unordered in nature.

#💡How to Create a Empty Set? Let's See->
# If I write-
num={}
print(type(num))
#Output-> <class 'dict'>
# So to make a empty set we have a different syntax:-
nums=set()
print(type(nums))
#Output-> <class 'set'>

#💡Set Methods->

sets=set()

#💡1.set.add(element)->      # add an element on the set.
sets.add(5)                 # Integer
sets.add(5.9)               # Float
sets.add("Hello")           # String
sets.add(True)              # Boolean 
sets.add((1,2,3))           # Tuple
print(sets)
#Output-> {True, 5.9, 5, (1, 2, 3), 'Hello'}
# Here you can see, it proves that Set can store value of multiple datatype like:-int,float,string,boolean,list.

'''But if I try to add list or dictionary then it throw an error let's see:-
sets.add([1,2,3])
#Output-> TypeError: unhashable type: 'list'
sets.add({1,2,3})
#Output-> TypeError: unhashable type: 'dict'
'''

#💡2.set.remove(element)->   # remove an element on the set.

'''
sets.remove(5,5.9,"Hello",True) 
print(sets)
# it throw an error
# TypeError: set.remove() takes exactly one argument (4 given)
'''
# You can only take one arugument at one time for.remove(),.add()

sets.remove((1,2,3))
print(sets)
#Output-> {True, 'Hello', 5.9, 5}

#💡3.set.clear()             # Empties the set
sets.clear()
print(len(sets))
#Output-> 0

#💡4.set.pop()               # removes a random value from the set
st={1,2,5,8,9}
print(st.pop())
#Output-> 1
print(st)
#Output-> {2, 5, 8, 9}

# For upcoming 2 methods we suppose 2 set->
set1={1,3,5,9,7}
set2={2,3,8,10,9}
print(type(set1),type(set2))
#Output-> <class 'set'> <class 'set'>

#💡5.set.union(set2)         # combines both the set values & returns new
print(set1.union(set2))
#Output-> {1, 2, 3, 5, 7, 8, 9, 10}

#💡6.set.intersection(set2)  # combines common values & returns new
print(set1.intersection(set2))
#Output-> {9, 3}

# In both of them set1 & set2 doesn't change.
'''
🧠 Summarization of Set Methods->

✅ Set Methods: 
1 .add(element) → Adds a single immutable element (int, float, string, tuple, etc.) to the set
⛔ Cannot add mutable types like list or dictionary (raises TypeError)

2 .remove(element) → Removes a specified element from the set
⛔ Accepts only one argument at a time; throws error if element not found

3 .clear() → Empties the entire set
4 .pop() → Removes and returns a random element from the set
5 .union(other_set) → Returns a new set containing all elements from both sets (removes duplicates)
6 .intersection(other_set) → Returns a new set with only elements common to both sets
'''

# for more knowledge go through the Python Documentation
