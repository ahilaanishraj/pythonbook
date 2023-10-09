'''
steps for file program

1. create/open a file
2. take input from that file/ write output to that file
3. close the file'''

print('\n\n create or open a file')
try:
    with open('d:/aaa/f1.txt', 'x') as file:
        pass  # Do nothing, just create the file
    print("File 'f1.txt' has been created successfully.")
except FileExistsError:
    print("File 'f1.txt' already exists. Cannot create a new one.")

print('\n\nwritting content to file')

# Open a file for writing 
with open('f1.txt', 'w') as file:
    # Write some text to the file
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Nanjil college of arts and science\n")
    
print('\n\nread and display content to file')

# Open a file for reading
with open('f1.txt', 'r') as file:
    # Read the entire contents of the file
    content = file.read()
    print(content)

print('\n\nadd more content to file')
# Open a file for appending (creates a new file if it doesn't exist)
with open('f1.txt', 'a') as file:
    # Append some text to the file
    file.write("This is appended text.\n")
    file.write("Department of computer science\n")


print('\n\nRead file content to file line by line')
# Open a file for reading
with open('f1.txt', 'r') as file:
    # Read and process each line one by one
    for line in file:
        print(line.strip())  # Strip removes the newline character

print('\n\ncopy f1 content to f2 file')

import shutil

source_file = 'f1.txt'
destination_file = 'f2.txt'

shutil.copy(source_file, destination_file)
print(f"{source_file} has been copied to {destination_file}.")

print('\n\ncheck whether the file is exist or not')
import os

file_path = 'f2.txt'

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")


print('\n\delete  file')

file_to_delete = 'f1.txt'

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"{file_to_delete} has been deleted.")
else:
    print(f"{file_to_delete} does not exist.")

print('\n\ncheck whether the file is exist or not')
import os

file_path = 'f1.txt'

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")

