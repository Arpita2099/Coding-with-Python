# In the Day_16 of python coding, I am going to solve some of the problem related to while loop.
# By solving the some of the problem related to while loop, it help me to practice the while loop indetails and be good on making logic by using the while loop:
# Here are some of the questions:

# Print numbers from 1 to 10 using a while loop.
i=1
while i<=10:
    print(i)
    i+=1
print()
# Print the first 10 even numbers.
i=2
count=1
while count<=10:
    print(i)
    i+=2
    count=count+1
print()
# Print the multiplication table of a number entered by the user.
num=int(input("Enter any number: "))
i=1
while i<=10:
    print(f"{num} * {i} ={num*i}")
    i=i+1
print()
# Find the sum of numbers from 1 to n using a while loop.
Num=int(input("Enter any number: "))
i=1
total=0
while i<=Num:
    total=total+i
    i+=1
print("Sum of n number is: ",total)

# Reverse the digits of a given number (e.g., 123 → 321).
num=int(input("Enter a number: "))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print("Reversed number is: ", rev)
print()

# Keep asking the user for numbers until they enter 0, then print the sum of all numbers entered.
total=0
while True:
    num=int(input("Enter number from 0 to stop: "))
    if num==0:
        break
    total=total+num
print("Sum of all number entered is: ",total)
print()
# Write a program that keeps asking for a password until the correct one is entered.
c_password='1234'
while True:
    password=(input("Enter password: "))
    if password==c_password:
        print("Your password is correct.")
        break
    else:
        print("Your password is wrong, try again.")
print()
# Count how many digits are in a given number using a while loop.
num=int(input("Enter any digit of number: "))
count=0
while num>0:
    num//=10
    count=count+1
print("Number of digits: ",count)
print()
# Find the factorial of a number using a while loop.
num=int(input("Enter a number: "))
fact=1
while i<=num:
    fact=fact*i
    i+=1
print(f"Factoril of {num} is {fact}")
print()

# Check whether a given number is a palindrome (same forward and backward, e.g., 121).
num=int(input("Enter any number: "))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
    if rev==num:
        print(f"{num} is Palindrome.")
    else:
        print(f"{num} is not Palindrome.")
print()
# Print numbers from 1 to 20 but skip multiples of 3 (continue usage).
i = 1
while i <= 20:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1
print()
# Keep asking the user for input until they type "exit".
while True:
    text = input("Enter something ('exit' to stop): ")
    if text.lower() == "exit":
        break
    print("You typed:", text)
print()
# Use a while loop to simulate a simple ATM pin check: allow only 3 attempts, then break.
correct_pin = "4321"
attempts = 0
while attempts < 3:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("PIN accepted. Welcome!")
        break
    else:
        print("Incorrect PIN.")
        attempts += 1
if attempts == 3:
    print("Too many attempts. Card blocked.")
print()
# Write a number guessing game: keep asking until the user guesses the correct number, then break.
secret = 7
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong! Try again.")
print()
# Print all prime numbers less than n using a while loop.
n = int(input("Enter n: "))
num = 2
while num < n:
    i = 2
    is_prime = True
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num)
    num += 1
print()
# Keep dividing a number by 2 until it becomes less than 1, and count the steps.
num = float(input("Enter number: "))
steps = 0
while num >= 1:
    num /= 2
    steps += 1
print("Total divisions:", steps)
print()
# Simulate a menu-driven program (like calculator options: add, subtract, exit).
while True:
    print("\nMenu:\n1. Add\n2. Subtract\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        a = int(input("Enter first: "))
        b = int(input("Enter second: "))
        print("Result =", a + b)
    elif choice == "2":
        a = int(input("Enter first: "))
        b = int(input("Enter second: "))
        print("Result =", a - b)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
print()
# Use while loop to find the greatest common divisor (GCD) of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    a, b = b, a % b
print("GCD =", a)
print()
# Generate the Fibonacci sequence up to n terms using a while loop.
n = int(input("Enter any term of number: "))
a, b = 0, 1
count = 0
while count < n:
    print(a)
    a, b = b, a + b
    count += 1
