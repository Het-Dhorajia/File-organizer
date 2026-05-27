import os

folder_path = input("Enter folder path: ")

files = os.listdir(folder_path)

for file in files:
    name, ext = os.path.splitext(file)

    ext = ext.lower()

    if ext in [".jpg", ".png", ".jpeg"]:
        print(file, "→ Image")

    elif ext in [".mp4", ".mkv", ".avi"]:
        print(file, "→ Video")

    elif ext in [".pdf", ".docx", ".txt"]:
        print(file, "→ Document")

    elif ext in [".zip", ".rar"]:
        print(file, "→ Archive")

    else:
        print(file, "→ Other")