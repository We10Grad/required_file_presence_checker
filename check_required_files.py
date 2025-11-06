import os
import shutil

required_files = ["README.md", ".gitignore"]


for filename in required_files:
    if not os.path.isfile(filename):
        print("Missing Files")
        exit(1)