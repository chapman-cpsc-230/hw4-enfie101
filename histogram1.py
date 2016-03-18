"""
File: histogram1.py

Copyright (c) 2016 Callie Enfield

License: MIT

This code will produce a histogram made of asterisks given the values in the original list.
"""

ls = [4, 9, 13, 5]

def bar(number):
    string = ""
    for i in range (number):
        string += "*"
    return string

for i in range(len(ls)):
    print bar(ls[i])

print ls
