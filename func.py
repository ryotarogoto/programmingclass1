'''
Created on 2013/06/11

@author: dmn1003
'''
from MyCsv import readMyCsv, writeMyCsv
from Search import BMMethod

def getAnumber(DNA):
    return DNA.count('A')
    
def funcDNA2(DNA):
    nA = DNA.count('A')
    nT = DNA.count('T') * 0.8
    nC = DNA.count('C') * 0.6
    nG = DNA.count('G') * 0.4
    
    return nA + nT + nC + nG
    
def funcDNA(DNA):
    e1DNA = ['A', 'T', 'T']
    e2DNA = ['C', 'C', 'G']
    e3DNA = ['C', 'G', 'C']
    e4DNA = ['A', 'T', 'A']
    e5DNA = ['G', 'T', 'T']


    ans1DNA = BMMethod(DNA, e1DNA)[0]
    ans2DNA = BMMethod(DNA, e2DNA)[0]
    ans3DNA = BMMethod(DNA, e3DNA)[0]
    ans4DNA = BMMethod(DNA, e4DNA)[0]
    ans5DNA = BMMethod(DNA, e5DNA)[0]

    return len(ans1DNA) * 10 + len(ans2DNA) * 7 + len(ans3DNA) * 5 + len(ans4DNA) * 3 + len(ans5DNA)
    
    
    
if __name__ == "__main__":
    preDNA = readMyCsv()
    tDNA = [i.pop() for i in preDNA]
    print tDNA
    
    print getAnumber(tDNA)
    print funcDNA2(tDNA)
    print funcDNA(tDNA)