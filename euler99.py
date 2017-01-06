
from math import log
if __name__=='__main__':
    print log(2),log(10)
    f = open('/media/ipod/Download/base_exp.txt')
    i=1
    max=1
    for l in f.readlines():
        (b,e)=l.split(',')
        test=float(e)*log(float(b))
        if test>max:
            max=test
            print i,test,b,e
        i+=1
