"""Variables
A variable is a name given to a memory location in a program.
"""
name = "Navjyoti Sharma"
age = 29
price = 25.58
print("my name is : ", name)
print("my age is :", age)
print("price of tomato is :", price)


"""Data Types
Integer(12,-12,0), String("Good Morning"), Float(1.48,4.98), Boolean(True,False), None
"""
OrderNo = 45
CustomerName = "Cloths count"
price = 45.78

print(OrderNo)
print(CustomerName)
print(price)
print(type(OrderNo))
print(type(CustomerName))
print(type(price))

"""Keywords
Keywords are reserved words in python.e.g, and,as,assert,break,class,continue,def,del,elif,else,except,finally,False etc.
"""
"""Print Sum"""
a = 45
b = 89
sum = a + b
diff = a - b
print(sum)
print(diff)

"""comments in python
1. Sinle line Comment.
2. Multi Line Comment."""
# Single Line Comment.
"""
Multi 
Line
Comment 
"""

"""Types of Operators
An operator is a symbol that performs a certain operation between operands"""

#arithmetic operators (+,-,/,%,**)
a = 4
b = 2
print(a+b)
print(a-b)
print(a/b)
print(a%b) #remainder
print(a**b) #power oerator a^b

#relational operators (==, !=, <, >, <=, >=)
a = 3
b = 2
print(a==b) #False
print(a!=b) #True
print(a<b) #False
print(a>b) #True
print(a<=b) #False
print(a>=b) #True

#assignment operators (=, +=, -=, /=, %=, **= )
# Using the assignment operator '='
num = 5
print("After '=' operator, num:", num)

# Using the addition assignment operator '+='
num += 5
print("After '+=' operator, num:", num)

# Using the subtraction assignment operator '-='
num -= 2
print("After '-=' operator, num:", num)

# Using the division assignment operator '/='
num /= 4
print("After '/=' operator, num:", num)

# Using the modulus assignment operator '%='
num %= 3
print("After '%=' operator, num:", num)

# Using the exponentiation assignment operator '**='
num **= 4
print("After '**=' operator, num:", num)

#logical operators ( not, and, or)
a = 50
b = 30
print(not False)
print(not (a>b))
val1 = False
val2 = True
print("AND operator:", val1 and val2)
print("OR OPERATOR:", (a==b) or (a>b))

#Type conversion (Automatically, casting)
a = int("2") #Type casting from "string" to "int"
b = 4.25
print(a + b)
b = str(b) 
print(type(b))

#inputes in python
name = input("enter your name: ")
age = input("enter your age: ")
marks = input("enter your marks: ")
print("Welcome", name)
print("age = ", age)
print("marks = ", marks)

"""Practice 
Write a program to input 2 numbers & print their sum."""

first = int(input("enter first: "))
second = int(input("enter second: "))
sum = first + second
print("sum =", first + second)

#WAP to input side of a square & print its area.
side = float(input("enter  square side : "))
print("area =", side ** 2)

#WAP to input 2 floating point numbers & print their average.
a = float(input("enter first: "))
b = float(input("enter second: "))
print("avg =", (a+b)/2)