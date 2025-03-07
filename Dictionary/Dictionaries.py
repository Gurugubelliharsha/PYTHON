# 1. Create a dictionary with at least 5 key-value pairs of Student ID and Name
students = {101: "Alice", 102: "Bob", 103: "Charlie", 104: "David", 105: "Eve"}
print(students)

# 1.1 Adding values in dictionary
students[106] = "Frank"
print(students)

# 1.2 Updating values in dictionary
students[102] = "Ben"
print(students)

# 1.3 Accessing a value in dictionary
print(students[103])

# 1.4 Create a nested dictionary
student_details = {
    101: {"name": "Alice", "age": 20},
    102: {"name": "Bob", "age": 21},
    103: {"name": "Charlie", "age": 22}
}
print(student_details)

# 1.5 Access the values of a nested dictionary
print(student_details[102]["name"])

# 1.6 Print the keys present in a dictionary
print(students.keys())

# 1.7 Delete a value from a dictionary
del students[104]
print(students)