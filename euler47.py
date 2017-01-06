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



def genbits(tab):
    res=[0]*(tab[-1]+1)
    for b in tab: res[b]=1
    return res



def nuples(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in nuples(items[i+1:],n-1):
                yield [items[i]]+cc

def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss
if __name__=='__main__':
    primes=erasto(50000)
    ## print primes
    quatfac=[]


##    for t in xselections(range(4),4):
##        print t
    MAXIMUM=238210 ## Experimentalement
    consec=[]
    for i in range(MAXIMUM):
        if len(getfactors(i))==4:
            consec.append(i)
            if len(consec)>=3: print consec
            if len(consec)==4:
                for n in consec: print getfactors(n)
                # print getfactors(644),getfactors(645),getfactors(646)
                import sys
                sys.exit()
                
        else:
            consec=[]
    import sys
    sys.exit()


    
    for n in nuples(range(25),4):

        bits= genbits(n)
        nbre=1
        facteurs=[]
        for (e,p) in zip(bits,primes):
            if e:
                nbre *= p
                if nbre > MAXIMUM: 
                    continue 
                facteurs.append(p)
        quatfac.append(nbre)
        for expo  in xselections(range(6),4) :
            test=nbre
            ## print expo
            for (e, p) in zip(expo,facteurs):
                ## print e,p
                ### Strategie 2 factoristion de n+1  et n-1

                if e:
                    test=nbre*(p**e)
            if test > MAXIMUM: 
                continue 
            consecut=1
            if test  not in quatfac:
                # print nbre,p*(p**e),(p**e)
                quatfac.append(test)
            else:
                continue
            if len(getfactors(test-1))==4 :                
                #print 'jumeaux',test,test-1
                consecut+=1
                quatfac.append(test-1)  
                if len(getfactors(test-2))==4 :
                    #print "Triples",test-2,test-1,nbre
                    consecut+=1
                    quatfac.append(test-2)
                    if len(getfactors(test-3))==4 :
                        print "n-3",test-3,test-1,nbre
                        consecut+=1
                        quatfac.append(test-3)
                        
            if len(getfactors(test+1))==4 :
                #print 'jumeaux',test,test+1
                quatfac.append(test+1)
                consecut+=1
                if len(getfactors(test+2))==4 :
                    #print "Triples",test+2,test+1,test
                    quatfac.append(test+2)
                    consecut+=1
                    if len(getfactors(test+3))==4 :
                        print "n +3 ",test+3,test-1,test
                        consecut+=1
                        quatfac.append(test-2)  
            if consecut >=4:
                print 'factoriser range(%s-4,%s+4)'%(test,test)
##                import sys
##                sys.exit()
##        if nbre -1 in quatfac:
##            print 'des jumaeaux',nbre,nbre-1
##            if  nbre-2 in quatfac:
##                print 'des triple',nbre,nbre-1,nbre-2
##                if  nbre-3 in quatfac:
##                    print 'des triples',nbre,nbre-1,nbre-2,nbre-3
##                    import sys
##                    sys.exit()


            
    print len(quatfac)

    quatfac.sort()
    for n in quatfac:

        if n+1 in quatfac and n+2 in quatfac and n+3 in quatfac:
            print n,n+1,n+2,n+3
            import sys
            sys.exit()
    print 'peu etre un peu pti'
    
##    res= 1
##    for (e,p) in zip(base,primes):
##        if e:
##            res *= p
##    print res
##    tab= genrange(6)
##    taille=3
##    global base 
##    base=range(taille)
##    bul=bulle(25,3)
##    quatfac=[]
##    for b in bul:
##        print b
##        bits= genbits(b)
##        nbre=1
##        for (e,p) in zip(bits,primes):
##            if e:
##                nbre *= p
##        quatfac.append(nbre)
##    quatfac.sort()
##    print quatfac
        
    ## je deplace le 1 le plus a droite
    
    
