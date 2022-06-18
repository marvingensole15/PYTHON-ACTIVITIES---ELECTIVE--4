
f = open("pythonessay.txt", "r")
print(f.read())

f = open("pythonessay.txt", "r")
print(f.readline())

f = open("pythonessay.txt", "r")
for x in f:
    print(x)

import os
if os.path.exists("pythonessay.txt"):
    os.remove("pythonessay.txt")
else:
    print("The file does not exist")

import os
if os.path.exists("pythonessay.txt"):
    os.remove("pythonessay.txt")
else:
    print("The file does not exist")