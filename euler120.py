def func(a,n):
    return (
        
        ((a-1)**n)%(a*a),
        ((a+1)**n)%(a*a),
        ((a-1)**n+(a+1)**n)%(a*a)
        )
        

##maxes=[(0,0),(0,0),(0,0)]
##for a in  range(3,1001):
##    max=0
##    for n in range(2,2*a):
##        test= func(a,n)
##        if test[-1]>max:
##            max=test[-1]
##            indice=n
##            #print a,n,max
##    maxes.append((indice,max))
##resul=0
##for i in range(len(maxes)):
##0
##    if i >2:
##        print i ,maxes[i],maxes[i][1]/i,i*i,func(i,maxes[i][0])
##        resul+=maxes[i][1]
##print resul
def residus(square):
    res=[]
    prec=square -1
    suiv=square+1
    puiss_p=1
    puiss_s=1
    max=0
    carre =square*square
    for i in range(1,square*square):
        puiss_p *= prec
        ## puiss_p %=carre
        puiss_s *= suiv
        #puiss_s %=carre

        puiss=puiss_p+puiss_s
        test = puiss %carre
        if test>max:
            max=test
        if test in res and test >2:
            print "param:%s,cycle:%s,max:%s,dern puiss:%s"%(square,len(res),max,test)
            
            return max
        else:
            ##print square,i, test
            res.append(test)
    
result=0
for j in range(3,1001):
    result +=residus(j)
print result
