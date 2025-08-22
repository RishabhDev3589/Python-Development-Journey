print("JBMNMJ")
'''
🔍 Topics Covered →
✅ What is Recursion in Python?
✅ What is Call Stack & How it Works (LIFO)
✅ Importance of Base Case and Return in Recursion
✅ Dry Run Explanation of Recursive Calls
✅ Forward vs Reverse Order Recursion
✅ Recursion Examples:
    1.Printing numbers in forward and reverse
    2.Calculating factorial
    3.Summing elements of a list
    4.Printing elements of a list
    5.Infinite recursion (error case)
✅ Proper Function Structure and Syntax
✅ Recursive Thinking → Breaking big problems into smaller ones
✅ When and Where to Use Recursion
✅ Real-Life Use Cases of Recursion
'''

#💡UNDERSTANDING CALL STACK IN PYTHON (IN RECURSION)->

#💡What is Call Stack?
# It's a data structure that Python uses to keep track of function calls.
# Whenever a function is called, Python puts that function on the top of the "stack".
# When the function finishes, it is removed (popped) from the stack.
# This works just like stacking and unstacking plates (LIFO - Last In First Out).

#💡Why Call Stack is Important in Recursion?
# In recursion, the same function keeps calling itself again and again.
# Each call waits for the next one to finish.
# All these calls are stored in the call stack.
# Once the base case is hit, stack starts returning back (unwinding happens).

#💡Recursion in Python->
# When a function calls itself directly or indirectly, it's called Recursion.
# Recursion is used to break down a complex problem into smaller sub-problems.
# Every recursive function must have two parts:
# 1. Base Case        -> The condition when recursion stops.
# 2. Recursive Call   -> The function calling itself with a smaller input

#💡Syntax of Recursive Function:
'''
def function_name(parameters):
    if base_case_condition:
        return result
    return function_name(smaller_input)
'''
#💡Let's understand with a simple recursive function ↓

def greet(n):
    if n == 0:                               # Base Case → stops further calls
        print("End of function calls\n")
        return
    print("Calling greet(", n, ")")          # Before recursive call
    greet(n - 1)                             # Recursive call
    print("Returning from greet(", n, ")")   # After recursive call

greet(3)

#💡Output →
# Calling greet( 3 )
# Calling greet( 2 )
# Calling greet( 1 )
# End of function calls
# Returning from greet( 1 )
# Returning from greet( 2 )
# Returning from greet( 3 )

#💡Dry Run with Call Stack ->
'''
Let’s understand what happens step-by-step (like stacking plates):

Step 1: greet(3) is called → put on stack
Step 2: greet(2) is called → put on stack
Step 3: greet(1) is called → put on stack
Step 4: greet(0) is called → base case hit → stop recursion

Now the stack looks like this:

    ┌──────────────┐
    │ greet(3)     │
    │ greet(2)     │
    │ greet(1)     │
    │ greet(0)✅  │  ← base case, now stack starts to shrink
    └──────────────┘

After base case:
- greet(0) ends → removed
- greet(1) continues → "Returning from greet(1)" → removed
- greet(2) continues → "Returning from greet(2)" → removed
- greet(3) continues → "Returning from greet(3)" → removed

→ Stack is now empty, recursion is over
'''

#💡So, In recursion:
# → Calls are pushed into the stack (until base case)
# → Then popped out in reverse order (return phase)

#💡One more example (factorial with stack trace)->

def factorial(n):
    if n == 0 or n == 1:
        print("Reached base case: factorial(", n, ")")
        return 1
    print("Calling factorial(", n, ")")
    result = n * factorial(n - 1)
    print("Returning from factorial(", n, ") with value:", result)
    return result

print("Factorial of 4 is:", factorial(4))

'''
#💡Output->

Call Stack Flow:

Calling factorial(4)
Calling factorial(3)
Calling factorial(2)
Calling factorial(1)
Reached base case: factorial(1)
Returning from factorial(2) with value: 2
Returning from factorial(3) with value: 6
Returning from factorial(4) with value: 24
'''

#💡Dry Run->
# factorial(4) -> 4 * factorial(3)
# factorial(3) -> 3 * factorial(2)
# factorial(2) -> 2 * factorial(1)
# factorial(1) -> returns 1
# Now all results are multiplied and returned back

#💡let's make a recursive function for print numbers from n to 1->
def print_reverse(n):
    if(n==0):                   # It's is base case 
        return         
    print(n)
    print_reverse(n-1)          # (Recursive call) here it call itself for n number of times

print_reverse(5)

'''Output->
5
4
3
2
1
'''

#💡Dry Run:
# print_reverse(5) -> prints 5, calls print_reverse(4)
# print_reverse(4) -> prints 4, calls print_reverse(3)
# ...
# print_reverse(1) -> prints 1, calls print_reverse(0)
# print_reverse(0) -> base case met, function returns and stops

#💡let's make a recursive function for print numbers from 1 to n->
def print_forward(n):
    if n == 0:
        return
    print_forward(n-1)
    print(n)

print_forward(5)

'''Output->
1
2
3
4
5
'''

#💡Dry Run:
# print_forward(5) → calls print_forward(4)
# print_forward(4) → calls print_forward(3)
# print_forward(3) → calls print_forward(2)
# print_forward(2) → calls print_forward(1)
# print_forward(1) → calls print_forward(0)
# print_forward(0) → base case hit → returns

# Now return phase begins ⬇ (print happens here)

# print_forward(1) → prints 1
# print_forward(2) → prints 2
# print_forward(3) → prints 3
# print_forward(4) → prints 4
# print_forward(5) → prints 5 ✅

#💡Note:
# If print comes before the recursive call → reverse order
# If print comes after the recursive call → forward order

# return without value know as control return

#💡Important:- Every recursive function must have a base case,
# otherwise it will call itself forever and cause an error:
# RecursionError: maximum recursion depth exceeded

#💡❌ Wrong Example: Infinite recursion (no base case)
'''
def infinite_recursion():
    print("Calling...")
    infinite_recursion()

infinite_recursion()
# Output -> RecursionError
'''

#💡let's make a recursive function to print a whole list->
def print_list(list1,idx=0):
    if(idx==len(list1)):
        return
    print(list1[idx])
    print_list(list1,idx+1)

list1=[1,2,3,4,5,6,7,8,9]
print_list(list1)

# Output-> 1 2 3 4 5 6 7 8 9  (all no. are in different line)

#💡let's make a recursive function to print a Sum of List Elements->
def sum_list(arr, idx=0):
    if idx == len(arr):
        return 0
    return arr[idx] + sum_list(arr, idx + 1)

print("Sum of List:", sum_list([1, 2, 3, 4])) 

# Output: 10


'''💡Where is Recursion Used?
- Factorials
- Fibonacci series
- Tree/Graph traversal
- Searching/Sorting algorithms (Quick Sort, Merge Sort)
- Backtracking (like Sudoku, N-Queens)
'''

'''🧠 Call Stack Summary->
Stack-based memory structure used to store function calls
Follows LIFO (Last In First Out)
Recursion builds up the stack until the base case
Then unwinds the stack back (return phase)
'''

# for more knowledge go through the Python Documentation

