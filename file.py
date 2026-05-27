import os

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("Invalid folder path")
    exit()

file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".rar"]
}

stats = {
    "Images": 0,
    "Videos": 0,
    "Documents": 0,
    "Archives": 0,
    "Others": 0
}

files = os.listdir(folder_path)

for file in files:
    full_path = os.path.join(folder_path, file)

    if os.path.isdir(full_path):
        continue

    _, ext = os.path.splitext(file)
    ext = ext.lower()

    found = False

    for category, extensions in file_types.items():
        if ext in extensions:
            stats[category] += 1
            found = True
            break

    if not found:
        stats["Others"] += 1

print("\nFile Statistics:\n")

for category, count in stats.items():
    print(category, ":", count)