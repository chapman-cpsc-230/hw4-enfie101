"""
File: digits.py

Copyright (c) 2016 Callie Enfield

License: MIT

This code will tell how many digits are in a given number, including negative signs.
"""

def digits(n):
    #wrong for n <= 0
    #cnt = 0
    #while n > 0:
    #    n /= 10
    #    cnt += 1
    #return cnt
    return len(str(n))
print digits (-4530)
