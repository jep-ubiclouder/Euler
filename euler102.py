#!/usr/bin/python


class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
def droite(pa,pb,ptest):
    """ retourne si l'origine des dans la meme region que le ptest"""
    
    x1=pa.x-pb.x
    y1=pa.y-pb.y

    test=(x1*(ptest.y-pa.y)-y1*(ptest.x-pa.x))>0
    test0=(pa.x*y1-x1*pa.y)>0

    return test==test0


if __name__=='__main__':
    h=open('triangles.txt')
    res=0
    for l in h.readlines():
        c=l[:-2].split(',')
        
        pa=point(int(c[0]),int(c[1]))
        pb=point(int(c[2]),int(c[3]))
        pc=point(int(c[4]),int(c[5]))
        if droite(pa,pb,pc) and droite(pa,pc,pb) and droite(pc,pb,pa)  :
            res += 1
    print res,c
