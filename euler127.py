"""
Problem 127
01 September 2006

The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 32 7, so rad(504) = 2 3 7 = 42.

We shall define the triplet (a, b, c) to be an abc-hit if:

   1. GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
   2. a b
   3. a + b = c
   4. rad(abc) c

For example, (5, 27, 32) is an abc-hit, because:

   1. GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
   2. 5 <27
   3. 5 + 27 = 32
   4. rad(4320) = 30 32

It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c 1000, with Sigma(c) = 12523.

Find Sigma(c) for c< 100000.

"""
def erato(n):
   """
   Suggestions from Ka-Ping Yee, John Posner and Tim Peters"""
   sieve = [0, 0, 1] + [1, 0] * (n/2) # [0 0 1 1 0 1 0...]

   prime = 3                          # initial odd prime

   while prime**2 <= n:
       for i in range(prime**2, n+1, prime*2): 
            sieve[i] = 0      # step through sieve by prime*2

       prime += 1 + sieve[prime+1:].index(1) # get next prime

   # filter includes corresponding integers where sieve = 1

   return filter(lambda i, sieve=sieve: sieve[i], range(n+1))
from math import sqrt
def getfactors(n):
   """Return list containing prime factors of a number."""
   if n in primes or n==1: return [n]
   else:
       retval=[]
       borne=n
       for i in primes:
           if i >n: return retval
               
           if not n%i: # if goes evenly
               retval.append(i)
               while not n%i: n = n/i
       return retval


def GDC(a,b):
    if a == b:
        return a
    else:
        while a > 0 and b > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
    return max(a, b)

maxi=10000

primes=erato(maxi)
decomps=[[0,0],[1,1]]
"""
for i in range(2,maxi*2):
    tmp=getfactors(i)
    yo=1
    for t in tmp:
        yo*=t
    decomps.append([tmp,yo])
"""
resul=0
nbre=0
for i in range(2,maxi):
    for j in range (i+1,maxi):
        if i+j>maxi:
            break
        if GDC(i,j)== 1 and GDC(i,i+j)==1 and GDC(j,i+j)==1:
            prod=(i+j)*i*j
            yo=1
            for n in getfactors(prod):
                yo*=n
            if yo < (i+j):
                print i,j,i+j,yo
                resul+=(i+j)
                nbre+=1
print resul,nbre
