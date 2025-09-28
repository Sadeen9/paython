import os

if os.path.exists("grades.txt"):
    with open("grades.txt","r") as f:
        data = f.read()
        print(data)
else:
    print("grades.txt not found -- starting fresh")
