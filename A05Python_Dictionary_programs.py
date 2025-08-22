print("JBMNMJ")

'''🔍 Topics Covered →
✅ What is a Dictionary?
✅ Dictionary Syntax and Creation
✅ Dictionary Value Types (All data types allowed in values)
✅ Dictionary Keys (Why strings/tuples are preferred; why lists aren't allowed)
✅ Accessing Values using Keys
✅ Mutability of Dictionaries (Change/Update/Add values)
✅ Null (Empty) Dictionary
✅ Nested Dictionary (Accessing nested values)
✅ Dictionary Methods
'''

#💡3.Dictionary in Python-> 
# Dictionary are used to store data values in keys:values pairs
# they are unordered,mutable & don't allow duplicate keys
# In dictionary they are accept all types of data
# dictionary key andar ham list aur tuples bhi store kar saktey hai {in value section}
# Dictionary are Mutable in nature      dict={"keys":values,...}

#💡Syntax of dictionary creation-> name_of_dictionary={keys:values,..}---here pairs of keys:values are differentiate by "," 
dict={
    "name" : "Rishabh",                  #datatype of values= String,character
    "cgpa" : 9.64,                       #datatype of values= float 
    "age"  : 20,                         #datatype of values= integer
    "marks" : [96.5,98,76,80],           #datatype of values= list
    "S_Dt" : ("Rishabh",19,94.5,True),   #datatype of values= tuples
}
print(dict)
#Output-> {'name': 'Rishabh', 'cgpa': 9.64, 'age': 20, 'marks': [96.5, 98, 76, 80], 'S_Dt': ('Rishabh', 19, 94.5, True)}

# So here we clearly see that In values section it allowed all data type
# We mostly use strings as dictionary keys.
# Actually, immutable data types (like strings and tuples) are considered better for dictionary keys.
# So that's reason we doesn't use list as keys in dictionary

#💡In dictionary we use keys to access the values from dictionary
# for ex.:-
print(dict["name"],dict["cgpa"],dict["age"],dict["marks"],dict["S_Dt"])
#Output-> Rishabh 9.64 20 [96.5, 98, 76, 80] ('Rishabh', 19, 94.5, True)

#💡print(dict["std"]) # here it's throw error because std keys are not found in dict
#Output-> KeyError: 'std'

#💡If you want, you can change the value of specific keys
# for ex.:-
dict["name"]="Rishi"
print(dict)
#Output-> {'name': 'Rishi', 'cgpa': 9.64, 'age': 20, 'marks': [96.5, 98, 76, 80], 'S_Dt': ('Rishabh', 19, 94.5, True)}

#💡If you want to add a new keys in dictionary then->
dict["Aim"]="Developer" # here aim key is add on the last of the dictionary
print(dict)
#Output-> {'name': 'Rishi', 'cgpa': 9.64, 'age': 20, 'marks': [96.5, 98, 76, 80], 'S_Dt': ('Rishabh', 19, 94.5, True), 'Aim': 'Developer'}

#💡If you want to create a null dictionary then-> 
null_dict={}
print(null_dict)
#Output-> {}

#💡Nested Dictionary-> 
# In Python nested dictionary is allowed
Student={
    "Name" : "Rishabh",
    "Course" : "B.tech",
    "Score" : {
        "DS" : 75,
        "DBMS" : 80,
        "MPCA" : 95
    }
}
# If we want to access the nested dictionary value then->
# for ex. aap score keys key andar ki DBMS ka marks pataa karna chahtey ho 
# then write dict["name_of_keys"]["name_of_nested keys"]
print(Student["Score"]["DBMS"])
#Output-> 80

# Dictionaries do not allow duplicate keys.
# If you try to create a dictionary with duplicate keys, the latest value will override the previous one.

#💡Dictionary Methods-> 

dict1={
    "name" : "Rishabh",                  
    "skills" : "Python",
    "age"  : 20,  
}
print(dict1)
#Output-> {'name': 'Rishabh', 'skills': 'Python', 'age': 20}

#💡1.dict.keys()             # here it returns all keys of dictionary
print(dict1.keys())
#Output-> dict_keys(['name', 'skills', 'age'])

# If you want then you make a list of this output:-
print(list(dict1.keys()))
#Output-> ['name', 'skills', 'age']

#If you want then you also store permanently this list in list1
list1=list(dict1.keys())
print(list1)
#Output-> ['name', 'skills', 'age']
print(type(list1))
#Output-> <class 'list'>
print(list1[0])
#Output-> name

#💡2.dict.values()->         # here it returns all values of dictionary
print(dict1.values())
#Output-> dict_values(['Rishabh', 'Python', 20]) # here also if we want, then we make a list of this output 

#💡3.len(dict1)->            # To get length of dictionary
print(len(dict1))
#Output-> 3

#💡4.dict.items()->         # here it returns all keys:values pairs as tuples
print(dict1.items())
#Output-> dict_items([('name', 'Rishabh'), ('skills', 'Python'), ('age', 20)])

pairs=list(dict1.items())
print(pairs[0])
#Output-> ('name', 'Rishabh') # here we got a tuple of keys & values

#💡5.dict.get("keys") # returns the specific key values
print(dict1.get("name"))
#Output-> Rishabh

print(dict1.get("contact"))
#Output-> None

# It's similar as dict["keys"] but their is 1 main difference 
# If I write dict["keys"] & if key was not found at that dictionary it throw an error which disturb whole code

# But if I write dict.get("keys") & if key was not found at that dictionary it doesn't throw an error
# It return None value without disturbing the upcoming code

#💡6.dict.update(new dict / pairs of keys:values)-> # it insert the specific items or new dictionary to the old dictionary
# There is 2 way to insert the keys ,values

# way 1->
new_dict={"Contact" : 998542454}
dict1.update(new_dict)
print(dict1)
#Output-> {'name': 'Rishabh', 'skills': 'Python', 'age': 20, 'Contact': 998542454}

# way 2->
dict1.update({"Hobby": "Singing"})
print(dict1)
#Output-> {'name': 'Rishabh', 'skills': 'Python', 'age': 20, 'Contact': 998542454, 'Hobby': 'Singing'}

'''Summarize the Dictionary Method-
✅ Dictionary Methods:
1. .keys() → returns all keys
2. .values() → returns all values
3. len() → returns number of key-value pairs
4. .items() → returns all key-value pairs as tuples
5. .get() → safely gets value by key (returns None if key doesn't exist)
6. .update() → adds or updates key-value pairs in dictionary
'''

# for more knowledge go through the Python Documentation
