# Rasing Costom Errors in Python.
# In Python, we can raise custom errors by using the raise keyword.
# For instance,
salary=int(input("Enter the amount of salary: "))
if not 3000<salary<6000:
    raise ValueError("Not a valid salary.")

# Defining Custom Exceptions
# In python, we can define custom exceptions by creating a new class that is derived from
# the built-in Exception class.
# Here's the syntax to define custom execptions:
# class CustomError(Exception):
    # code .....
    # pass
# try:
    # code .....
# raise CustomError:
    # code .....
# This is useful because sometimes we might want to do something when a particular
# exception is raised. For example, sending an error report to the admin, calling an api,etc.

a=int(input("Enter any value between 5 and 9."))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9.")

# This is all about the today coding.
