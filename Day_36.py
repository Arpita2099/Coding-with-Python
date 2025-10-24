# How importing in Python
# Importing in Python is the process of loading code from a Python into the current script.
# This allows you to use the functions and variables defines in the module in your current
# script, as well as any additional modules that the imported module may depend on.

# To import a module in Python, you use the import statement followed by the name of the 
# module. For instance, to import the math module, which contains a variety of mathematical
# functions from the math module, you would use the following statement:

import math

# Once a module is imported, you can use any of the functions and variables defined in the 
# module by using the dot notation. For instance, to use the sqrt function from the math 
# module, you would write:

import math
result=math.sqrt(25)
print(result)
print(math.factorial(7))
print(math.floor(2.6789))

# From keyword
# You can also import specific functions or variables from a module using the from keyword.
# For instance, to import only the sqrt function from the math module, you would write:

from math import sqrt
result=sqrt(100)
print(result)

# You can also import multiple functions or variables at once by separating them with a comma:
from math import sqrt, pi
result=sqrt(49)
print(result)
print(pi)

# Importing everything
# It's also possible to import all function and variables from module using the *wildcard.
# However, this is generally not recommended as it can lead to confusion and make it harder
# to understand where specific functions and variables are coming from.

from math import *
result=sqrt(64)
print(result)
print(factorial(5))

# Python also allows you to rename imported modules using the as keyword. This can be useful
# if you want to use a shorter or more descriptive name for a module, or if you want to 
# avoid naming conflicts with other modules or variables in your code.

# The "as" keyword
import math as m
result=m.floor(12.90)
print(result)
print(m.pi)

# The dir function
# Finally, Python has a built-in function called dir that you can use to view the names of 
# all the functions and variables defined in a module. This can be helpdul for exploring and 
# understanding the contents of a new module.

import math
print(dir(math))

# This will output a list of all the names defined in the math module, including functions 
# like sqrt and pi, as well as other variables and constants.
# In summary, the import statement in Python allows you to access the functions and 
# variables defined in a module from within your current script. You can import the entire 
# module, specific functions or variables, or use the * wildcard to import everything. You 
# can use the as keyword to rename a module, and the dir function to view the contents of a module.
