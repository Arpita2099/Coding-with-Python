# Symmetric_difference and symmetric_diffrence_update():
# The symmetric_diffrence() and symmetric_diffrence_update()
# methods prints only items that are not similar to both the sets.
# the symmetric_diffrence() method return a new set whereas
# symmetric_difference_update() method updates into the existing set from another set.

# For instance,
cities={"Tokyo","Madrid","Berlin","Kathmandu"}
cities2={"Tokyo","California","Madrid","Kabul"}
cities3=cities.symmetric_difference(cities2)
print(cities3)

# Sets Methods
# There are several in-built methods used for the manipulation of set.
# They are explained below:

# isdisjoint():
# This isdisjoint() method checks if items of given set are present in another set. 
# This method returns False it iteams are present, else it returns True.
cities={"Tokyo","Madrid","Berlin","Kathmandu"}
cities2={"Tokyo","California","Madrid","Kabul"}
cities3=cities.isdisjoint(cities2)
print(cities3)

# issuperset():
# The issuperset() method checks if all the items of a particular set are present
# in the origin set. It returns True if all the items are present, else it return False.
cities={"Tokyo","Madrid","Berlin","Kathmandu"}
cities2={"Tokyo","California","Madrid","Kabul"}
cities3=cities.issuperset(cities2)
print(cities3)

# issubset()
# The issubset() method checks if all the items of the original set are present in the particular set.
# It returns True if all the items arae present, exit it returns False.
cities={"Tokyo","Madrid","Berlin","Kathmandu"}
cities2={"Tokyo","California","Madrid","Kabul"}
cities3=cities.issubset(cities2)
print(cities3)

# add()
# If you want to add a single items to the set use the add() method.
# For instance,
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.add("Helsink")
print(cities)

# update()
# If you want to add more than one item, simply create set or any other iterable object
# (list, tuple,dictionary), and use the update() method to add it into the existing set.
# For instance,
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Helsink","Warsaw","Seoul"}
cities.update(cities2)
print(cities)

# Remove()/discard()
# We can use remove() and discard() methods to remove items from list.
# For instance,
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities.remove("Tokyo")
print(cities)
# The main difference between remove and discard is that, if we try to delete an item
# which is not present in set, then remove() raises an error, whereas discard() does not raise any error.\
# For instance,
Name={"Arpita","Amar","Sushma","Sabana"}
Name.discard("Binisha")
# Name.remove("Binisha"): It will give you KeyError.
print(Name)

# pop()
# This method removes the last item of the set but the catch is that we don't know which
# Item gets popped as sets are unordered. However, you can access the popped item if you 
# assign the pop() method to a variable.
# For instance,
cities={"Tokyo","Madrid","Berlin","Delhi"}
item=cities.pop()
print(cities)
print(item)

# del()
del Name
# print(Name)

# clear
cities.clear()
print(cities)
