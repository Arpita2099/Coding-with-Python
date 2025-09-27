# In the day 9 of python coding.
# Today I am going to code in if-else statement of the python.

# if-else Statements
# Sometimes the programmer needs to check the evaluation of certain expression(s).
# Whether the espression(s) evaluate to True or False. If the expression evaluates to False,
# then the program execuation follows a different path than it would have if the expression had evaluated to True.

# Based on this, the conditional statements are further classified into following types:
# if
# if-else
# if-else-elif
# nested if-else-elif

# Use of if statement in the python.
age=int(input("Enter your age: "))
print("Your age is: ",age)
if age>=18:
    print("You are eligible to Vote.")
    print("You are able for gatting driving license.")

# Use of else-if ststement in the python.
num=int(input("Enter any number: "))
if num%2==0:
    print(f"{num} is an Even Number.")
else:
    print(f"{num} is an Odd Number.")

# Use of if-else-elif statement in the Python Programming Language.
marks=int(input("Enter the marks: "))
if marks>=90:
    print("You receive A+ Grade.")
elif marks>=80:
    print("You Received A Grade.")
elif marks>=70:
    print("You Received B+ garde.")
elif marks>=60:
    print("You Received B Grade.")
else:
    print("You are Failed No Grade.")

# Use of nested if-else-elif in the Python Programming Language.
num=18
if num<0:
    print("Number is Negative.")
elif num>0:
    if num<=10:
        print("Number is between 1-10.")
    elif num>10 and num<=20:
        print("Number is between 11-20.")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")

