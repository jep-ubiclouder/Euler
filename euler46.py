#!/usr/bin/python
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

def carres(lim):
    i=1
    tmp=[]
    while i*i <lim:
        tmp.append(i*i)
        i+=1
    return tmp


import sys
if __name__=='__main__':
    primes=erato(1000000)
    print "primes fait"
    squares=carres(1000000)
    print "squares"
    i=0
    while 1:
        i+=1
        odd=2*i+1
        if odd not in primes:
            for s in squares:
                test=odd-2*s
                if test in primes:
                    ##print odd,test,2*s,s
                    break
                if s/2 > odd:
                    print "reponse",odd
                    sys.exit()
            
        
