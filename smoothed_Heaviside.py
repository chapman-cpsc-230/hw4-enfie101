"""
File: smoothed_Heaviside.py

Copyright (c) 2016 Callie Enfield

License: MIT

This code implements H_eps and tests it.
"""

from math import pi, sin
eps = 0.01

def H_eps(x,eps):
    if x < -eps:
    #Do case 1
        result = 0
    elif x <= eps:
    #Do case 2
        result = 0.5*((1+(x/eps))+sin(pi*(x/eps)))
    else:
    #Do case 3
        result = 1
    return result

def test_H_eps():
    if H_eps(-0.04,eps) != 0:
        print "Error"
    elif H_eps(-0.01,eps) != 0.5*((1+(-0.01/eps))+sin(pi*(-0.01/eps))):
        print "Error"
    elif H_eps(0,eps) != 0.5*((1+(0/eps))+sin(pi*(0/eps))):
        print "Error"
    elif H_eps(0.01,eps) != 1:
        print "Error"
    else:
        print "Everything is correct"

test_H_eps()
