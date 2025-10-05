# In Day 17 of Python Code, I am going to do code related to Function on Python.

# Python Function
# QA function is a block of code that performs a specific task whenever it is called. 
# In bigger programs, where we have large amounts of code, it is advisable to create or use exisiting
# functions that make the program flow organized and neat.

# There are two types of functions:
# 1. Built-in Functions
# 2. User-defined Functions

# Built-in Functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follow:
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(),etc.

# User-defined Functions:
# We can create functions to perform dpecific tasks as per our needs. Such functions are called user-defined functions.
def calculate_Gmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
a=9
b=8
if(a>b):
    print("First Number is greater.")
else:
    print("Second Number is greater.")
calculate_Gmean(a,b)

c=5
d=9
if(c>d):
    print("First Number is greater.")
else:
    print("Second Number is greater.")
calculate_Gmean(c,d)
print()

def Gmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isGreater(a,b):
    if (a>b):
        print("First Number is greater.")
    else:
        print("Second Number is greater.")

a=10
b=15
isGreater(a,b)
Gmean(a, b)

c=14
d=19
isGreater(c,d)
Gmean(c,d)

# Fuunction Arguments in Python
# Function Arguments and return statement
# There are four types of arhumwnts that we cab provide in a function:
# Default Arguments
# Keyword Arguments
# Variable leangth Arguments
# Required Arguments

# Default Arguments:
# We can provide a default value while creating a function.
# This way the function assumes a default value if a value ia not
# provided in the function call for that argument.
# For instance,
def name(fname,mname="Kumari", lname="Shah"):
    print("Hello",fname,mname,lname)
name("Arpita")
name("Amrita","", "Hazara")

def average(a=4,b=5):
    print("The average is",a+b/2)
average(2,8)
average(10,40)
print()
# Variable length Arguments:
# Sometimes we may need to pass the arguments than those defined in the actual function.
# This can be done using variable length arguments.
# There are two ways to achieve this:
# Arbitrary Arguments:
# While creating a function, passs a* before the parameter name while defining the function.
# The function accesses the arguments by processing them in the form of tuple.
# For instance,
def name(*name):
    print("Hello",name[0],name[1],name[2],name[3])
name("Arpita","Amar","Waston","Yograj")
print()

def average(*number):
    sum=0
    for i in number:
        sum=sum+i
    print("Average is: ", sum/len(number))
average(23,56,78,90,80)
print()

def name(**name):
    print("Hello", name["fname"],name["mname"],name["lname"])
name(mname="Buchanan",lname="Barnes",fname="James")
print()
# return statement
# The return statement is used to return the value of the expression back to the calling function.
def average(*num):
    sum=0
    for i in num:
        sum=sum+i
    return sum/len(num)
c=average(5,6,7,1)   
print(c)
