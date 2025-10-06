# In the Day 20 of coding in Python
# I am going to do code for python list.
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets[].
# Lists are changeable meaning we can alter then after creation.
# For instance,
List1=[1,2,3,4,5,6]
List2=["Arpita","Yograj","Wastan","Ragini","Naresh"]
print(List1)
print(List2)

marks=[5,6,7,8,9]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
if 8 in marks:
    print("Yes!")
else:
    print("No!")
print(marks[1:])
print(marks[1:4:2])
# In the list we can also print the different types of datatypes together.
# For instance,
L=["Hello",12,15.7,True,'''hello Ji, Kaise hai aap.''']
print(L)
print(L[-3])

# Same thing applies for strings as well!
if "Arpi" in "Arpita":
    print("Yes")
else:
    print("No")

# List Comprehension
list=[i*i for i in range(10)]
print(list)

l=[i for i in range(1,11) if i%2==0]
print(l)

# List Methods in Python
# list.sort()
# This method sorts the list in ascending order. The original list is updated.
# For instance,
colors=["Red","Pink","Blue","Purple"]
colors.sort()
print(colors)

number=[9,6,7,4,1,2,3,90,67,5]
number.sort()
print(number)
number.append(10)
print(number)

# What if you want to print the list in descending ordered?
# We must give reverse=True as a parameter in the sort method.
# For instance,
number.sort(reverse=True)
print(number)

number.reverse()
print(number)

print(number.index(90))
print(number.count(10))
a=number.copy()
a[0]=12
print(a)
m=[20,30,40]
a.extend(m)
print(a)

# This is all about the today coding.
