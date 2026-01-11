# Ai Auto Directory Creator

import os

folders =["data","model","scripts","notebook","output"]
project=input("Enter Ai project Name: ")

for folder in folders:
    path = os.path.join(project,folder)
    os.makedirs(path,exist_ok=True)
    print(f"created:{path}")
