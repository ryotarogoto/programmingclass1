#!/usr/bin/env python

def table(DNA):
    jamptable = list()
    
    cpDNA = DNA[:]
    cp2DNA = DNA[:]

    cpDNA.reverse()
    cp2DNA.reverse()
    
    i = 0
    for ele in cpDNA:
        try:
            if  ele == 'A':
                matchind = cp2DNA[(i + 1):].index('A')
            elif ele == 'T':
                matchind = cp2DNA[(i + 1):].index('T')
            elif ele == 'C':
                matchind = cp2DNA[(i + 1):].index('C')
            else:
                matchind = cp2DNA[(i + 1):].index('G')
            jamptable.append((matchind+1))
        except ValueError:
            jamptable.append(1)

        i = i + 1
    jamptable.reverse()
    return jamptable

if __name__ == '__main__':
    from MakeDNA import SimpleDNA
    DNA = SimpleDNA(100).getDNA()

    print DNA
    print table(DNA)
            
            
            



    
