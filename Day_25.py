# Python Dictionary
# Dictionaries are ordered collection of data items.
# They store multiple items in a single variable.
# Dictionary items are key-value pairs that are seperated by commas and enclosed within curly brackets{}.
# For instance,
info={"Name":"Arpita Sah", "Age":"18","eligible":"True"}
print(info)
print(type(info))

# Accessing Dictionary items:
# 1. Accessing single values:
# Values in dictionary can be sccessed using keys. We can accessed using keys.
# # We can access dictionary values by mentioning keys either in square bracket or by 
# # using get method.
# For instance,
info={"Name":"Arpita Sah", "Age":"18","eligible":"True"}
print(info['Name'])
print(info.get('Age'))
print(info.keys())
print(info.values())

# Iteration on the dictionary:
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")
# This is all about the today coding.
