# String Formating in Python:
# String formatting can be done in python using the format method.
# For instance,
txt="For only {price:.2f} dollars!"
print(txt.format(price=49))

# f-string in python
# It is a new string formatting mechanism introduced by the PEP.
# It is also known as Literal String Interpolation or more commonly
# as F-strings (f character preceding the string literal).
# The primary focus of this mechanism is to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the f-string itself.
# The f-string can be formmated in much same as the str.format() method.
# The f-string offers a convenient way to ambed Python expression inside string literals for formatting.

# For instance,
str='Arpita'
print(f"{str} is {str} sah for {str} reason.")

# Docstrings in Python
# Python docstrings are the string literals that apper right after the definition of a function, method, class, or module.
# For instance,
def square(n):
    '''Takes a number as n, returns the square of n.'''
    print(n**2)
square(5)
print(square.__doc__)

# Here,''' Takes a number as n, returns the square of n''' is docstring which will not apper in output.

# Python Comments Vs Docstrings
# Python Comments
# Comments are description that help programmers better understand the intent and
# functionality of the program. They are completely ignored by the python interpreter.

# python docstrings
# As mentioned above, python docstrings are strings used right after the definition of a function,
# method, class, or module (like in Example 1). They are used todocument our code.
# We can access these docstrings using the doc attribute.

# Python doc attribute
# Whenever string literals are present just after the definition of a function, module, class or method.
# Docstring is written below the function only.

# PEP 8
# PEP 8 is a document that provides guidelines and best practices on how to write Python code.
# It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. 
# The primary focus of PEP 8 is to improve the readability and consistency of Python Code.

# PEP stands for Python Enhancement Proposal, and there are several of them.
# A PEP is a document that describes mew features proposed for Python and documents aspects of python.
# like design and style, for the community.

# The Zen of Python
# Long time Pythoneer Time Peter succincity channels the BDFL's guiding principles for Python's design into 20 aphorisms,
# only 19 of which have been written down.

# To open this
# Go to the terminl
# And type python3
# And import this,
# And enter 
# You will get the poem related to python programming language.
