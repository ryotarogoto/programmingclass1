'''
Created on 2013/07/09

@author: dmn1003
'''

'''
capacity of knapsack is 25000.
greedy algorithm.
'''

import MyCsv
import random

def evaltotalsize(data, genes):
    index = 0
    totalsize = 0
    for gene in genes:
        if gene == 1:
            totalsize += int(data[index][0])
        else:
            continue
        index += 1
    return totalsize

def evaltotalvalue(data, genes):
    index = 0
    totalvalue = 0
    for gene in genes:
        if gene == 1:
            totalvalue += int(data[index][1])
        else:
            continue
        index += 1
    return totalvalue

def mutate(genes, nummutation):
    newgenes = genes[:]
    for i in range(nummutation):
        index = random.randint(0, len(genes))
        if newgenes[index] == 1:
            newgenes[index] = 0
        else:
            newgenes[index] = 1
    return newgenes

def popup(genes, nummutation):
    newgenes = genes[:]
    for i in range(nummutation):
        index = random.randint(0, len(genes)-1)
        if newgenes[index] == 1:
            newgenes[index] = 0
        else:
            continue
    return newgenes
    


capa = 25000
nummutation = 4
step = 100
data = MyCsv.readMyCsv()
newdata = [data[i] for i in range(0, 202, 2)]
maindata = newdata[1:]
genes = [random.randint(0,1) for i in range(len(maindata))]

#print gene
#print maindata

#first evalation
totalsize = evaltotalsize(maindata, genes)
print 'first evalation of totalsize:'
print totalsize
while totalsize > capa:
    newgenes = popup(genes, nummutation)
    totalsize = evaltotalsize(maindata, newgenes)
    genes = newgenes[:]
    print '-----------'
    print totalsize
 

totalvalue = evaltotalvalue(maindata,genes)
champion = totalvalue
championgenes = genes[:]

#second
for i in range(step):
    print "step number", 
    print i
    genes = [random.randint(0,1) for i in range(len(maindata))]
    totalsize = evaltotalsize(maindata, genes)
    while totalsize > capa:
        newgenes = popup(genes, nummutation)
        totalsize = evaltotalsize(maindata, newgenes)
        genes = newgenes[:]
        print '-----------'
        print totalsize
 

    totalvalue = evaltotalvalue(maindata,genes)
    if champion < totalvalue:
        championgenes = genes[:]

print "answer:"
print step
ans = evaltotalvalue(maindata, championgenes)
print ans