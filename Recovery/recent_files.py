import os

recent_dir = ''
with os.scandir (recent_dir) as files:
    files = [file.name for file in files if files.is_file ()]

print (files)
    