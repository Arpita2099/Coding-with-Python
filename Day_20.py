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
