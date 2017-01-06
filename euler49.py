def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

import math
def erato(nbr):                #crible d'eratosthene
    premier=range(3,nbr,2)     #retourne la liste des
    long=len(premier)          #nombres premiers inferieurs a "nbr"
    i=0
    next=3
    fin=int(math.sqrt(float(nbr)))+1
    while next<fin:
        j=i+next
        while j<long:
            premier[j]=0 #met a 0 les multiples de next
            j=j+next
        i=i+1
        while  (premier[i]==0):#saute les non premiers déjà à 0
            i=i+1
        next =premier[i] #Le nombre premier suivant
    premier=filter(None,premier) #enleve les termes nuls du tableau
    return premier

primes=erato(10000)
sol=0
import sys
for p in primes:
    if p <1000:continue
    if sol==2: sys.exit()
    # print p
    xcomb=[]
    for p1 in xcombinations(list('%s'%(p,)),4):
        test=int(''.join(p1))
        if test in primes:
            xcomb.append(test)

    for test in xcomb:
        if test==p: continue
        if test<1000:continue
        
        d=abs(test-p)
        if (max(test,p)+d) in xcomb :
            print test,p,(max(test,p)+d),d
            sol+=1
