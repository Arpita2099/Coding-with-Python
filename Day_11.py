# In today coding of python I will do one real life example of if-else statements.

# Create a python program capable of greeting you with Goodmorning, Good Afternoon, and Good Evening.
# Your program should use time module to get the current hour.

import time
Current_hour=int(time.strftime("%H"))
if 5<=Current_hour<12:
    print("Good Morning Sir!!")
elif 12<=Current_hour<18:
    print("Good Afternoon Sir!!")
elif 18<=Current_hour<=12:
    print("Good Evening Sir!!")
else:
    print("Good Night Sir!!")

# Write a program to print the GMT-NPT using import time.
import time
a=int(time.time())
hours=(a//3600)%24
minn=(a//60)%60
#current_second=a%60
print(f"{hours:02}:{minn:02}")
if (hours+5)>23:
    Nepali_hour=(hours+5)%24
    if (minn+45)>59:
        Nepali_hour+=1
        Nepali_minn=(minn+45)%60
        print(f"{Nepali_hour:02}:{Nepali_minn:02}")
    else:
        Nepali_minn=minn+45
        print(f"{Nepali_hour:02}:{Nepali_minn:02}")
elif minn+45>59:
     Nepali_hour=hours+6
     Nepali_minn=(minn+45)%60
     print(f"{Nepali_hour:02}:{Nepali_minn:02}")
else:
    Nepali_hour=hours+5
    Nepali_minn=(minn+45)
    print(f"{Nepali_hour:02}:{Nepali_minn:02}")

# Military time -> Civilian time
t=int(input("Enter the time: "))
hour=t//100
minute=t%100
if hour>23:
    raise ValueError("Hour cannot be greater than 23.")
elif minute>59:
    raise ValueError("Minute cannot be greater than 59.")
else:
    if hour==12:
        print(f"{hour}:{minute} am")
    elif hour>12:
        print(f"{hour-12}:{minute} pm")
    else:
        print(f"{hour}:{minute} am")

# This is all about the today coding in Python.
