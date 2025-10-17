# Exception Handling in Python.
# Exception handling is the process of responding to unwanted or unexpected events 
# when a computer program runs. Exception handling deals with these events to avoid 
# the program or system crashing and without this process, 
# exceptions would disrupt the normal operation of a program.
# For instance,
a=input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
for i in range(1,11):
    print(f"{int(a)}X{i}={int(a)*i}")
# If I will give any string as input than it will throw error because
# String cannnot be converted into the integer so it will give error.
# and it I will use the try then it will not throw error rather it will give the exception value.

# Exceptions in Python
# Python has many built-in exceptions that are raised when your program encounters an error
# (something in the program goes wrong).
# When these exceptions occur, the Python interpreter stops the current process and passes
# it to the calling process until it is handled. If not handle, the program will crash.

# Python try...except
# try... except blocks are used in python to handle errors and exceptions. 
# The code in try block runs when there is no error. 
# If the try block catches the error, then the except block is executed.
# For instance,
a=input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)}X{i}={int(a)*i}")
except Exception as e:
    print(e)
print("Some important lines of code.")
print("End of Program.")

a=input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)}X{i}={int(a)*i}")
except Exception as e:
    print("Invalid Input.")
print("Some important lines of code.")
print("End of Program.")

# This is all about the today coding in Python.
