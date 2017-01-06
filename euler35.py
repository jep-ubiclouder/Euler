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

a=['%s'%(i,) for i in erato(1000000)]
a.append('2')
#a.sort()
## print len(a)
result=[]
for p in a:
    exit = 0
    for c in p:
        if c not in ('1','3','7','9'):
            exit=1
            break
    if exit: continue
    if p not in result:
        roxor(p,result)
    
    
result.append('2')
print result,len(result)

