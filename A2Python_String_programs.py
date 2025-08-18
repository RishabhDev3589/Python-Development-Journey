print("JBMNMJ")

#💡String-> it's a datatype that stores a sequence of characters.
# String are Immutable 

#💡String {Sentence,Mix-up of words/values} (' '," ",''' ''')<-3 Way to put the value on string
name1='Rishabh'
name2="Rishabh"
name3='''Rishabh'''
print(name1,name2,name3)

#💡escape sequence characters:-
# 1.\n -> it's use for nextline command
# 2.\t -> it's use for take a space of tab 

#💡String have a Indexing Symtem starting with 0 {it's help to access the character}
print(name1[0])
#Output-> R
print(name1[5])
#Output-> b

#💡print every character using loop->
print("")
for character in name1:
    print(character)
    
#💡String Slicing->

# 1. Positive Slicing
listname='Rishabh','Rashmi'
names="Raghunath"

print(listname[1])
#Output-> Rashmi

print(names[0:9]) # here o is included but 10 is excluded
#Output-> Raghunath

print(names[5:10])
#Output-> nath

# 2. Negative Slicing
print(names[0:len(names)])
#Output-> Raghunath

print(names[0:-1]) # here when python see -1 it see like this len(names)-1 its make -1 into 8 According to the names string
#Output-> Raghunat

print(names[-9:-4]) # here when python see -9 to -4 it see like this len(names)-9 to len(names)-4 it make into [0:5] According to the names string
#Output-> Raghu

print(names[-4:-9]) # here when python see -4 to -9 [5:0] it doesn't make any sense So that's why it doesn't show any value
#Output-> no output

print(names[:5]) # here when python interpeter does not see any value before : it consider 0 on that place 
#Output-> Raghu

print(names[5:]) # here when python interpeter does not see any value after : it consider len(string) on that place 
#Output-> nath

print(names[:]) # here when python interpeter does not see any value after & before : it consider [o:len(string)] on that place 
#Output-> Raghunath

#💡To Find the length of string we use len()<- length function
print(len(names))

#💡String Methods

#💡1.Convert your string in uppercase using upper()
print(names.upper())
#Output-> RAGHUNATH

#💡2.Convert your string in lowercase using lower()
print(names.lower())
#Output-> rughunath

# IMP. note:- In Python strings are Immutable. yaha par names naam ka string upper ya lower case mey change nahi hoga balki ye ek naye string mey store kar deygaa
# if you want to make changes in your original string then write ->
'''names=names.upper()
print(names)
*Output-> RAGHUNATH'''

#💡3.Removes continues character which is in the last / end in the string using rstrip()
continues="Rishabh!!!"
print(continues.rstrip('!'))
#Output-> Rishabh 

#💡4.Replace Method ->replace() for replacing the old value in new value
parag="Rishabh is a good person. Rishabh is always says true. Rishabh is a honest person" 
print(parag.replace("Rishabh","Rishi")) # replace all Rishabh word with Rishi in the string
#Output-> Rishi is a good person. Rishi is always says true. Rishi is a honest person

#💡5.Split Method-> split()
# it create a list 
splitf="Rishabh like kajukatli" # here space is must between your string words.
print(splitf.split())
#Output->['Rishabh', 'like', 'kajukatli']

#💡6.Capitalize Method-> capitalize() *it capitalize the first letter of your string & also make all other letter in lowerr case
capital="hey Friends"
print(capital.capitalize())
#Output-> Hey friends

#💡7.Center Method-> center()
str1="Welcome to the Console!!!"
print(str1.center(150)) # yaha par str1 ki length 25 hai aur 150 extra add hoga jissey content center mey aa jaye gaa
#Output->                                             Welcome to the Console!!!

#💡8.count Method-> count()
cou="rishi,rishabh,rashmi,rishi,gautami"
print(cou.count("rishi")) # its returns the no. of times the given value has occured within the given string
#Output-> 2

#💡9.endswith Method-> endswith()
str1="Welcome to the Console!!!"

print(str1.endswith("!!!")) # It checks if the string ends with a given value then return True  else return False
#Output-> True

print(str1.endswith("to",4,10)) # ham chahey toh specific indexing kar key bhi uss jagah key bech mey wo value hai ki nahi ye check kar saktey hai
#Output-> True

#💡10.find Method-> find()
# it searches for the first occurrence of the given value and return the index where it is present.If given value is absent from the string then return -1
print(str1.find("to"))
#Output-> 8

#💡11.index Method-> index()
print(str1.index("to")) # it's same as find method. it has only one difference if given value is absent from the string then raise an exception 
#Output-> 8

#💡12.isalnum Method-> isalnum()
print(str1.isalnum()) # It returns True only if the entire string consists of A-Z, a-z, 0-9 .If any other characters or punctuations are present, then it returns False
#Output-> False

#💡13.isalpha Method-> isalpha()
print(str1.isalpha()) # It's the same as isalnum() method. It has only one difference:- it doesn't consider numbers
#Output-> False

#💡14.islower Method-> islower()
print(str1.islower()) # It returns True only if all the characters in the string are in lowercase.(All lowercase)->True, otherwise False
#Output-> False

#💡15.isprintable Method-> isprintable()
print(str1.isprintable()) # If It can print all letters, so it returns True, but if there's any character that cannot be printed for example:- \n,etc ,it returns False)
#Output-> True

#💡16.isspace Method-> isspace()
print(str1.isspace()) # It returns True only and only if the String contains white spaces, else returns False
# If it's only spaces, it's True; if even one character appears, it's False
#Output-> False

#💡17.istitle Method-> istitle()
print(str1.istitle()) # It returns True only if the first letter of each word of the string is capitalized, else it returns False
#Output-> False

#💡18.isupper Method-> isupper()
print(str1.isupper()) # sab upper case me hai toh True nahi toh False
#Output-> False

#💡19.startswith Method-> startswith()
print(str1.startswith("Welcome")) # It's the same as endswith(). It has only one difference: it checks from the starting
#Output-> True

#💡20.swapcase Method-> swapcase()
print(str1.swapcase()) # It changes the character casing of the string
#Output-> wELCOME TO THE cONSOLE!!!

#💡21.title Method-> title()
print(str1.title()) # It capitalizes each letter of the word within the string.
#Output-> Welcome To The Console!!!

# ---It's All About String & it's Operation In Python--- 


