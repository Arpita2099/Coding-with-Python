# Opening file in Python
f=open("myfile.txt",'r')
print(f)\

# Reading Mode in Python
text=f.read()
print(text)
f.close()

# Writing to a file
f=open("myfile.txt",'w')
f.write("Hello everyone, I am here to learn coding.")

# Append in a file
f=open("myfile.txt",'a')
f.write("\t Hello Everyone!!")
f.close()

with open('myfile.txt','a') as f:
    f.write("\n Hey dude, I am inside the with.")

