# In the Day 20 of coding in Python.
# I am going to code for the tuple in Python.

# Python Tuple:
# Tuples are ordered collection of data items.
# They store multiple items in a single variable.
# Tuple items are seperated by commas and enclosed within rounded brackets().
# Tuples are unchangeable meaning we can not alter them after creation.

# For instance,
tuple1=(1,2,3,4,4,5,5,6)
tuple2=("Red","Black","Blue","White")
print(tuple1)
print(tuple2)

details=("Amar Durgannav","21","MBBS","Second Year","5.2")
print(details)

print(tuple1[0])

# We can not edit the original tuple as a list.
# If we do it will shoe error.
# 'tuple' object does not support item assignment
# For instance,
# tuple1[6]=10
# print(tuple1)

# Operation in tuple
# Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, then
# first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.
# For instance,
countries=("Nepal","Spain","Italy","England")
temp=list(countries)
temp.append("Russia") # Adding item
temp.pop(3) # Removing item
temp[2]="Finland" # Changing item
countries=tuple(temp)
print(countries)

# Thus we can tuple to a list, manipulate items of the list using list methods, then
# convert list back to a tuple.

# However, we can directly concatenate two tuples without converting them to list.
# For instance,
countries1=["Nepal","Bangladesh"]
countries2=["India","China"]
SouthEastAsia=countries1+countries2
print(SouthEastAsia)

# At last as we didi in the list. Tuple are also same for all function as list.

