# In this Day_8 of python code.
# Going to discuss about the string in python.

# String Definition?
# In python, anything that you enclosed between single or double quotation marks is considered a string.
# A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

# For instance,
name="Arpita Sah"
print("Hello, "+ name)

# String is the array of the collection.
Name="Amar Durgannav"
print(Name[0])
print(Name[1])
print(Name[2])
print(Name[3])

for i in Name:
    print(i)

# String Slicing
name="Arpita Sah"
print(name[0:6])

# Negative slicing
print(name[:-1])

# length of the string can be find out by using len() function.
print(len(name))

# String as an array.
# A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.
pie="Apple"
print(pie[:5])

name="Arpita"
print(name[-4:-2])

# String Methods:
print(name.lower())
print(name.upper())
Title="I am here for coding"
print(Title.title())
print(Title.capitalize())
print(name.replace("Arpita","Amar"))
print(name.split(" "))
print(len(Title.center(50)))
print(Title.endswith("coding"))
print(Title.find("am"))
print(Title.index("here"))
str="WelcometoPythonCoding"
print(str.isalnum())
str1="Arpita"
print(str1.isalpha())
str2="hello bro"
print(str2.islower())
str3="We wish you a Happy Dashai"
print(str3.isprintable())
str4="We wish you a Happy Dashai\n"
print(str4.isprintable())
str5="   "
print(str5.isspace())
str6="World Health Organization"
print(str6.istitle())
str7="SAH"
print(str7.isupper())

# So, this is all about the string in python.
