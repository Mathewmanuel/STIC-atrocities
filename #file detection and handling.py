#file detection and handling
import os#helps interact with files
#relative filepath
filepath="test2.txt"
if os.path.exists(filepath):
    print(f"this file at {filepath} exists")
else:
    print("that location exists")

import os#helps interact with files
#absolute filepath
filepath="C:/Users/Dell/OneDrive/Documents/SITC internship/test.tx"
if os.path.exists(filepath):
    print(f"this file at {filepath} exists")
    if os.path.isfile(filepath):
        print("is a  file")
else:
    print("that location exists")
