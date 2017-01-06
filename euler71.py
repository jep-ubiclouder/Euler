#!/usr/bin/python

## 3/7= 0.42857142857142855
## avec quelle est n/d avec d<=10^6 max(n/d)<3/7 ?
## pour chaque d

class fraction:
    def __init__(self,n,d):
        
        self.n=n/GCD(n,d)
        self.d=d/GCD(n,d)
        # je voudrais un fraction irredutible
        
def GCD(a,b):
    if a == b:
        return a
    else:
        while a > 0 and b > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
    return max(a, b)


def HCM(a,b):
    return a*b/GCD(a,b)

def lessthan(f1,f2):
    # true si f1<f2, false si f1>f2
    return (f1.n*f2.d)<(f1.d*f2.n)

def moyenne(f1,f2):
    d=HCM(f1.d,f2.d)
    
    n=f1.n*d/f1.d+f2.n*d/f2.d
    
    ## GCD(a,b)*LCM(a,b)==ab
    f3=fraction(n,d*2)
    return f3

def farey(f1,f2):
    ## posons f1<f2
    return fraction(f1.n+f2.n,f1.d+f2.d)
    
if __name__=='__main__':

    ## n/d est encadre par 2/5 et 3/7
    ## je vais reduire cet intervalle par dichotomie ce qui me laissera tres peu de valeurs a tester.

    f1=fraction(3,8)
    print f1.d,f1.n
    f2=fraction(3,7)
    f3=farey(f1,f2)
    print f3.n,f3.d
    res=[f3]
    while f3.d<1500000:
        #print "%s/%s"%(f3.n,f3.d)
        if f3.d<=1000000:res.append(f3)
        f3=farey(f3,f2)

    print ['%s/%s'%(f3.n,f3.d) for f3 in res]
##    f3=res[-1]
##    i=0
##    while True:
    
##        f4=fraction(70217+i,163840)
##        if lessthan(f4,f2): i+=1
##        else:
##            f5=fraction(70217+i-1,163840)
##            print f5.n,f5.d,i
##            break

        
##    res=[f5]
##    while f5.d<200000000000:
##        print "%s/%s"%(f5.n,f5.d)
##        if f5.d<=1000000:res.append(f5)
##        f5=moyenne(f2,f5)

##    print ['%s/%s'%(f.n,f.d) for f in res]
##    f=res[-1]
        
    
    
