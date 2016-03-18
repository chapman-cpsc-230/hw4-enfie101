"""
File: count_pairs.py

Copyright (c) 2016 Callie Enfield

License: MIT

<brief description of the code>
"""

def count_v2(dna,base):
    i = 0
    for CT in dna:
        if CT == base:
            i += 1
        return dna.count(base)

dna = 'ACTGGATTCGATCT'
base = 'CT'
n = count_v2(dna,base)
print "%s is in %s %d times." % (base,dna,n)
