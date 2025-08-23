print("JBMNMJ")
'''
🔍 Topics Covered →
✅ What are Conditional Statements?
✅ Why Conditions are used in Python
✅ if Statement (with examples)
✅ if-else Statement (with examples)
✅ if-elif-else Ladder (with examples)
✅ Nested if Statement (with examples)
✅ Short-hand if and if-else (Ternary Operator)
✅ Real-life Scenarios of Conditional Statements
✅ match-case Statement (introduced in Python 3.10)
✅ match-case with default case
✅ match-case with multiple patterns
✅ match-case with guards (conditions inside case)
✅ Difference between if-elif-else and match-case
'''

#💡 Conditional Statements in Python->
# These are used to make decisions in programs.
# In real life, decisions are based on conditions (Yes/No, True/False). 
# Similarly, Python uses conditional statements to control the flow of execution.

#💡Types of Conditional Statements in Python->
# 1. if statement
# 2. if-else statement
# 3. if-elif-else statement
# 4. Nested if
# 5. Short-hand if & if-else

#💡1. if Statement->
# Syntax:
'''
if condition:
    # code block
'''

age = 20
if age >= 18:
    print("You are eligible to vote.") 
# Output-> You are eligible to vote.


#💡2. if-else Statement->
age = 15
if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
# Output-> Not eligible for voting


#💡3. if-elif-else Ladder->
marks = 75
if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")
# Output-> Grade: A


#💡4. Nested if->
num = 10
if num >= 0:
    if num == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")
# Output-> Number is Positive


#💡5. Short-hand if and if-else (Ternary Operator)->
x = 5
if x > 0: print("Positive Number")  # short-hand if

# Short-hand if-else
y = -3
print("Positive") if y > 0 else print("Negative")
# Output-> Negative


#💡Real-life Scenario Example: Checking Even or Odd Number:-
n = 11
if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
# Output-> Odd Number

#💡 match-case Statement in Python (Introduced in Python 3.10)->
# It's similar to switch-case in other languages (C, Java, etc.)

#💡Syntax:
'''
match variable:
    case value1:
        # code block
    case value2:
        # code block
    case _:
        # default block
'''

# Example 1: Basic match-case:-
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")
# Output-> Wednesday


# Example 2: match-case with multiple patterns:-
char = "a"
match char:
    case "a" | "e" | "i" | "o" | "u":
        print("It's a vowel")
    case _:
        print("It's a consonant")
# Output-> It's a vowel


# Example 3: match-case with guards (conditions inside case):-
num = 15
match num:
    case n if n % 2 == 0:
        print("Even Number")
    case n if n % 2 != 0:
        print("Odd Number")
    case _:
        print("Not a valid number")
# Output-> Odd Number


# Example 4: match-case for menu driven program:-
choice = 2
match choice:
    case 1:
        print("Start Game")
    case 2:
        print("Load Game")
    case 3:
        print("Exit")
    case _:
        print("Invalid Choice")
# Output-> Load Game

# Example 5: match-case based Calculator:-
a=int(input("Enter 1st Number:- "))
b=int(input("Enter 2nd Number:- "))
operator=str(input("Enter operator Mathematical Symbol:- "))

match operator:
    case "+":
        print("Addition =", a + b)
    case "-":
        print("Subtraction =", a - b)
    case "*":
        print("Multiplication =", a * b)
    case "/":
        print("Division =", a / b if b != 0 else "Division by Zero Error")
    case _:
        print("Invalid Operator")
# Output-> Addition = 15 (It's based on your input)

'''✅ Difference between if-elif-else and match-case
- if-elif-else → used for complex conditions, ranges, and logical operators
- match-case   → better for equality checking and cleaner code for multiple options
'''

# for more knowledge go through the Python Documentation
