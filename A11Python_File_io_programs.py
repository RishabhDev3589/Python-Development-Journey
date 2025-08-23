print("JBMNMJ")
'''
🔍 Topics Covered →
✅ File Handling Basics (Text vs Binary Files)
✅ File Opening Syntax: open() vs with open()
✅ File Modes: r, w, a, x, r+, w+, a+, t, b
✅ Reading Methods: .read(), .readline(), .readlines()
✅ Writing Methods: .write()
✅ Pointer Operations: seek(), tell()
✅ Difference Between Truncate vs Append Behavior
✅ Using os Module to Delete Files Safely
✅ Practical Examples with Before & After File Content
✅ Clean Code with Real-Time File Content Changes and Comments
'''

#💡File I/O in Python->
# Python can be used to perform operation on a file (read & write data)
#💡Types of all files:-
# 1.Text Files:- .txt,.docx.log,etc.
# 2.Binary Files:- .mp4,.mov,.png,.jpeg,etc. 

# Open,read & Close File->
# we have to open a file before reading or writing

#💡There is Two Syntax of File I/O in Python:-

#💡1.Normal Syntax:-
''' f=open("file_name","mode"):     # Opening the File
    data=f.read()                   # For Reading
    print(data)
    f.write("Content")              # For Writing {For next line we use '\n'}
    f.close()                       # Closing the File
'''
#💡with Syntax:-
'''
with open("File_name","mode") as f: # Opening the File
    data=f.read()                   # For Reading
    print(data)
    f.write("Content")              # For Writing {For next line we use '\n'}
'''
#Note: When using the with statement, it is not necessary to manually close the file — it is automatically closed when the block is exited, even if an error occurs.

# Both Syntax Work same.
# The with statement is the modern and recommended way to handle file operations in Python, as it ensures proper resource management and automatically closes the file.

#💡Modes in file I/O ->

# 1. Read("r"):- Open For reading (By default)
# 2. Write("w"):- Open For writing, "# It immediately truncates (clears) the file upon opening
# 3. Append("a"):- Open For Writing without Truncating the file appending to the end of the file if it exists
# 4. Creating a File("x"):- It create a new file and open it for writing
# 5. Binary mode("b"): used for binary files (like images or videos)"
# 6. Text("t"):- Text Mode (By default)
# 7. "+":- open a disk file for updating (reading & writing)

#💡Some IMP. Modes with "+"->

#   MODES -> DESCRIPTION        WRITING BEHAVIOR             POINTER 
# 1. r+ -> read + write         overwrite                   At Start (No Truncate)
# 2. w+ -> write + read         overwrite                   At Start Truncate (it means the data is deleted from the file for upcoming progess)
# 3. a+ -> append + read        append only                 At End   (No Truncate) (After last line)

'''💡Detailed Explanation:-

1.(r+)–> Read and Write:
Opens file for both reading and writing.
Does not truncate the file.
Starts writing from the beginning, so it may overwrite existing content, but doesn't delete it entirely.
File must exist
# IMP-> If you call the write or append & If the file doesn't exist, it will be created automatically before performing write or append operations.

2.(w+)–> Write and Read:
Opens file for writing and reading.
Truncates (clears) the file immediately on open.
File content is deleted first, then writing starts from beginning.
If file doesn't exist, it's created.

3.(a+)–> Append and Read:
Opens file for reading and appending.
Does not truncate file.
Write pointer is always at the end, so writing will only append to the file.
Reading is possible, but you must use seek(0) if you want to read from start.

'''
#💡Pointer Operations
# seek(offset): Moves the pointer to given byte
# tell(): Returns the current position of the pointer

#💡Reading a file->
# There is 3 way to read a file:-

#💡1st.way->                       # read Entire file
f=open("demo.txt","r")
data=f.read()
print(data)
f.close() 
# Output-> JBMNMJ
#          HEY GOOD MORNING

#In this approach, you first read and store the data from the file into a variable, and then display it using print().

#💡2nd.way->                       # read one line at one time
f=open("demo.txt","r")
data=f.readline()
print(data)
# Output-> JBMNMJ
data=f.readline()
print(data)
# Output-> HEY GOOD MORNING

# for reading All Lines as List->
with open("demo.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# In this Way you read the data line by line from the file

#💡3rd.way-> Reading a specific number of characters from the file (based on position/index)
f=open("demo.txt","r")
data=f.read(6)
print(data)
# Output-> JBMNMJ               <-pointer at J           
data=f.read(17)
print(data)
# Output-> HEY GOOD MORNING     <-pointer at G
data=f.read(5)
print(data)
f.close() 
# Output-> Nothing (Because my pointer are at G and after G there is not any words in demo file so therefore it return nothing)

# File I/O is based on pointers. If the pointer is at the start, you can read the data from the beginning.

#💡Writing a file->
# There is 2 way to  write in file:-

#💡1st. using write (It truncate the file and then write)
f=open("demo.txt","w")
f.write("HEY EVERYONE")
f.close() 
# Before the code:*(demo.txt)->
'''JBMNMJ
HEY GOOD MORNING'''
# After the code execution:*(demo.txt)->
'''
HEY EVERYONE
'''

#💡For Next line we use \n For example:-
f=open("demo.txt","w")
f.write("HEY EVERYONE\nTODAY I WANT TO SAY ABOUT MY PAST 4 YEAR EXPERIENCE")
f.close() 
# Before the code:*(demo.txt)->
'''
HEY EVERYONE
'''
# After the code execution:*(demo.txt)->
'''
HEY EVERYONE
TODAY I WANT TO SAY ABOUT MY PAST 4 YEAR EXPERIENCE
'''

#💡2. using append(it append the file and write)
f=open("demo.txt","a")
f.write("\nSO LET'S START")
f.close()
# Before the code:*(demo.txt)->
'''
HEY EVERYONE
TODAY I WANT TO SAY ABOUT MY PAST 4 YEAR EXPERIENCE
'''
# After the code execution:*(demo.txt)->
'''
HEY EVERYONE
TODAY I WANT TO SAY ABOUT MY PAST 4 YEAR EXPERIENCE
SO LET'S START
'''

#💡Let's move on the "+" mode operations->

#💡1st.->
with open("demo.txt","r+") as f:
    data=f.read()
    print(data)
    f.write("\nLET'S CREATE SOME GOOD GAME")
    d=f.read()
    print("file data:-",d)        # pointer at last position so that's why it doesn't show anything
# Before the code:*(demo.txt)->
'''
HEY EVERYONE
TODAY I WANT TO SAY ABOUT MY PAST 4 YEAR EXPERIENCE
SO LET'S START
'''
# After the code execution:*(demo.txt)->
'''
HEY EVERYONE
TODAY I WANT TO SAY ABOUT MY PAST 4 YEAR EXPERIENCE
SO LET'S START
LET'S CREATE SOME GOOD GAME
'''

# So here we can see that "r+" allows both reading and writing without truncating the file.
# Since we read the entire file first, the write pointer moves to the end — so the new content gets appended, not overwritten.

#💡2nd.->
with open("demo.txt","w+") as f:
    f.write("LET'S CREATE SOME GOOD GAME WITH GOOD UI")
    f.seek(0)                # Move pointer to beginning
    data = f.read()
    print(data)

# Output-> LET'S CREATE SOME GOOD GAME WITH GOOD UI

# Before the code:*(demo.txt)->
'''
HEY EVERYONE
TODAY I WANT TO SAY ABOUT MY PAST 4 YEAR EXPERIENCE
SO LET'S START
LET'S CREATE SOME GOOD GAME
'''
# After the code execution:*(demo.txt)->
'''
LET'S CREATE SOME GOOD GAME WITH GOOD UI
'''
# Explanation:
# The "w+" mode opens the file for both writing and reading.
# It immediately truncates (clears) the file when opened.
# Since we used f.seek(0) after writing, we can read the new content from the start

#💡3rd.->
with open("demo.txt","a+") as f:
    f.write("\nLET'S WATCH SOME MOVIES")
    f.seek(0)                # read from beginning
    data = f.read()
    print(data)

'''Output-> LET'S CREATE SOME GOOD GAME WITH GOOD UI
LET'S WATCH SOME MOVIES '''

# Before the code:*(demo.txt)->
'''
LET'S CREATE SOME GOOD GAME WITH GOOD UI
'''
# After the code execution:*(demo.txt)->
'''
LET'S CREATE SOME GOOD GAME WITH GOOD UI
LET'S WATCH SOME MOVIES
'''

# Explanation:
# The "a+" mode opens the file for both appending and reading.
# It does NOT truncate the file — existing content remains unchanged.
# Any new content written is always added at the end of the file.
# To read the full content, we must manually move the pointer to the beginning using f.seek(0).
# In this example, the new line is appended, and then the entire file is read from the beginning.


#💡Deleting the file->
# We delete a file using os module
# module(like a code library) is a file written by another programmer that generally has a function we can use
#⚠️ Be careful with os.remove(); always double-check the filename!

import os

files = os.listdir()                
print("Files:", files)              # it shows all the file
# Output-> [It show list of Your existing File]

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
    print("File deleted successfully")
else:
    print("File not found")

# Output-> File deleted Successfully

#💡✅ Summary of File I/O Modes in Python->
'''
💡File Opening Modes:

| Mode | Description         | Truncates File?   | Pointer Starts At | Creates File if Not Exists?   |
|------|---------------------|-------------------|-------------------|-------------------------------|
| 'r'  | Read Only           | ❌ No            | Start              | ❌ No                        |
| 'w'  | Write Only          | ✅ Yes           | Start              | ✅ Yes                       |
| 'a'  | Append Only         | ❌ No            | End                | ✅ Yes                       |
| 'r+' | Read + Write        | ❌ No            | Start              | ❌ No                        |
| 'w+' | Write + Read        | ✅ Yes           | Start              | ✅ Yes                       |
| 'a+' | Append + Read       | ❌ No            | End                | ✅ Yes                       |
| 'x'  | Create Only (Write) |❌ Error if exist | Starts             | ✅ Yes(only if doesn't exist)|

📝 Notes:
- Truncate → Clears existing file content when opening the file.
- In modes like 'a' and 'a+', writing always happens at the end of the file.
- Always use `with open()` for better file handling — it closes the file automatically.
- "x" mode creates a new file, and throws an error if the file already exists.
'''

'''💡File Methods:-
f.read()        # Reads entire file
f.readline()    # Reads one line at a time
f.readlines()   # Reads all lines as a list
f.write()       # Writes to the file
f.seek(pos)     # Moves pointer to specified position
f.tell()        # Returns current pointer position
f.close()       # Closes the file (auto with 'with')
'''

# for more knowledge go through the Python Documentation