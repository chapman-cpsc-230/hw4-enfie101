"""
File: Heaviside.py

Copyright (c) 2016 Callie Enfield

License: MIT

This code implements function H(x) and tests it.
"""

from math import pi,sin

def H(x):
    if x < 0:
        result = 0
    if x >= 0:
        result = 1
    return result

def test_H():
    if H_eps(-10) != 0:
        print "Error"
    elif H_eps(-10**-15) != 0:
        print "Error"
    elif H_eps(0) != 0:
        print "Error"
    elif H_eps(10**-15) != 0:
        print "Error"
    elif H_eps(10) != 1:
        print "Error"

print "Everything is correct"
