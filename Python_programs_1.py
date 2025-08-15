# Summary of Sequence:-
'''1.Basic print statements
   2.Primary data types (Integer, String, Float, Boolean, None)
   3.Type detection using type()
   4.Comments in Python
   5.Types of operators (Arithmetic, Relational, Assignment, Logical)
   6.Type Conversion and Type Casting
   7.User Input handling
'''
print("JBMNMJ")
print('HELLO WORLD')

#There are 5 Primary Datatype in Python :

# 1.Integer (+ve,-ve,0) {Whole Values}
age1=18
age2=-18
age3=0

# 2.String {Sentence,Mix-up of words/values} (' '," ",''' ''')<-3 Way to put the value on string
name1='Rishabh'
name2="Rishabh"
name3='''Rishabh'''
print(name1,name2,name3)

# 3.Float(Decimal Values)
price=29.88

# 4.Boolean (True,False) *(T,F are in capital letter)
moonsoon=True
summer=False

# 5.None (Jis mey hamey koi bhi value abhi put nahi karna hai ussmey ham none put kar deytey hai ) *(N are in capital letter)
a=None

#datatype detection by Python:-
print(type(age1))
print(type(name1))
print(type(price))
print(type(moonsoon))
print(type(a))

#Python is case-sensitive language (A,a both are different)

#Comments on Python->
# 1.Single-Line comment
''' 2.Multi-Line comment'''

#Types of Operators in Python->

# a+b-> (Here a,b is a Operand & + is a Operator )

# 1.Arithmetic Operators (+,-,*,/,**,%)
A=5
B=8
print(A+B , A-B , A*B , A/B , A%B , A**B)

# IMP-> **(a to the power b)
# % (it gives Reminder)
# In Python if we divide 2 value we always get a value in floating

# 2.Relational/Comparison Operators(==,!=,>,<,<=,>=)
a=20
b=30
print(a==b , a!=b , a<b , a>b , a<=b , a>=b)
#Output->(False True True False True False)

# IMP-> Relational Operator Always return Boolean Value

# 3.Assignment Operator(=,+=,-=,*=,/=,%=,**=)
num=10 # yaha par ham num ko 10 assign kar rahey hai
print("Assign = num:",num)

num+=10 # num mey 10 add kar do
print("Addition = num:",num)

num-=10 # num mey 10 subtract kar do
print("Subtract = num:",num)

num*=10 # num ko 10 sey multiply kar do
print("Multiply = num:",num)

num/=10 # num  ko 10 sey divide kar do  
print("Divide = num:",num)

num**=10 # num to the power 10 kar keuy do
print("Power = num:",num) 

num%=10 # num ko jab 10 divide kareygey tab remainder kya hoga wo deyga
print("Modulo = num:",num)

# 4.Logical Operator(not,and,or)

#not operator (it's work on single operand) {it reverse the value}
x=True
print(not x)
y=False
print(not y)

#and operator (it's work on double operand) {It return true value only when both the value is true}
val1=True
val2=True
print("AND operator: ",val1 and val2)

#or operator {dono mey sey yadi koi ek bhi value True hai toh True nahi toh False}
val1=True
val2=False
print("OR operator: ",val1 or val2)

# Type Conversion And Type Casting ->

# *IMP-> type conversion is automatically done by python interpeter on the basis of Supremum precedency of datatype
# for example :-
a=12
b=18.98
print(a+b) # here the a is converted into float value and then give the output of sum.

u='12'
v=18.98
# print(u+v) (here error throw because we add str and float which is wrong instruction)
# So we try to convert the datatype of u into int so the output gives right value
# Here we Indroduce the topic of Type Casting Where we forcefully convert the datatype

u=int(u)
print(type(u))
print(u+v) # here it gives perfect output

# Input In Python
# Input using input Statement-> input()

o=int(input("Enter your value: "))
print(type(o))
# we always declare the datatype of upcoming user input value 
# It's not important to declare the datatype 
# if we not declare it python store the upcoming value in string form  
 
# for example:-
p=input("Enter the value: ")
print(type(p))






