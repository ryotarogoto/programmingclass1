'''
Created on 2013/07/02

@author: dmn1003
'''


import random
from func import *
from MakeDNA import SimpleDNA

#const
ary = ['A', 'T', 'C', 'G']

#randomwalk
def resultofrandomwalk(eDNA, step):
    evalvaluelist = list()
    for i in range(step):
        tmpDNA = eDNA[:]
        tmpval = funcDNA2(eDNA)
        eDNA[random.randint(0, 3)] = ary[random.randint(0, 3)]
        if tmpval > funcDNA2(eDNA):
            eDNA = tmpDNA[:]
        evalvaluelist.append(funcDNA2(eDNA))
        
    return evalvaluelist

memo = list()
def localsearch(eDNA):
    ary = ['A', 'T', 'C', 'G']
    tmpval = funcDNA2(eDNA)
    for i in range(len(eDNA)):
        for ele in ary:
            if eDNA[i] != ele:
                eDNA[i] = ele
                if tmpval < funcDNA2(eDNA):
                    return eDNA
            

#randomwalk_localsearch
def resultofrandompluslocal(eDNA, step):
    evalvaluelist = list()
    for i in range(step):
        tmpDNA = eDNA[:]
        tmpval = funcDNA2(eDNA)
        eDNA[random.randint(0, 3)] = ary[random.randint(0, 3)]
        if tmpval > funcDNA2(eDNA):
            eDNA = tmpDNA[:]
        newDNA = localsearch(eDNA)
        
        eDNA = newDNA
        evalvaluelist.append(funcDNA2(eDNA))
        
    return evalvaluelist
    
    
    
if __name__ == "__main__":
    step = 100
    num_dna = 50
    evalDNA = SimpleDNA(num_dna).getDNA()
    ans1 = list()
    ans2 = list()
    
    for i in range(101):
        ans1.append(resultofrandomwalk(evalDNA, step))
        
    print "randomwalk"
    print ans1[50]
    
    for i in range(101):
        ans2.append(resultofrandompluslocal(evalDNA, step))
        
    print "random+localsearch"
    print ans2[50]
        


