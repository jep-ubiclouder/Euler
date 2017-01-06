#!/usrt/bin/python

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




if __name__=='__main__':

    n=0
    primes=erasto(1000000)
    nbdiag=[1]
    squares=[]
    while n<100000:
        n+=1
        nbdiag.append((2*n+1)*(2*n+1))
        squares.append((2*n+1)*(2*n+1))
        nbdiag.append((4*n*n+2*n+1))
        nbdiag.append(4*n*n+1)
        nbdiag.append(4*n*n+1-2*n)

    nbdiag.sort()
    ## print nbdiag
    p=0

    ## pb 28
##    stop=1001*1001
##    res=0
##    for n in nbdiag:
##        if n > stop:
##            break
##        res+=n
##    print res

    
    for n in nbdiag:
        if n in primes: p+=1
        if n in squares:
            total =nbdiag.index(n)+1
            cote=squares.index(n)
            #print total,n,p

            
            """if float(p)/float(total)<0.105:"""
            print p,total,n,float(p)/float(total),2*cote+3
            
            if float(p)/float(total)<0.0985:
               import sys
               sys.exit()
               
            
