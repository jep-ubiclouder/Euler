#!/usr/bin/python

## Euler 131

"""trouver les premiers de la forme 3b²+3b+1
 p > 100000
"""
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
        while  (premier[i]==0):
                        i=i+1
        next =premier[i] #Le nombre premier suivant
        
    premier=filter(None,premier) #enleve les termes nuls du tableau
    return premier
max=1000000
import math 
borne =int(math.sqrt(max))
primes=erato(1000000)
resul=[]
for i in range(borne):
    p= 3*i*(i+1)+1
    if p in primes:
        resul.append(p)
        print i,p
print len(resul),resul
  