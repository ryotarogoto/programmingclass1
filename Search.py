#!/usr/bin/env python
from jamptable import table

def SimpleSearch(tDNA, eDNA):
    calc = 0
    n1 = len(tDNA)
    n2 = len(eDNA)
    hit_ind = list()

    for ind1 in range(n1):
        calc = calc + 1
        if tDNA[ind1] == eDNA[0]:
            count = 0
            for ind2 in range(n2):
                if (ind1 + ind2) >= n1:
                    break
                if tDNA[ind1 + ind2] == eDNA[ind2]:
                    count = count + 1
                else:
                    calc = calc + 1
                    break
            if count == n2:
                hit_ind.append(ind1)
    return [hit_ind, calc]

def BMMethod(tDNA, eDNA):
    calc = 0
    jamptable = table(eDNA)
    n1 = len(tDNA)
    n2 = len(eDNA)
    hit_ind = list()

    #index DNA1
    indDNA1 = n2 - 1

    while indDNA1 < n1:
        #number of match
        num_mt = -2
        if tDNA[indDNA1] == eDNA[-1]:
            for indDNA2 in range(-2, (-1 * n2 -1), -1):
                if tDNA[indDNA1 + indDNA2 + 1] == eDNA[indDNA2]:
                    num_mt = num_mt - 1
                    if num_mt == (-1 * n2 - 1):
                        hit_ind.append(indDNA1)
                else:
                    jampnum = jamptable[num_mt]
                    
                    calc = calc + 1
                    break
            indDNA1 = jampnum + indDNA1
        else:
            indDNA1 = indDNA1 + 1
            calc = calc + 1

    return [hit_ind, calc]

if __name__ == '__main__':
    from MakeDNA import SimpleDNA
    tDNA = SimpleDNA(10).getDNA()
    eDNA = SimpleDNA(10).getDNA()

    #print tDNA
    print table(eDNA)
    print eDNA
    [matchp1, count1] = SimpleSearch(tDNA, eDNA)
    print matchp1
    print count1
    [matchp2, count2] = BMMethod(tDNA, eDNA)
    print matchp2
    print count2

