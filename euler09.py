#!/usr/bin/python

def gen_triples(u,v):
    return [v*v-u*u,2*v*u,v*v+u*u]



## http://mathworld.wolfram.com/PythagoreanTriple.html
from Numeric import *


""" le seul moyen d'obtenir exhaustivement les triplet pythagoreen."""

if __name__=='__main__':
    
    U=[[1,2,2],[-2,-1,-2],[2,2,3]]
    A=[[1,2,2],[2,1,2],[2,2,3]]
    B=[[-1,-2,-2],[2,1,2],[2,2,3]]
    Id=[[1,0,0],[0,1,0],[0,0,1]]
    base=[[3,4,5]]

    res=[]
    res.append(matrixmultiply(base,Id))
    for mat in (A,B,U):
        res.append(matrixmultiply(base,mat))
        ## print res
    for o in res:
        for mat in (A,B,U):
            tempo=matrixmultiply(o,mat)
            if tempo not in res:
                res.append(tempo)
        if len(res)> 1000:
            break
    res.sort()
    perimetres={}
    for o in res:
        perim=0
        for n in o:
            for truc in n:
                perim += truc
        print perim
        i=1
        while i*perim <1000:
            if not perimetres.has_key(perim*i):
                perimetres[perim*i]=0
            perimetres[perim*i] +=1
            i+=1
    max=0
    for p in perimetres.keys():
        if perimetres[p]>max:
            max=perimetres[p]
            print p,max
    
