'''
@author: Jean-Eric Preis
'''
import math
if __name__  == '__main__':
    m= 121
    s=math.ceil(math.sqrt(m))
    l = 2
    b = 10
    carte = {}
    for r in range(s):
        print(l*b**r%m,r)
        carte[l*b**r%m]=r

    for t in range(1,r+2):
        #print(b**(t*r)%m)
        if(b**(t*r)%m in carte.keys()):
            print(b**(t*r)%m , carte[b**(t*r)%m], t*r)
            print(abs(t*r - carte[b**(t*r)%m])  , b**(abs(t*r - carte[b**(t*r)%m] ) )%m,l,len(carte))
            break