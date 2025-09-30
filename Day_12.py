# In the Day 12 of Coding in Python, I am goin to write code for match case statement in Python.
# Here, is the code.
# Match in Python-> Switch
a=int(input(" Enter 1 to add two numbers.\n Enter 2 to substract two number.\n Enter 3 to find square of number.\n"))
match a:
    case 1:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print(f"Sum of two number: {a+b}")
    case 2:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print(f"Substraction of two number: {a-b}")
    case 3:
        a=int(input("Enter the number: "))
        print(f"Square of a number: {a**2}")
    case _:
        print("Invalid Input.")

x=int(input("Enter the value of X: "))
match x:
    case 0:
        print("X is Zero.")
    case 4:
        print("Case is 4")
    case _:
        print(x)
                
