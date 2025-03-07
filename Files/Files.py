import os

# 1. Read a text file
with open("rf.txt", "r") as file:
    print("File Content:\n", file.read())

# 2. Write text to a .txt file
with open("wf.txt", "w") as file:
    file.write("Hello, this is a test file.")

# 3. Read a file stream
with open("wf.txt", "r") as file:
    print("\nReading file:")
    print(file.read())

# 4. Read a file stream with random access
with open("wf.txt", "r") as file:
    file.seek(6) 
    print("\nReading from 6th character:", file.read())

# 5. Read a file from a particular index using seek()
with open("wf.txt", "r") as file:
    file.seek(3)  
    print("\nReading next 5 characters:", file.read(5))

# 6. Check if file has read and write access
file_path = "wf.txt"
print("\nChecking file permissions:")
print("Read Access:", os.access(file_path, os.R_OK))
print("Write Access:", os.access(file_path, os.W_OK))