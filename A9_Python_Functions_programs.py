print("JBMNMJ")
'''
🔍 Topics Covered →
✅ What is a Function?
✅ Why Functions are used in Python
✅ Types of Functions (Built-in vs User-defined)
✅ Function Syntax and Structure
✅ Calling Functions with Arguments
✅ Return Statement vs Print
✅ Optional Function Components (Parameters, Return)
✅ Function with Default Parameters (with 4 real scenarios)
✅ Function with Multiple Return Values
✅ Keyword Arguments (with usage examples)
'''

#💡Function in Python->
# A block of statements that perform a specific task
# Functions are used to avoid code repetition and to make the code more organized and reusable.

#💡There is mainly two types of function:-
# 1.Build-in function           {Already provided by Python like print(),range(),len(),type(),etc}
# 2.User-defined function       {A function which is made by a programmer using the 'def' keyword}

#💡Why Use Functions?
# -> To avoid writing the same code again and again (low redundancy)
# -> To divide a big problem into smaller parts (modular code)
# -> To make the code reusable and easy to understand

#💡Syntax of function->
'''
def func_name(parameter1,parameter2,...):   # Function Definition
    #Some work
    return value                            # (optional)

func_name(argument1,argument2,...)          # Function Call
'''

#💡Let's create a simple function to add two numbers:
def calc_sum(a,b): # here this line is called as function definition
    sum=a+b
    #print(sum)
    return sum

#💡let's call this Function many times with different parameter:-
print(calc_sum(13,8)) # Output-> 21
print(calc_sum(11,8)) # Output-> 19
print(calc_sum(13,9)) # Output-> 22

# here (13,8),(11,8),(13,9):- all this are arguments.
#💡Argument values are passed into the function's parameters and used to perform the task inside the function block.

#💡In Python functions, two components are optional:
# 1. Parameters         - Without parameters, the function accepts no input values.
# 2. Return Statement   - Without a return statement, the function performs its task but does not return any specific output.

#💡Let's see what if we cannot return the function:-
def print_hello():
    print("Hello")

output=print_hello()
# Output-> Hello
print(output)          # It return None value because in print_hello() there is no return statement 
# Output-> None

#💡Important Difference:
# -> 'print' shows the result but you can't use it later
# -> 'return' gives you the value to use later in program

#💡function for finding Average of 3 numbers:-
def aver_func(a,b,c):
    average=(a+b+c)/3
    return average 

aver=aver_func(8,9,21)
print("Average of 3 values is:- ", round(aver, 2))
# Output-> Average of 3 values is:-  12.67

#💡Default Parameter->
# Assigning a default value to parameter,which is used when no argument is passed.

#💡Scenario no.1->
def calc_product(a=1,b=1):
    pro=a*b
    return pro

val=calc_product()
print(val)
# Output-> 1

#💡Scenario no.2->
# If I call this function with parameter the default parameter is ignored Let's see->
value=calc_product(21,8)
print(value)
# Output-> 168

#💡Scenario no.3->
# without any argument & without any default parameter if we call a function it throw an error Let's see->
'''def calc_product(a,b):
    pro=a*b
    return pro

v=calc_product()
print(v) # it's throw an Error
# TypeError: calc_product() missing 2 required positional arguments: 'a' and 'b'
'''

#💡Scenario no.4->
# If we want to assign a default value to a parameter, we must start from the last parameter.
# Default arguments should always be placed after non-default ones
def calc_product(a,b=1):
    pro=a*b
    return pro

v=calc_product(8)
print(v)
# Output-> 8
# Since only one argument is passed, 'a' becomes 8 and 'b' takes its default value of 1.

#💡Function With Multiple Returns->

def calculate(a, b):
    sum = a + b
    product = a * b
    return sum, product

s, p = calculate(3, 4)
print("Sum:", s)        # Output -> Sum: 7
print("Product:", p)    # Output -> Product: 12

# Functions can return multiple values using comma separation

#💡Keyword Arguments->
# You can specify arguments by name, not just position

def greet_user(name, msg):
    print("Hello", name + ",", msg)

greet_user(msg="Good Morning!", name="Amit")
# Output -> Hello Amit, Good Morning!

'''✅ Summarization of Default Parameters:
   - Scenario 1: No arguments passed → uses default values
   - Scenario 2: Arguments passed → overrides default
   - Scenario 3: No default, no argument → throws error
   - Scenario 4: Default must start from the right
'''

# for more knowledge go through the Python Documentation

