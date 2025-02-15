import os

# Specify the directory (or use the current directory)
directory_path = "/SEM-1"

# List all files and folders in the directory
contents = os.listdir(directory_path)

# Print the contents
print("Contents of directory:", directory_path)
for item in contents:
    print(item)
