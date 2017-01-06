
import math
def roxor(s,result):
    start='%s%s'%(s[-1],s[:-1])
    buff=[]
    while start<>s:
        ## print start,s
        if start not in a:
            return 0
        else:
            buff.append(start)
        start='%s%s'%(start[-1],start[:-1])
    if s not in buff:
        buff.append(s)
    for p in buff:
        result.append(p)
    return 1



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


def l2r(s):
    for i in range(1,len(s)):
        # print i,s[:-i]
        if s[:-i] not in a:
            return False
    return True
def r2l(s):
    for i in range(len(s)):
        #print i,s[i:]
        if s[i:] not in a:
            return False
    return True

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
prem=primes()
p=prem.next()
result=['23','53']
a=['3','7']
while len(result)<11:
    p='%s'%(prem.next())
    exit = 0
    for c in p:
        if c not in ('1','3','7','9'):
            exit=1
            break
    if len(p)==1 or exit : continue
    print p
    a.append(p)
    if l2r(p) and r2l(p):
        result.append(p)
        print result,len(a)
print result
    
##a=['%s'%(i,) for i in erato(100000000)]
##a.append('2')
###a.sort()
#### print len(a)
##result=[]
##for p in a:
##    exit = 0
##    for c in p:
##        if c not in ('1','3','7','9'):
##            exit=1
##            break
##    if len(p)==1 or exit : continue
    
##    if l2r(p) and r2l(p):
##        result.append(p)
    
#### result.append('2')
##print result,len(result)

