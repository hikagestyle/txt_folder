import os

dir_name = "dir"

os.makedirs(dir_name, exist_ok=True)

with open('list.txt', 'r') as f:
    List = f.read().split("\n")

for i in List:
    os.makedirs(dir_name + '/' + i, exist_ok=True)

# python3 test_.py
