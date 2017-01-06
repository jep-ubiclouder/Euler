'''
Created on 13 sept. 2016

@author: Jean-Eric Preis
'''




if __name__  == '__main__':
    facts=[1,1,2,6,24,120,720,720*7,720*7*8,720*9*8*7]
    nbre=169
    h={}
    for nbre in range(1000):
        res=0
        tmpZ=[]
        while nbre>0:
            unit=nbre%10
            tmpZ.append(unit)
            nbre//=10
            #print(unit)
            tmpZ.sort()


            res+=facts[unit]
        if ''.join('%i'%u for u in tmpZ) not in h.keys():
            h[''.join('%i'%u for u in tmpZ)]=res
    clefs=h.keys()
    #clefs.sort()
    for k in sorted(clefs):
        print(k,h[k])