#Strings - String is a data type that stores a sequence of characters.
str1 = "This is a string.\nWe are creating it in python. \tIt is easy to understand." #By using escape sequence(\n), tab(\t)
print(str1)

#Basic Operations (Concatenation, Length of str)
str2 = "Navjyoti"
str3 = "Sharma"
final_str = str2 + " " + str3 #concatenation
print(final_str)

len1 = len(str1) #length of string
print(len1)

len2 = len(str2) #length of string
print(len2)

len3 = len(str3) #length of string
print(len3)

print(len(final_str))

# indexing - (Position)
str = "Navjyoti Sharma"
ch = str[0]
print(str[8])

# slicing - Accessing parts of a string
#str[ starting_idx : ending_idx ] (ending idx is not included)
str = "Navjyoti Sharma"
print(str[1:7])
print(str[:12])
print(str[-6:-1]) #negative index (-3,-2,-1)

# String functions
str = "i am studying python"
print(str.endswith("stu")) #returns true if string ends with substr (endswith("stu"))
print(str.capitalize()) #capitalizes 1st char
print(str)
print(str.replace("i", "A")) #replaces all occurences of old
print(str.find("am")) #returns 1st index of 1st occurrer
print(str.count("python")) #counts the occurence of substr


#Practice question
#WAP to input user's first name & print its length.
name = input("Enter your name :")
print("length of your name is", len(name))

#WAP to find the occurrence of '$' in a string.
str = "my name is nav$jyoti Sharma $$$$"
print(str.count("$"))


#Conditional Statements (Syntax - if-elif-else)
light = "blue"
if(light == "red"):
    print("stop")     #Indentation
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

print("End of code")


#Practice Question on Conditional Statements 
#Grade students based on marks
marks = int(input("enter student marks : "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "c"
else:
    grade = "D"
print("grade of the student ->", grade)


#WAP to check if a number entered by the user is odd or even.
num = int(input("Enter Number: "))
rem = num % 2
if(rem == 0):
    print("Even")
else:
    print("odd")


#WAP to find the greatest of 4 numbers entered by the user.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter forth Number: "))
if(a>=b and a>=c and a>=d):
    print("First number is the largest", a)
elif(b>=c and b>=d and b>=a):
    print("Second number is the greatest", b)
elif(c>=b and c>=d and c>=a):
    print("Third number is the greatest", b)
else:
    print("Forth is largest", d)


#WAP to check if a number is a multiple of 7 or not.
x = int(input("Enter a number: "))
if(x % 7 == 0):
    print(x , "is multiple of 7.")
else:
    print(x , "is not a multiple of 7.")

