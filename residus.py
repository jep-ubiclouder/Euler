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
    premier.append(2)
    premier.sort()
    return premier

primes = erato(100000)
primes=[17,24001,1378001,60101,251,5051,10000099999999989999899999000000000100001, 401  ,3541,27961,1201  ,1601,73,409]
for p in primes :
    residus=[]
    r=1
    while r not in residus:
        residus.append(r)
        r*=10
        r%=p

    print( p,len(residus),primes.index(p))



