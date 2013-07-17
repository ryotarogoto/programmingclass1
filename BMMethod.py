from MakeDNA import SimpleDNA


def maketable1(DNA):
    f1 = lambda x:1 if x=='A' else 0
    f2 = lambda x:1 if x=='T' else 0
    f3 = lambda x:1 if x=='C' else 0
    f4 = lambda x:1 if x=='G' else 0

    a = [f1(x) for x in DNA]
    t = [f2(x) for x in DNA]
    c = [f3(x) for x in DNA]
    g = [f4(x) for x in DNA]
    return [a, t, c, g]

def check(zeros):
    jamptable = list()
    memo = 0
    count = 0
    for i in zeros:
        if i == 1:
            if count == 0:
                count = memo
            else:
                jamptable.append(memo - count)
                count = memo
        memo = memo + 1

    return jamptable

def lasttable(tDNA, a, t, c, g):
    jamptable = list()
    al = check(a)
    tl = check(t)
    cl = check(c)
    gl = check(g)

    al.append(len(tDNA))
    tl.append(len(tDNA))
    cl.append(len(tDNA))
    gl.append(len(tDNA))

    print al
    al.reverse()
    tl.reverse()
    cl.reverse()
    gl.reverse()
    print al


    count = 0
    for i in tDNA:
        print count
        if i == 'A':
            a = al.pop()
            jamptable.append(a)
        elif i == 'T':
            t = tl.pop()
            jamptable.append(t)
        elif i == 'C':
            c = cl.pop()
            jamptable.append(c)
        else:
            g = gl.pop()
            jamptable.append(g)
        count = count + 1
    return jamptable
            

    
            
            
            


def reverse(ary):
    n1 = len(ary)
    return [ary[x] for x in range(-1, (-1 * n1 + 1), -1)]

def countone(ary):
    count = 0
    for i in ary:
        if i == 1:
            
            count = 0
    
def makejamptable(a, t, c, g):
    jamptable = list()
    az = reverse(a)
    tz = reverse(t)
    cz = reverse(c)
    gz = reverse(g)

    
    
    return jamptable
    
    
DNA = SimpleDNA(100).getDNA()
print DNA
[a, t, c, g] = maketable1(DNA)
az = check(a)
test = lasttable(DNA, a, t, c, g)
print az
print test
print sum(a)

[an, tn, cn, gn] = [sum(a), sum(t), sum(c), sum(g)]
Ld = len(DNA)




    
    
    
    
