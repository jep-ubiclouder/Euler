#!/usr/bin/python


def ipow(a,b,n):
    #calculates (a**b)%n via binary exponentiation, yielding itermediate
    #results as Rabin-Miller requires
    A = a = long(a%n)
    yield A
    t = 1L
    while t <= b:
        t <<= 1
    
    #t = 2**k, and t > b
    t >>= 2
    
    while t:
        A = (A * A)%n
        if t & b:
            A = (A * a) % n
        yield A
        t >>= 1



def isprimerabin(n):
    for p in (3,5,7,11,13,17,19):
        print p
        if 1 not in  ipow(n,p-1,p): return False
    return True


def residu():
    res={}
    for p in (3,5,7,11,13,17,19):
        res[p]=[]
        for i in range(35):
            res[p].append(2L**i%p)

    return res
def gen_nbre(l_max,classe,max_repeat):
    lst_essai=[]
    for i in range(10):
        if i<>classe: lst_essai.append(i)
    

def nbrefromliste(liste):
    res=0
    for c in liste:
        print res,c
        res *= 10
        res +=int(c)
    return res


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



if __name__=='__main__':
    residus=residu()
    #print residus
    print isprimerabin(9876543211)
    ## for i in  xcombinations((1,1,1,2),3): print i
    print nbrefromliste((1,2,3,4,5,6,7,8,9))+1
