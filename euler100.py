#!/usr/bin/python

class fraction:
    def __init__(self,n,d=1):    
        self.n=n/GCD(n,d)
        self.d=d/GCD(n,d)
        # je voudrais un fraction irredutible
        
    def __add__(self,f):
        # print self.d*f.d*(self.n+f.n),(self.d*f.d)
        return fraction(f.d*self.n+self.d*f.n,(self.d*f.d))
    
    def inverse(self):
        return fraction(self.d,self.n)
    
def GCD(a,b):
    if a == b:
        return a
    else:
        while a > 0 and b > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
    return max(a, b)
        
def reduced_cont_frac(tab):
    """
    p_(-2)=0 q_(-2)=1	(22)
    p_(-1)=1 q_(-1)=0	(23)
    p_0=a_0 q_0=1.	(24)
    p_n==a_np_(n-1)+p_(n-2)	(25)
    q_n==a_nq_(n-1)+q_(n-2).

    """
    p=[0,1]
    q=[1,0]
    from math import log10
    res=0
    for c in tab:
        p.append(c*p[-1]+p[-2])
        q.append(c*q[-1]+q[-2])
        if int(log10(p[-1]))>int(log10(q[-1])):
            res +=1
        ##float(p[-1])/float(q[-1])
    print res
        
if __name__=='__main__':

    tab=[(803761, 568345),(137904 ,97513),(23661, 16731),(4060 ,2871),(697, 493),(120,85),(21, 15),(4 ,3)]

    raps=(5.82840961829,
          5.82832509192,
          5.82783251232,
          5.82496413199,
          5.80833333333
          )
    for r in raps: print r*r
##    a=[]
##    i=1000000000000L
##    while True:
##        a.append(i*(i-1)/2)
##    a.reverse()
##    for i in range(len(a)):
##        if  not (a[i] & 1) and  a[i]>>1  in a:
##            print i,a[i],a[i]/2,a.index(a[i]/2)
##    tab=[
##        '296238 323015470680 161507735340 531654',
##        '962095 9508687656 4754343828 1002486',
##        '1076338 279909630 139954815 1083268',
##        '1095939 8239770 4119885 1097128',
##        '1099302 242556 121278 1099506',
##        '1099879 7140 3570 1099914',
##        '1099978 210 105 1099984',
##        '1099995 6 3 1099996',
##        '1099998 0 0 1099998'
##        ]

##    a=[2]*1000
##    a.append(1)
##    a.reverse()

####    f=fraction(1,2)
####    g=fraction(1,3)
####    p=f+ g
####    print p.n,p.d
##    reduced_cont_frac(a)
##    for rec in tab:
##        i,ti,tj,j=rec.split(' ')
##        m,n= 1100000L-int(i)-1,1100000L-int(j)-1
##        print float(m)/float(n),m,n
