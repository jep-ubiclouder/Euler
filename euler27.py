import math
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

a=erato(10000000)

def polyeuler(a,x,y):
    
    i = 0
    while i*i+x*i+y in a: i+=1
    return i

max=1
for p1 in a:
    print 'testing', p1
    if p1 <1000:
        if p1<61: continue
        for p2 in a:
            if p2>1000:
                break
            test=polyeuler(a,p1,p2)
            if test>max:
                print p1,p2,p1*p2,test
                max=test
            test=polyeuler(a,-p1,p2)
            if test>max:
                print -p1,p2,-p1*p2,test
                max=test
            test=polyeuler(a,p1,-p2)
            if test>max:
                print p1,-p2,-p1*p2,test
                max=test
            test=polyeuler(a,-p1,-p2)
            if test>max:
                print -p1,-p2,p1*p2,test
                max=test
