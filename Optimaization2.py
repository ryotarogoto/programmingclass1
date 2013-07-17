#!/usr/bin/env python

from func import funcDNA2
from MakeDNA import SimpleDNA
from random import randint
from MyCsv import readMyCsv, writeMyCsv
import csv

def RandomWalk(step):
    chompvalue = 0
    hamming = 3
    valuelist = list()
    ary = ['A', 'T', 'C', 'G']
    for i in range(step):
        eDNA = SimpleDNA(randint(0, 50)).getDNA()
        value = funcDNA2(eDNA)
        if value > chompvalue:
            chompDNA = eDNA[:]
            chompvalue = value
            for i in range(hamming):
                eDNA = SimpleDNA(len(eDNA)).getDNA()
                value = funcDNA2(eDNA)
                if value > chompvalue:
                    chompDNA = eDNA[:]
                    chompvalue = value
        valuelist.append(chompvalue)
    return [chompDNA, chompvalue, valuelist]

def RandomLocal(step):
    chompvalue = 0
    hamming = 3
    local = 3
    valuelist = list()
    ary = ['A', 'T', 'C', 'G']
    for i in range(step):
        eDNA = SimpleDNA(randint(0, 50)).getDNA()
        value = funcDNA2(eDNA)
        if value > chompvalue:
            chompDNA = eDNA[:]
            chompvalue = value
            N = len(eDNA)
            for i in range(hamming):
                eDNA = SimpleDNA(len(eDNA)).getDNA()
                value = funcDNA2(eDNA)
                if value > chompvalue:
                    chompDNA = eDNA[:]
                    chompvalue = value
                    
                    for i in range(local):
                        index = randint(0, N - 1)
                        for ele in ary:
                            eDNA[index] = ele
                            value = funcDNA2(eDNA)
                            if value > chompvalue:
                                chompDNA = eDNA[:]
                                chompvalue = value
        valuelist.append(chompvalue)
            
    return [chompDNA, chompvalue,valuelist]

if __name__ == "__main__":
    for i in range(101):
        step = 1000
        print "-----------------"
        
        ans = RandomLocal(step)
        print "-----------------"
        if i == 50:
            print len(ans[2])
            filename = "randomlocal.csv"
            writecsv = csv.writer(file(filename, 'w'), lineterminator='\n')
            ar1 = ans[2]
            for ele in ar1:
                writecsv.writerow([ele])
            
            
        print "-----------------"
        ans2 = RandomWalk(step)
        print "-----------------"
        if i == 50:
            print len(ans2[2])
            filename = "randomwalk.csv"
            writecsv2 = csv.writer(file(filename, 'w'), lineterminator='\n')
            ar2 = ans2[2]
            for ele in ar2:
                writecsv2.writerow([ele])

    
