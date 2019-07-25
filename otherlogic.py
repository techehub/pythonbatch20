import math
import os

print (os.getcwd())
os.mkdir("test")


def sum ( list):
    total =0
    for x in list:
        total =total +x
    return total


def add (a,b):
    return a+b