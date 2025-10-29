# # Function Definition: Function is basically a block of code in python.
# Type of Function
# 1. Built-in-Function: Already build function i.e. print(), input(),..., ectc.
# 2. User define Function: Now in below we are going to discussion about the user 
# define function in details:

# How function look like:
# def is_even(i): Here, def is the keyword in function, is_even is the name of function, and i is the parameter or argument of function.
# """ Here we can write about what you want to print in the function in details that if someone want to do some change then get ideal from here.""" and it is call doxt-string
# print("Inside is_even"). This is the body of function.
# return i%2==0. This is the body of function.
# is_even(3). This is called 

def display(): # Function definition or header.
    print("This is an online class.") # Function body
print("This is outside the function")
display() # Function invocation/calling of function.
# Rules of writing the function means cannot use the reserve word.

# Add two number:
def sum_num(a,b):# Formal parameter
    sum=a+b
    return sum
sum_num(3,6) # arguments

def add(a,b):
    return a+b
c=add(3,8)
print(c)

def average(*args):
    sum,count=0,0
    for i in args:
        sum=sum+i
        count=count+1
    return sum/count
print("The average of three number are: ",average(10,30,40))
print("The average of three number are: ",average(10,30,40,50,20))
