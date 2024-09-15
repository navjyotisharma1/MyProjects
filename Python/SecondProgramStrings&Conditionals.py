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
str = "I am studying python"
print(str.endswith("stu"))