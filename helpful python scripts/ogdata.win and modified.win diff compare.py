#Credits to Eldoofus
import os
import hashlib

p1 = input("Enter the path of the original directory: ")
p2 = input("Enter the path of the new directory: ")

f1 = os.listdir(p1)
f2 = os.listdir(p2)

for i in f1:
    if i in f2:
        o = open(p1 + "/" + i, "rb").read()
        n = open(p2 + "/" + i, "rb").read()
        if hashlib.sha256(o).hexdigest() == hashlib.sha256(n).hexdigest():
            os.remove(p2 + "/" + i)