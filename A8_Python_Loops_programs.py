print("JBMNMJ")
'''
🔍 Topics Covered →
✅ What are Loops?
✅ while Loop Syntax & Execution (Increment & Decrement)
✅ for Loop Syntax and its use in sequences (list, string, etc.)
✅ Infinite Loop Handling
✅ Looping through Lists using while and for
✅ Loop with else Block (Execution Condition Explained)
✅ Loop Control Statements:[break,continue,pass] 
✅ range() Function:-
    1.range(stop)
    2.range(start, stop)
    3.range(start, stop, step)
    Use of positive & negative steps
✅ Linear Search using for loop
✅ Infinite loop warning and good practices
✅ Python Comments & Explanation for better understanding
'''

#💡Loops in Python->
# A loop is a programming construct that allows you to repeat a block of code multiple times,as long as a condition is true or for a specific number of times.
# loops are used to repeat instructions
# There is mainly two types of loops in Python->
# 1.while loop
# 2.for loop

#💡1.while Loop->

#💡Syntax of while loop->  (In hindi while means jab tak)
'''count = 1              (here count is iterator)
while(condition):
    some work
    count+= 1           {for increment}
'''
#💡Increment order mey loop chalna:-

i = 1                   #initialization
while (i<=5):
    print(i)
    i+= 1               # increment
print("Loop Ended")

#💡Decrement order mey loop chalna:-

i = 5                   #initialization
while (i>=1):
    print(i)
    i-=1                # decrement
print("Loop Ended")

''' Both Loop Gives Same Output->
1
2
3
4
5
Loop Ended '''

#⚠️Important:- Make sure the condition eventually becomes False, or it’ll create an infinite loop.

'''💡Infinite Loop-> it's dangerous for our code.
i=5
while (i<6):
    print(i)
    i-=1
print("Loop Ended") '''

#💡Using while loop we go through the list:-
i=0
list=[1,2,3,4,5,6,7,8,9]
while (i<len(list)):
    print(list[i])
    i+= 1
# Output-> 1....9 print hoga

#💡2.for loop-> 
# Used to iterate over a sequence (like a list, tuple, dictionary, string, or range).
# it's for sequential traversal for traversing list,string,tuples,etc.

#💡Syntax of for loop->
'''
for variable in sequence:
    # code block
'''

list=[1,3,5,7,9]
for element in list:
    print(element)
# Output-> it prints 1....9 from the list

#💡If I want to find the specific value on list we use loop->           {💡It's also known as Linear Search}
list1=[2,4,6,8,10]
x=int(input("Which value are you find in list :-"))
i=0
for el in list1:
    if(el==x):
        print("Number found at ",i,"index")
        break
    i+=1
# Output-> Number found at  3 index

#💡for loop with else:-
# The else part execute only when the loop is finishes without a break 
# if the loop is stopped by a break,the else block is skipped
list=[5,6,9,3]
for el in list:
    print(el)
else:
    print("LOOP COMPLETELY WORK SUCCESSFULLY")

# Output-> 5,6,9,3,LOOP COMPLETELY WORK SUCCESSFULLY

#💡Some important keyword & function:-

#💡1.range()->
# range functions returns a sequence of no.,Starting from 0 (by default) and increment by 1 (by default) and stop before a speecified number

#💡Syntax of range()->       range(start,stop,step)

#💡There is 3 way to declare range()->

# 1.If we write range() with one value it considered as stop value. 
for el in range(5):
    print(el)

# 2.if we write range() with two value it considered 1st value as start(which is included) and 2nd value as stop(which is excluded).
for el in range(0,5):             
    print(el)

# 3.if we write range() with three value it considered 1st value as start(which is included) and 2nd value as stop(which is excluded) and third value as stepsize
for el in range(0,5,1):
    print(el)

'''here all the three program gives same Output->
0
1
2
3
4
'''
#💡Stepsize negative bhi ho sakta hai jab ham loop decreasing order mey chalaye gey:
for el in range(5,0,-1):
    print(el)
# Output-> 5,4,3,2,1

#💡2.break->             
# It is used to terminate the loop when encountered
# it stop loop immediately 
list1=[2,4,6,8,10]
x=int(input("Which value are you find in list :-"))
i=0
for el in list1:
    if(el==x):
        print("Number found at ",i,"index")
        break
    i+=1
# In this program you can see when x is found in the list1 after that loop is stop because of break keyword

#💡3.continue->
# It terminate execution in the current iteration & continue execution of the loop with the next iteration
# In Simple way we can say It skip current iteration without disturbing the whole loop
i=0
while (i<=5):
    if (i==3):
        i+=1
        continue
    print(i)
    i+=1
# Output-> 0,1,2,4,5 

#💡4.pass-> 
# pass is a null statement that does nothing.It is used as a placeholder for future code

# If I try to write only this :-
# for i in range(10)
# It throw an error 

# But If I write loop with using pass keyword it doesn"t throw an error
for i in range(10):
    pass  
# It Does Nothing
# No Output.

'''✅Summarization of Loop Control Keywords:-
✅break → Immediately exits the loop
✅continue → Skips to the next iteration
✅pass → Does nothing, used as a placeholder
'''

# for more knowledge go through the Python Documentation.
