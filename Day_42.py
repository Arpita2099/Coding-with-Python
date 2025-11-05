# Local and Global Variable in Python:
# A variablr is a named location in memory that stores a value. In Python, we can assign values to 
# variables using the assignment operator=. For instance,
x=5
y="Hello ! Everyone."
print(x)
print(y)

# Now, let's talk about local and global variables.

# A local variable is a variable that is defined within a function and only accessible 
# within that function. It is created when the function is called and is destroyed when
# the function returns.

# On the other hand, a global variable is a variable that is defined outside of a function
# in your code.

x=4
print(x)

def hello():
    x=5
    print(f"The local x is {x}")
    print("Hello Harry")
print(f"The global x is {x}")
hello()
print(f"The global x is {x}")

x=10
def my_function():
    y=5 # local variable
    print(y)
my_function()
print(x)
print(y) # This will cause an error because y is a local variable and not accesible outside of the function.

x=10
def my_function():
    global x
    x=15
    y=5 # local variable
    print(y)
my_function()
print(x)

# In this example, w used the global keyword to declarfe that we want to modify the global
# variable x from within the function. As a result, the value of x is changed to 5.

# It's important to note that it's generally considered good practice to avoid modifying
# global variables from within functions, as it can lead to unexpected behavior and make your 
# code harder too debug.

# I hope this tutorial has helped clarify the differences between local and global variables 
# and how to use the global keyword in Python.
