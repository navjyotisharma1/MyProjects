#Lists in Python - A built-in data type that stores set of values. It can store elements of different types (int, float, string, etc.)

marks =[87, 67, 78, 94.5, 87.9, 79.26]
student = ["Karan", 85, "Delhi", 98.5] 
student[1] = "Arjun"   #Change is allowed in python[List]
print(student)
print(len(student))
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[2])
print(marks[:4])

#List Slicing - Similar to String Slicing ----- list_name[starting_idx : ending_idx] #ending index is not included
marks = [87, 64, 65, 95, 78] #marks[1:4] is [64, 65, 95]
print(len(marks))  # 5
print(marks[-3: -1]) #is [65, 95] (We can also do indexing on the behalf of -ve indexing)

#List Methods
list = [2, 1, 3]
list.append(4) #adds one element at the end (Mutation [2, 1, 3, 4])
list.sort() #sorts in ascending order [1,2,3]
list.sort(reverse=True) #sorts in descending order[3, 2, 1]
list.reverse() #reverse list [3, 1, 2]
list.index(idx, el) #insert element at index


