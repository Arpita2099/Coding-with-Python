# List
# enclosed within a big bracket []
# Values or elements are seperated by comma.
# Other collection data types are dictionary, set, andd tuple.

# Lists are mutable and ordered.
# Mutable means non-resislient to changes.
# Ordered =Each elements of lists are index.

# How to initialize and declare a list.
L1=[1,2,3] # They are all in int data type.
L2= ['1',2,3.0,True]
print(L1[2]) # Indexing in the list using positive indexing.
print(L2[-2]) # Indexing in the list using negative indexing.
# Both are list
# What's the difference
# L1 is an array but L2 is not an array.
# Even though both of them are list.

# Append function on list: Used to add the last element in the list.
L1.append(4)
print(L1)

# insert function on list: Used to add new item into the list and it will not add more than two argument.
L1.insert(5,6)
print(L1)

# Iterates through value # For Loop # For collection data_type.
# Iterates through index # For Loop # Foe collecting data_type.
# Range function is used to provide the upper, lower and increasing value in the for loop to get the required output.
for i in range(1,11):
    print(i)

# Range function syntax # range(start=0,stop,step=1)
# If you do not pass the inital or stat value than it will get started from 0.
for i in range(6):
    print(i)

# Also if you do not give the value of step than it will autometically increase each by step one in default.
# But ending or upper range is required other wise loop will run infinite loop.
for i in range (20,5,-5):
    print(i,end=' ')

# How to apply for loop collection data_types.
L=[1,2,3,4,5,6,7,8,9]
for i in L: # This is called iterate through value.
    print(i,end=' ')

for i in range(len(L)):
    print(i, end=' ')

# Factorial of a number using while loop.
n=10
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(f"Factorial of {n} is: {fact}")

# Write a program to print the factorial using for loop.
fact=1
n=6
for i  in range(1,n+1):
    fact=fact*i
print(f"Factorial of {n} is {fact}.")

# Find the number divisible by both 7 or 9 upto 1000
n=1000
for i in range(1,n+1):
    if i%7==0 or i%9==0:
        print(i,end=' ')

n=60
sum_even=0
sum_odd=0
for i in range(1,n+1):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print("Sum of even number is: ",sum_even)
print("Sum of Odd number is: ",sum_odd)        
