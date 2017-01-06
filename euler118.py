##import math
##def erato(nbr):                #crible d'eratosthene
##    premier=range(3,nbr,2)     #retourne la liste des
##    long=len(premier)          #nombres premiers inferieurs a "nbr"
##    i=0
##    next=3
##    fin=int(math.sqrt(float(nbr)))+1
##    while next<fin:
##        j=i+next
##        while j<long:
##            premier[j]=0 #met a 0 les multiples de next
##            j=j+next
##        i=i+1
##        while  (premier[i]==0):#saute les non premiers déjà à 0
##            i=i+1
##        next =premier[i] #Le nombre premier suivant
##    premier=filter(None,premier) #enleve les termes nuls du tableau
##    return premier


def primes():
    '''Yields the sequence of primes via the Sieve of Eratosthenes.'''
    yield 2                 # Only even prime.  Sieve only odd numbers.

    # Generate recursively the sequence of primes up to sqrt(n).
    # Each p from the sequence is used to initiate sieving at p*p.
    roots = primes()
    root = roots.next()
    square = root*root

    # The main sieving loop.
    # We use a hash table D such that D[n]=2p for p a prime factor of n.
    # Each prime p up to sqrt(n) appears once as a value in D, and is
    # moved to successive odd multiples of p as the sieve progresses.
    D = {}
    n = 3
    while True:
        if n >= square:     # Time to include another square?
            D[square] = root+root
            root = roots.next()
            square = root*root

        if n not in D:      # Not witnessed, must be prime.
            yield n
        else:               # Move witness p to next free multiple.
            p = D[n]
            q = n+p
            while q in D:
                q += p
            del D[n]
            D[q] = p
        n += 2       
def remplirclasses(n):
    wrk="%s"%(n,)
    c=[m for m in wrk]
    c.sort()
    wrk =''.join(e for e in c)

    if '0'in wrk:
        return
    for i in range(len(wrk)-1) :
        if wrk[i] in wrk[i+1:]: ## un doublon
            return
    for nt in range(1,10):
        if '%s'%(nt,) in wrk:
            classe['%s'%(nt,)].append(wrk)
            return

p=primes()
n=p.next()
max=10000000
global classe
classe={}
for i in range(1,10):classe['%s'%(i,)]=[]


while n < max:
    remplirclasses(n)
    n=p.next()
    
##a=erato(9876543)
##a.append(2)
##a.sort()
##print len(a)
##print a[:20]
##for p in a:
##    remplirclasses(p)
for k in classe.keys(): print k,len(classe[k])
print classe['1'][:10]
