"""
Problem 124

The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
"""

import math

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

def radical(n,premiers):
    result=[1]
    while True:
        ##print n
        if n in premiers:
            if n not in result:
                result.append(n)
            break
        else:
            for p in premiers:
                if n%p :
                    continue
                else:
                    if p not in result:
                        result.append(p)
                    n= n/p
                    break
    res=1
    for i in result:
        res *= i
    return res


""" main"""
prem =primes()
p=prem.next()
print p
n=1
stop=0
premiers=[]

while p <100000:
    premiers.append(p)
    p=prem.next()

# print premiers
rads=[(0,0),(1,1)]
for i in range(2,100000):
    tmp= radical(i,premiers)
    val=1
    rads.append((tmp,i))
    """print i,val,tmp"""
rads.sort()
for (r,nb) in rads:
    if r== 1947:
        print r,nb
