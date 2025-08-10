print("Welcome To KBC [Kon Baneyga Crorepati]\nFirst go through the rules & regulation:-\n")
print('''🚨 Important Rules:-
1. Contestants can quit at any time and take the current amount.
2.Wrong answer before safety level → walk away with lower or no amount.
3.Answers are final once locked by saying “Lock kiya jaye”.''')
amount=0

def questions(a):
    
    print("\nQ1. Which gas is most abundant in the Earth atmosphere?")
    print('''A. Oxygen
B. Carbon Dioxide
C. Hydrogen
D. Nitrogen ''')
    ans1=input("Select your Answer:-")
    print("Selected Answer ko Lock Kiya Jaye🔐")
    if(ans1=='D'):
        print("Sahi Jawab🎉")
        a=amount+500000
        print('Ab tak ki Dhanrashi💰',a)
    else:
        print("Galat Jawab❌")
        a=amount-200000
        print('Ab tak ki Dhanrashi💰',a)
        
    
    print("\nQ2. Which is the longest river in the world?")
    print('''A. Amazon
B. Nile
C. Yangtze
D. Mississippi ''')
    ans2=input("Select your Answer:-")
    print("Selected Answer ko Lock Kiya Jaye🔐")
    if(ans2=='B'):
        print("Sahi Jawab🎉")
        a=a+700000
        print('Ab tak ki Dhanrashi💰',a)
    else:
        print("Galat Jawab❌")
        a=a-300000
        print('Ab tak ki Dhanrashi💰',a)
        
    print("\nQ3. What is the unit of electrical resistance?")
    print('''A. Volt
B. Ohm
C. Ampere
D. Watt ''')
    ans3=input("Select your Answer:-")
    print("Selected Answer ko Lock Kiya Jaye🔐")
    if(ans3=='B'):
        print("Sahi Jawab🎉")
        a=a+1000000
        print('Ab tak ki Dhanrashi💰',a)
    else:
        print("Galat Jawab❌")
        a=a-500000
        print('Ab tak ki Dhanrashi💰',a)
        
    print("\nQ4. In which year did India win its first Cricket World Cup?")
    print('''A. 2003
B. 1996
C. 1983
D. 1975 ''')
    ans4=input("Select your Answer:-")
    print("Selected Answer ko Lock Kiya Jaye🔐")
    if(ans4=='C'):
        print("Sahi Jawab🎉")
        a=a+1500000
        print('Ab tak ki Dhanrashi💰',a)
    else:
        print("Galat Jawab❌")
        a=a-700000
        print('Ab tak ki Dhanrashi💰',a)
        
    print("\nQ5. Who was the first woman to win a Nobel Prize?")
    print('''A. Marie Curie
B. Jane Goodall
C. Rosalind Franklin
D. Ada Lovelace ''')
    ans5=input("Select your Answer:-")
    print("Selected Answer ko Lock Kiya Jaye🔐")
    if(ans5=='A'):
        print("Sahi Jawab🎉")
        a=a+2000000
        print('Ab tak ki Dhanrashi💰',a)
    else:
        print("Galat Jawab❌")
        a=a-1000000
        print('Ab tak ki Dhanrashi💰',a)
                
    return a
prize=questions(amount)
print('\nAap ki Dhanrashi💰',prize)
#amount=amount+prize   
