"""
File: histogram2.py

Copyright (c) 2016 Callie Enfield

License: MIT

<brief description of the code>
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
