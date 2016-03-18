"""
File: histogram2.py

Copyright (c) 2016 Callie Enfield

License: MIT

This code will create another histogram, but this time with table lines and headings.
"""

n = [4, 9, 13, 5]

print "n   |  Data"
print "----+----------"

def bar(n):
    string = ""
    for i in range(n):
        string += "*"
    return string

for i in range(len(n)):
    print n[i], "  |  ", bar(n[i])
