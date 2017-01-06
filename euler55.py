

def ispalin(s):
    v=True
    ## print s
    for i in range(len(s)/2):
        ## print i,-(i+1),s[i],s[-(i+1)]
        if s[i]<>s[-(i+1)]:
            return False
    return v

def reverseadd(n):
    l=list('%s'%(n,))
    l.reverse()
    i=int(''.join(l))
    return n+i

if __name__=='__main__':
    max_iter=50
    res=[]
    for nbre in range(100,10000):
        i=0
        s=nbre
        while i< max_iter :
            i+=1
            s=reverseadd(s)
            if ispalin(list('%s'%(s,))):
                break
        if i>=max_iter: res.append(nbre)
    print len(res),res
