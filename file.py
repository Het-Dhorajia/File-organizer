import os

folder_path = input("Enter folder path: ")

files = os.listdir(folder_path)

print("\nFiles found:\n")

for file in files:
    print(file)