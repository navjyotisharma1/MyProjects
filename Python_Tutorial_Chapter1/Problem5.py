#Label the program written in problem 4 with comments.
# Import the os module, which contains methods for interacting with the operating system
import os

# Specify the directory whose contents you want to list.
# Here, '.' refers to the current working directory. You can change it to any valid directory path.
directory_path = '/'  # You can change this to any directory path

# Use os.listdir() to get a list of entries in the specified directory.
# This returns a list of file and folder names (not including '.' and '..')
contents = os.listdir(directory_path)

# Print the contents of the directory.
print(contents)
