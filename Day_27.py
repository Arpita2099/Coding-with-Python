# Dictionary Methods in Python
# Dictionary uses sveral built-in methods for mmanipulation. They are listed below:

# update()
# The update() method updates the value of the key provided to it if the item already
# exists in the dictionary, else it creates a new key-value pair.
# For instance,
info={'name':'Arpita Sah','age':18, 'eligible':True}
print(info)
info.update({'age':20})
info.update({"DOB":2005})
print(info)

# Removing items from dictionary:
# They are a few methods that we can use to remove items from dictionary.

# clear()
# The clear() method removes all the items from the list.
# For instance,
information={'name':'Arpita Sah','age':18, 'eligible':True}
information.clear()
print(information)

# pop()
# The pop() method removes the key-value pair whose key is passed as a parameter.
# For instance,
info={'name':'Arpita Sah','age':18, 'eligible':True}
info.pop('eligible')
print(info)

# popitem():
# The popitem() method removes the last key-value pair from the dictionary.
# For instance,
info={'name': 'Amar Durgannav', 'age': 20, 'eligible': True, 'DOB': 2005}
info.popitem()
print(info)

# del:
# We can also use the del keyword to remove a dictionary item.
# For instance,
info={'name': 'Sabana Khatun', 'age': 20, 'eligible': True, 'DOB': 2005}
del info['name']
print(info)
# If key is not provided, then the del keyword will delete the dictionary entirely.
# For instance,
# info={'name': 'Sabana Khatun', 'age': 20, 'eligible': True, 'DOB': 2005}
# del info
# print(info)

# This all about today coding.
