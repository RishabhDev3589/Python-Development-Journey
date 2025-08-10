# Calculator using Match_Case
print("Welcome to Python World")
print("Let's Make Arithmetical Operation")
print("To Perform This Please Enter 2 Values")
num1=float(input("Enter Your 1st value:-"))
num2=float(input("Enter Your 2nd value:-"))
print("Select the Arithmetical Operation you want:-\nCode 1 for Addition\nCode 2 for Subtraction\nCode 3 for Multiplication\nCode 4 for Division\nCode 5 for Modulus\nCode 6 for Pure Division\nCode 7 for Exponential Power ")
code=int(input("Enter the Code operation:-"))
match code:
    case 1:
        add=num1+num2
        print("The Addition of Two Number is",add)
    case 2:
        sub=num1-num2
        print("The Subtraction of Two Number is",sub)
    case 3:
        multi=num1*num2
        print("The Multiplication of Two Number is",multi)
    case 4:
        div=num1/num2
        print("The Division of Two Number is",div)
    case 5:
        mod=num1%num2
        print("The  Reminder of Two Number is",mod)
    case 6:
        pure_div=num1//num2
        print("The PureDivision of Two Number is",pure_div)
    case 7:
        expo=num1**num2
        print("The power of Two Number is",int(expo))
    case _:
        print("Code is not valid") 
print("\nThanks Later")
print("JBMNMJ")
feedback=input("Give your feedback:- ")