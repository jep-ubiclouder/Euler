#!/usr/bin/python

def erasto(n):
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
   if n in _primes or n==1: return [n]
   else: 
       for i in _primes:
           if not n%i: # if goes evenly

               n = n/i
               return [i] + getfactors(n)
_primes=erasto(30000)

def add(x,y):
	return x+y

def divisors(n):
   """Get all the divisors of a number"""
   d = []
   for i in range(1,int(sqrt(n))+1):
      if n % i == 0:
         if n/i != i:
            d += [i,n/i]
         else:
            d += [i]
   return d





def abondant(n):
	## print i,reduce(add,divisors(n))
	return n>1 and 2*n<reduce(add,divisors(n))	

abds=[]
for i in range(2,25000):
    if i in _primes: 
	continue
    
    if abondant(i):
       abds.append(i)
## print abds,len(abds)
result=0

for i in range(2,25000):
   #if i in abds:continue
   if i %1000==0:print i
   for a in abds:
      d=i-a
      if d in abds: # decomposition trouvee
         # print i,d,a
         break

      if i < a: ## pas trouve de somme
         #print i
         result+=i
         break
print result
