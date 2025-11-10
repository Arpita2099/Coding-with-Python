# Python provides several ways to manipulate files. Today, we will discuss how to handle files in Python.

# Opening a File
# Before we can perform any operations on a file, we must first open it. Python provides the
# opens() function to open a file.It takes two arguments: the name of the file and the mode in which the 
# file should be opened. The mode can be 'r' for opening.

# Here is an example of how to open a file for reading:
f=open('myfile.txt','r')

# By default, the open() function returns a file object that can be used to read from or write 
# to the file, depending on the mode.

# Modes in file

# There are various modes in which we caan open files.
# 1. read(r): This mode opens the file for reading only and gives an error if the file does not exist.
# Thnis is the default mode if no mode is passed as a parameter.

# 2. write(w): This mode opens the file for writing only and creates a new file if the file does not exist.

# 3. append(a): This mode opens the file for appending only and creates a new file if the file does not exist.
