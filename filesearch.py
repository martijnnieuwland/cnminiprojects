import os
import glob

folder = input("Which directory do you want to search? ")

extensions = []
for f in glob.iglob(f"{folder}/**/*", recursive=True):
    filename, file_extension = os.path.splitext(f)
    if file_extension == ".jpg":
        print(f)
    if file_extension not in extensions:
        extensions.append(file_extension)
print(f"Types of file extensions in this folder are:\n{extensions}.")
