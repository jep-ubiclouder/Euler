#!/usr/bin/python


def digsig(n):
    res=0
    for c in str(n):
        res +=int(c)
    return res
if __name__=='__main__':
    max= 0
    for a in range(100,50,-1):
        for b in range(100,50,-1):
            nb=digsig(a**b)
            if nb>max: max=nb
    print max
