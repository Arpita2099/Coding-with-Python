import module1 as m1 # Here it will import the model1 and store as m1.
import module2 as m2 # Here it will import the model2 and store as m2.

print("Print the factorial and Fibonacci of given number.")

num = int(input("Enter any number: ")) # Here it will ask for user enter any integer.

# Factorial of the given number.
fact = m1.factorial(num) # It will extract the module1 function code.
print(f"\nFactorial of {num} is: {fact}") # Here it will print the factorial of number.

# Fibonacci of the given number.
fib = m2.fibonacci(num) # It will extract the module2 function code.
print(f"Fibonacci series up to {num} terms is: {fib}") # Here it will print the fabonacci of number.
