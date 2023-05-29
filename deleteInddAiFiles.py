import os

dir_name = "path to folders"
allFiles = os.listdir(dir_name)

for file in allFiles:
    if file.endswith(".indd") or file.endswith(".ai"):
        os.remove(os.path.join(dir_name, file))