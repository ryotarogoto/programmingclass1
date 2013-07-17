#!/usr/bin/env python

import random
import func
from MakeDNA import SimpleDNA

ary = ['A', 'T', 'C', 'G']
def checkDNA(aDNA, bDNA):
    hamming = 0
    n1 = len(aDNA)
    for i in range(n1):
        if aDNA[i] == bDNA[i]:
            hamming += 1
    return hamming

num_dna = 4
baseDNA = SimpleDNA(num_dna).getDNA()
evalDNA = SimpleDNA(num_dna).getDNA()

print "first---"
print "baseDNA:",
print baseDNA
print "evalDNA:",
print evalDNA

hamm = checkDNA(baseDNA, evalDNA)
print "first value of evaluation: %d" % hamm

while hamm < num_dna:
    tmpDNA = evalDNA[:]
    for i in range(num_dna - hamm):
        evalDNA[random.randint(0, (num_dna - 1))] = ary[random.randint(0, 3)]
    tmphamm = checkDNA(baseDNA, evalDNA)
    if hamm > tmphamm:
        evalDNA = tmpDNA
    else:
        hamm = tmphamm
    print hamm
print baseDNA
print evalDNA
    
    
    


