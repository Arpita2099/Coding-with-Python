# In the Day_10 of coding with python,
# I am going to solve some of the program related to if-else..... statements.
# In this coding I am going to solve some of the question that make me to use my own login and be more practice in solving problem rather than learning only.

# Here are some of the Questions with their solution.

# Write a program that checks if a number entered by user is positive.
# In this problem I am going to use only if statement to solve this problem.
# To take input from user I will use input() function and int() function because I want to take interger number as a input..
num=int(input("Enter a integer: "))
if num >0:
    print(f"{num} is Positive Number.")


# Write a program that check if a number is evem or odd.
# In this program I will use if-else statement because there are two condition even and odd.
# So, the given number will take from user.
Number=int(input("Enter any Number: "))
if Number % 2 ==0:
    print(f"{Number} is an Even Number.")
else:
    print(f"{Number} is an Odd Number.")

# Check whether a person is eligible to vote (age>=18)
Age=int(input("Enter any age: "))
if Age>=18:
    print(f"The person with this {Age} is eligible to vote.")
else:
     print(f"The person with this {Age} is not eligible to vote.")

# Write a program to check if a given year is a leap year. 
Year=int(input("Enter any year: "))
if (Year%4==0) or (Year%100!=0) and (Year%400==0):
    print(f"{Year} is a Leap Year.")
else:
    print(f"{Year} is not a leap year.")

# Write a program to check if a given character is a vowel or constant.
character=input("Enter any character: ")
if character.isalpha():
    if character.lower() in ['a','e','i','o','u'] and character.upper() in ['A','E','I','O','U']:
        print(f"{character} is a vowel letter.")
    else:
        print(f"{character} is a consonant letter.")
else:
    print("Not a character.")

# Write a program that assigns grade based on marks.
Marks=int(input("Enter Your Marks Here: "))
if Marks>90:
    print("Congratulation You Scored Grade A.")
elif Marks>80 and Marks<90:
    print("Congratulation You Scored Grade B.")
elif Marks>70 and Marks<80:
    print("Congratulation You Scored Grade C.")
elif Marks>60 and Marks<70:
    print("Congratulation You Scored Grade D.")
else:
    print("You are Failed.")

# Take input of temperature and print.
Temper=int(input("Enter the degree of temperature: "))
if Temper>30:
    print("Hot")
elif Temper>20 and Temper<30:
    print("Warm")
elif Temper>10 and Temper<20:
    print("Cold")
else:
    print("Freezing")

# Write a program to display the day of the week based on numbers(1= Monday....7=Sunday.)
Day=int(input("Enter the number 1-7: "))
if Day==1:
    print("Monday")
elif Day==2:
    print("Tuesday")
elif Day==3:
    print("Wednesday")
elif Day==4:
    print("Thrusday")
elif Day==5:
    print("Friday")
elif Day==6:
    print("Saturday")
else:
    print("Sunday")

# Write a program that checks whether a number is Positive, Negative, or Zero.
Num=int(input("Enter an integer: "))
if Num>0:
    print(f"{Num} is a Positive Number.")
elif Num<0:
    print(f"{Num} is a Negative Number.")
else:
    print(f"{Num} is Zero.")

# Take input of Age and Print.
# 0-12-->"Child"
# 13-19-->"Teen"
# 20-59-->"Adult"
# 60+-->"Senior"
age=int(input("Enter your age: "))
if age>0 and age<12:
    print("You are Child")
elif age>13:
    print("You are Teen")
elif age>20 and age<59:
    print("You are Adult.")
else:
    print("You are senior.")

# Write a program to check if a number is divisible by 2 and also by 5.
num1=int(input("Enter any number: "))
if num1%2==0:
    if num1%5==0:
        print(f"{num1} is divisible by both 2 and 5.")
    else:
        print(f"{num1} is divisible by 2 not 5.")
else:
    if num1%5==0:
        print(f"{num1} is divisible by 5 but not 2.")
    else:
        print(f"{num1} is not divisible by both.")

# Login Program and indentation.
# In this login page the email id:arpitasah750@gmail.com along with password=12345 than it will print the command Welcome else it will print your email and password is wrong.
email=input("Enter your email password: ")
password=input("Enter your password: ")
if email=='arpitasah750@gmail.com' and password=='12345':
  print("Thank you for login, and Welcome")
elif email=='arpitasah750@gmail.com' and password!='12345':
  print("Your password is incorrect.")
  password=input('Enter your password:')
  if password=='12345':
    print("Your password is right, Welcome!")
  else:
    print("Your password is wrong Again!")
else:
  print("Your email and password is wrong.")

# This is all about today Coding in the Python.

    
