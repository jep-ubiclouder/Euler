#!/usr/bin/python

from math import *
import time
import sys
## from mx.DateTime import*
from sage.all import *


if __name__=="__main__":
    for i in range(2,10000):
        R=RealField(2048)
        print continued_fraction((R(i).sqrt()))
        
##def xcombinations(items, n):
##    if n==0: yield []
##    else:
##        for i in xrange(len(items)):
##            for cc in xcombinations(items[:i]+items[i+1:],n-1):

##                yield [items[i]]+cc

##def xselections(items, n):
##    if n==0: yield []
##    else:
##        for i in xrange(len(items)):
##            for ss in xselections(items, n-1):
##                yield [items[i]]+ss

##def xuniqueCombinations(items, n):
##    if n==0: yield []
##    else:
##        for i in xrange(len(items)):
##            for cc in xuniqueCombinations(items[i+1:],n-1):
##                yield [items[i]]+cc
                
##def xpermutations(items):
##    return xcombinations(items, len(items))

##if __name__=="__main__":
##    # print "Permutations of 'love'"
##    cpte=1
##    start=time.time()
##    #0a  =
##    for p in  xcombinations(list('7654321'),7):
##        if is_prime(int(''.join(p))):
##            print int(''.join(p))
##            sys.exit()
##if __name__=="__main__":
##    p=prime_pi(999999999)
##    print len(p)
    
##    R=RealField(1000)
##    c=convergents(continued_fraction(R(1).exp()))
##    print c[:5],len(c)
##    res=0
##    for n in c[99].numer().str(): res+=int(n)
##    print res

    
##    res=0
##    for i in range(1,101):
##        if  is_square(i):  continue
##        R=RealField(2500)
        
##        s=R(i).sqrt()*10**101
    
        
##        for c in s.str()[:100]:
##            res+=int(c)
            
##            #print res,i,s,c
##    print res
        


    
##    max=0
##    start=time.time()
##    for i in range(2,1001):
##        R=RealField(2500)
##        for r in convergents(continued_fraction(R(i).sqrt())):
##            n,d=r.numer(),r.denom()
##            if d==1:continue
##            if n*n-i*d*d==1:
##                print i,n,d
##                if n > max:
##                    max=n
##                    res=i
##                break
##    print "resultat max:%s D:%s temps:%f"%(max,res,time.time()-start)
            
            
        









##    cpte=0
##    for i in range(1,11):
##        for j in range(1,2000):
##            if int(log10(i**j))+1==j:
##                cpte+=1
##    print cpte



    
##def c(n,r):
##    if r>n :return 1
##    return(facts[n]/facts[r]/facts[n-r])
##if __name__=="__main__":
##    global facts
##    facts=[1,1]
##    for i in range(2,102):
##        facts.append(i*facts[i-1])
##    cpte=0
##    for n in range(1,101):
##        for r in range(1,n+1):
##            if c(n,r) >=1000000: cpte+=1
##    print cpte



##    t=[]
##    for i in range(1000000):
##        for a in list('%s'%(i,)): t.append(int(a))
##        if len(t)>1000000: break
##    print i,t[1]*t[10]*t[100]*t[1000]*t[10000]*t[100000]*t[1000000]
##def chk(s,t):
    
##    for c in s:
##        if c not in t :
##            return False
##    return True

##if __name__=="__main__":
##    for i in range(1,10):
##        for j in range(10**i,2*10**i):
##            if j%3: continue  ## le nombre est forcement divisible par 3
##            if int(log10(6*j)) > i: 
##                break
##            base='%s'%(j,)
##            for c in range(2,7):
##                s='%s'%(c*j,)
##                if not chk(s,base):
##                    break
##                elif c > 3:
##                    print 'match',j,c,s
##        print base
        
#    res=0
##    start=DateTime(1901,1,6) ##premier dimanche du siecle
##    t=start.COMDate()
##    while True:
##        t+=7
##        tmp=DateTimeFromCOMDate(t)
        
##        if  tmp.day==1:
##            res +=1
##            print 'Match:',tmp.date,res
##        if tmp.year >2001: sys.exit()
        
    
##def ispalin(s):
##    v=True
##    ## print s
##    for i in range(len(s)/2):
##        ## print i,-(i+1),s[i],s[-(i+1)]
##        if s[i]<>s[-(i+1)]:
##            return False
##    return v


##def tobin(x, count=8):
##        """
##        Integer to binary
##        Count is number of bits
##        """
##        return "".join(map(lambda y:str((x>>y)&1), range(count-1, -1, -1)))

##def dropZ(s):
##    for i in range(len(s)):
##        if s[i]<>'0': return s[i:]
##def toDecimal(x):
##    return sum(map(lambda z: int(x[z]) and 2**(len(x) - z - 1),  
##                   range(len(x)-1, -1, -1)))

##
##    print ispalin('585'),ispalin('1001001001')
    
##    res=0
##    for i in range(1,1000000):
##        if ispalin('%s'%(i,)) and ispalin(dropZ(tobin(i,32))):
##            print  'match',i
##            res+=i
##    print res
    
##def sump5chif(n):
##    s='%s'%(n,)
##    res=0
##    for c in s:
##        res+=p4[int(c)]
##    return res

    
##    global p4
##    p4=[i**5 for i in range(10)]
##    print p4
##    s=0
##    for i in range(2,10000000):
##        if i==sump5chif(i):
##            print 'match',i
##            s+=i
##    print s
        

##def nametoval(s):
##    sum=0
##    for l in s:
##        sum+=ord(l)-64
##    return sum    
##    print nametoval('COLIN')
##    h=open("/home/jep/ipod/Download/names.txt")
##    compte=1
##    res=0
##    arr=[]
##    for lig in h.readlines():
        
##        for nom in lig.split(','):
##            arr.append(nom[1:-1])
##        arr.sort()
##        for nom in arr:
##            res+=nametoval(nom)*compte
##            compte+=1
##    print res,compte
    
##   max=50000
##    res=[i*(3*i-1)/2 for i in range(max+1)]
##    for i in range(1,max):
    
##        for j in range(i+1,max/2):
##            if res[i]+res[j] in res:
##                print i,j,res[i]+res[j],abs(res[i]-res[j])
##                if abs(res[i]-res[j]) in res:
##                    print "*****=> reponse",i,j,res[i]+res[j],abs(res[i]-res[j])
##                    sys.exit()
                
                    

##    s=1
##    modulo=10**10
##    expo=7830457
##    cpte=0
##    while expo >=1:
##        print expo,cpte,2**cpte,s
##        if expo %2: ## le bit a droite est up
##            s*=2**(2**cpte) % modulo
##        cpte+=1
##        expo=expo>>1
##    print s
##    print  (28433*s) %modulo +1


## 264338388211803426224830977
##    3386738249
##    11803426 224 830 977
##    tab=[]
##    for a in range(2,101):
##        for b in range(2,101):
##            c=a**b
##            if not c in tab:
##                tab.append(c)
##    print len(tab)

##def factor(n):
##    d=1
##    # factors=[]
##    sumf=0
##    while d < sqrt(n):
##        if n%d==0:
##            sumf +=d
##            sumf += (n/d)
##        d+=1
##    return sumf-n

##if __name__=="__main__":
##    limit=10000
##    test= [1 for i in range(limit+1)]
##    amis=[]
##    #print test
##    for i in range(2,limit):
##        if test[i]==1:
            
##            f=factor(i)
##            test[i]=f
##            try:
##                test[f]=factor(f)
##                if i==test[f] and i<>f:
##                    print i,f
##                    amis.append((i,f))
##            except:
##                continue
##    print amis,sum(a+b for (a,b) in amis)
##def sumfac_chif(n):1
##    t='%s'%(n,)
##    tmp=0
##    for c in t:
##        tmp+=fact_chiffre[int(c)]
##    return tmp

##if __name__=="__main__":
##    global fact_chiffre
##    fact_chiffre=[1,1,2,6,24,120,720,5040,40320,362880]
##    i=3
##    while 1:
##        if i == sumfac_chif(i): print i
##        i+=1


##def factor(n):
##    d=2
##    factors=[]
##    while d < sqrt(n):
##        if n%d==0:
##            factors.append(d)
##            factors.append(n/d)
            
##        d+=1
##    return factors

##if __name__=="__main__":
##    start=time.time()
##    n=1
##    a=factor((n*(n+1))/2)
##    max=1
####    while len(a)<500:

##        if len(a)>max:
##            max=len(a)
##            print n-1,len(a)
##        a=factor((n*(n+1))/2)
##        n+=1
##    print "reponse:n:%s,valeur%s"%(n-1,((n-1)*n)/2)
##    print time.time()-start,'secondes'

##    a=factor(76576500)
##    print len(a)

###from __future__ import generators

##def xcombinations(items, n):
##    if n==0: yield []
##    else:
##        for i in xrange(len(items)):
##            for cc in xcombinations(items[:i]+items[i+1:],n-1):

##                yield [items[i]]+cc

##def xuniqueCombinations(items, n):
##    if n==0: yield []
##    else:
##        for i in xrange(len(items)):
##            for cc in xuniqueCombinations(items[i+1:],n-1):
##                yield [items[i]]+cc
            

##def xpermutations(items):
##    return xcombinations(items, len(items))

##if __name__=="__main__":
##    # print "Permutations of 'love'"
##    cpte=1
##    start=time.time()
##    #0a  =
##    for p in  xpermutations(list('0123456789')):
        
##        if cpte<1000000:
            
##            cpte+=1
##        else:
##            print ''.join(p),cpte
##            print time.time()-start
##            break
        
        

##    print
##    print """Combinations of 2 letters from 'love'"""
##    for c in xcombinations(['l','o','v','e'],2): print ''.join(c)

##    print
##    print "Unique Combinations of 2 letters from 'love'"
##    for uc in xuniqueCombinations(['l','o','v','e'],2): print ''.join(uc)

##    print
##    print "Selections of 2 letters from 'love'"
##    for s in xselections(['l','o','v','e'],2): print ''.join(s)

##    print
##    print map(''.join, list(xpermutations('done')))


##"""
### fibonacci

##f=[1,1]
##b=f[0]+f[1]
##i=2
##while log10(b)<1000:
##		i+=1
##		f[0]=f[1]
##		f[1]=b
##		b=f[0]+f[1]
##print i,log10(b)
##"""

##"""
### premiers
##import time, math
##s = time.time()
##"""
##def IsPrime( n ):
##		if n == 2:
##				return 1
##		elif n % 2 == 0:
##				return 0
  
##		i = 3
##		range = int( sqrt(n) ) + 1
##		while( i < range ):
##				if( n % i == 0):
##						return 0
##				i += 1
##		return 1
##"""
##S=0
##N=2
##while N < 1000000:
##		if IsPrime(N):
##				S+=N
##		N+=1
##print S,N
##print time.time() - s
##"""
##"""
##def prod(a,b,c,d,e):
##		return a*b*c*d*e
##a='''7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'''
##max=0
##for i in range(len(a)-5):
##		test=prod(int(a[i]),int(a[i+1]),int(a[i+2]),int(a[i+3]),int(a[i+4]))
##		if test>max: 
##				print test ,i
##				max=test
##print max"""

##a=1209511
##rac=int(sqrt(a))+1
##while True:
##		if a%rac==0:
##				print a/rac,rac,a*rac,IsPrime(rac)
##				break
##		rac-=1
		
##matr="""
##08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
##49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
##81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
##52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
##22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
##24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
##32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
##67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
##24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
##21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
##78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
##16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
##86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
##19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
##04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
##88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
##04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
##20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
##20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
##01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
##"""
###for i in matr.split('/n'):print i



