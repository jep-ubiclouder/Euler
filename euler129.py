#!/usr/bin/python


# Euler 129
# http://mathschallenge.net/index.php?section=project&ref=problems&id=129
n=1
max=1
while True:
    
    """if n%2==0:
        continue"""
    if n%5==0:
        n+=2
        continue
    
    ## il existe k tel que i divise Rep(k)
    k=1
    repu=1
    while repu%n<>0:
        repu *=10
        repu += 1
        k+=1
        
##        if k> 4:
##            k=1
##            break
##    if k==4:
##    print "k %s,n %s n-1:%s q:%s"%(k,n,n-1,float(n-1)/k)
            
    if k> max:
        max=k
        print "k %s,n %s n-1:%s q:%s"%(k,n,n-1,float(n-1)/k)
    if k >500:
        import sys
        sys.exit()
        
    n+=2
    
