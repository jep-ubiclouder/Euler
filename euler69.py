def gcd(a, b):

    a = abs(a)
    b = abs(b)
    
    if a == 0:
	if b == 0: raise ValueError, "gcd(0,0) undefined."
	else: return b

    while 1:
	b = b % a
	if (b == 0): return a
	a = a % b
	if (a == 0): return b

# returns (gcd, a, b) where ap + bq = gcd.  taken from snappea


def totient(n):
    tmp=[]
    for i in range(1,n):
        if gcd(n,i)==1 :tmp.append(i)
    return len(tmp)
if __name__=='__main__':
    max=1.0
    for a in range(2,10000):
        res=a*1.0/totient(a)
        if res>max:
            print a,totient(a),res
            max=res
## resultat= primorielle n =>510510
