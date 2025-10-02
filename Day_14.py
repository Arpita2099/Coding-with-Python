# In the day 14 of coding in Python, I am going to solve some of the problem related to foor loop.
# I am going to solve some problems to make my coding skills perfect in the Python.

# Print numbers from 1 to 50 using a for loop.
print("The number from 1 to 50 are: ")
for i in range(1,51):
    print(i, end=" ")
print()

# Print the square of each number from 1 to 10.
print("Square of number from 1 to 10.")
for i in range(1,11):
    print(i**2, end=" ")
print()

# Print the multiplication table of any number entered by the user.
num=int(input("Enter any number: "))
print(f"Multiplication of {num} is: ")
for i in range(1,11):
    print(num,"*",i,"=",num*i)
print()

# Print the first 10 odd numbers
print("The first 10 Odd numbers are: ")
for i in range(1,20,2):
    print(i)
print()

# Print the sum of numbers from 1 to 100 using a for loop.
sum=0
for i in range(1,101):
    sum=sum+i
print("Sum of the number from 1 t0 100 is: ", sum)

# Solve the following pattern:
# *
# **
# ***
# ****
# *****
print("Print the patter1.")
rows=5
for i in range(1, rows+1):
    print("*"*i)
print()

print("Printing the pattern here: ")
# *****
# ****
# ***
# ** 
# * 
rows=5
for i in range(rows,0,-1):
    print("*"*i)
print()

# Given a list=[10,20,30,40,50], print each element using a for loop.
list=[10,20,30,40,50]
for i in list:
    print(i)
print()

# Find the maximum number in a list without using max().
numbers=[10,20,30,40,50]
maximum=numbers[0]
for num in numbers:
    if num > maximum:
        maximum=num
print("Maximum Number is: ",maximum)
print()

# Count how many vowels are in a given string:
str=input("Enter the string: ")
vowels="arpiTaSah"
count=0
for ch in str:
    if ch in vowels:
        count+=1
print("Total number of Vowel is: ",count)

# Check if a number is prime using a for loop.
num=int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, num): 
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")
print()

# Write a program to print all prime numbers between 1 and 100.

# Write a program to find the factorial of a number using a for loop.

# Print the Fibonacci sequence up to n terms using a for loop.

# Reverse a string using a for loop (without using slicing).

# Real-Life Style Problems

# A shop has prices [120, 340, 560, 230, 90]. Print only the prices greater than 200.
# For solving this problem I am using the simple concept because upto now I am doing the code for for loop.
# But there is another methods of solving this problem by using the list function appends to have output in the form of list formats.
# Simply youu can see the easy way to solve this problem using for loop. 
prices=[120,340,560,230,90]
print("Thr price greater than 200 are: ")
for i in prices:
    if i>200:
        print(i)

# Print all the even numbers between 1 and 100, but skip numbers divisible by 10.
print("The even number between 1 to 100 and not divisible by 10 are: ")
for i in range(1,101):
    if i%2==0 and i%10!=0:
        print(i,end=" ")
