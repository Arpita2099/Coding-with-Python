# Recursion in Python
# Recursion is the process of defining something in terms of itself.
# A physical world example would be to place two parallel mirrors facing each other.
# Any object in between them would be reflected recursively.

# Python Recursive Function.
# In Python, we know that a function can call other functions.
# It even possible for the function to call itself.
# These types of construct are termed as recursive function.
# For instance,
def factorial(num):
    if (num==1 or num==0):
        return 1
    else:
        return (num*factorial(num-1))

# Driver Code:
num=7;
print("Number:",num)
print("Factorial:",factorial(num))


# Fibonacci Sequence:
def fibonacci(num):
    a=0
    b=1
    if (num==0 or num==1):
        return 1
    else:
        return ((num-1)+fibonacci(num-2))
num=10
print("Number: ",num)
print("Fibinacci Sequence: ")

for i in range(num):
    print(fibonacci(i), end=" ")
