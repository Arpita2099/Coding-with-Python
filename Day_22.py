# Sets in Python
# Sets are unordered collection of data items. 
# They store multiple items in a single variable. Set items are seperated by commas
# and enclosed within curly brackets{}.
# Sets are unchangeable, meaning you cannot change items of the set once created.
# Sets do not contain duplication items.

# For instance,
info ={'Arpita', 18, True, 3.8, 20}
print(info)
print()
s={2,4,2,4,6,8,6}
print(s)
# Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers.
# Also, sets do not allow duplication values.
# Try to create an empty set. Check using the type() function whether the type of your variable is a set.
arpita=set()
print(type(arpita))
print()

# Loop in set
for value in info:
    print(value)
print()

#Method in sets of Python
# Joining Sets
# Sets in python more or less work in the same way as sets in mathematics.
# We can perform operations like union and intersection on the sets just like in mathematics.

# Union() and update():
# The union() and update() methods prints all items that are present in the two sets.
# The union() method return a new set whereas update() method adds item into the existing set from another set.
# For instance,

cities={"Tokyo","Madrid","Berlin","Kathmandu"}
cities2={"Tokyo","California","Madrid","Kabul"}
cities3=cities.union(cities2)
print(cities3)
print()
print("Union on the sets.")
s1={1,3,5,7,9}
s2={1,2,3,4,5}
print(s1.union(s2))
print()
print("Update in the sets.")
s2.update(s1)
print(s1)
print(s2)
print()

# Intersection and intersection_update():
# The intersection() and intersection_update() methods prints only
# items that are similar to both the sets. The intersection() method returns a new set whereas 
# intersection_update() method updates into the existing set from another set.

# For instance,
cities={"Tokyo","Madrid","Berlin","Kathmandu"}
cities2={"Tokyo","California","Madrid","Kabul"}
cities3=cities.intersection(cities2)
print("Intersection on sets:")
print(cities3)
print()
print("Intersection update:")
cities2.intersection_update(cities)
print(cities)
print(cities2)
