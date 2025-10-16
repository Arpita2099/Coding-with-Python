# For loop with else in Python.
# Python else in Loop
# As you have learned before, the else clause is used along with if statement.
# Python allows rhe else keyword to be used with the for and while loop too.
# The else block appears after the body of the loop.
# The statements in the else block will be executed after all iterations are completed.
# The program exists the loop only after the else block is executed.
# For instance,
for i in range(5):
    print(i)
else:
    print("Unable to print i.")
print()

for i in range(5):
    print(i)
    if i==4:
        break
else:
    print("Unable to print i.")

print()
i=0
while i<7:
    print(i)
    i=i+1
else:
    print("Unable to print i.")

for x in range(5):
    print("Iteration no {} in for loop".format(x+1))
else:
    print("else block in loop.")
print("Out of Loop.")
