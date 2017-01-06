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

primes=erato(1000000)
primes.append(2)
primes.sort()
print 'premiers!',len(primes)
i=0
import sys
max=1
rep=0
for q in primes:
    if q >primes[-max]:break
    buff=0
    i=0
    sys.stdout.write(" Now %s.%s"%(q,primes[-max]))
    for p in primes[primes.index(q):]:
        if  buff>primes[-1]:break
        
        ##print q,p
        buff+=p
        i+=1
        if buff in primes:
           
            if i>max:
                max=i
                res=buff
                print "*",buff,i
print "***",res,max
