# Write a python program to print the contents of a directory using the os module.Search online for the function which does that.
import os

# Specify the directory you want to list (use '.' for current directory)
directory_path = '.'

# Get the list of files and directories
contents = os.listdir(r'C:\Users\sharm\OneDrive\Desktop\GitDemo\MyProjects\Python_Tutorial_Chapter1'
)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)
