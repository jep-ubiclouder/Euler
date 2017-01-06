#!/usr/bin/python

## euler199.py

def sdc(n):
    
    z="%s"%(n,)
    res=0
    for c in z:
        res+=int(c)
    return res
def is_puiss(n,test):
    ## retourne  1 si test == n**p
    while test%n == 0 and n<>1:
        test /=n
        if test==1:
            return True
    return False
puissances=[]
for n in range(2,100):
    for p in range(2,100):
        puiss=n**p
        if puiss>10 and puiss not in puissances:
            puissances.append(puiss)
puissances.sort()
print puissances[:50]
print is_puiss(8,512)
print is_puiss(28,614656)
print is_puiss(28,614657)
interet=[]
for test in puissances:
    ##print test
    if  is_puiss(sdc(test),test):
        interet.append((test,sdc(test)))
        print "found %s,%s,index:%s" %(test,sdc(test),len(interet))
interet.sort()
print interet[2],interet[10],interet[30],len(interet)
