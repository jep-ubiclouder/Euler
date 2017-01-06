'''
Created on 9 sept. 2016

@author: Jean-Eric Preis
'''
'''d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
'''
d17=0

res={}


def check(nbre,di):
    res=[]
    for i in range(10):
        if not( (i*100+nbre)%di):
            res.append(i)

    return(res)

while d17<1000:
    chiffres=[True]*10
    d17+=17
    ## s='{:03d}'.format(d17)
    j=d17%10

    chiffres[j]=False
    i=d17//10 % 10
    chiffres[i]=False
    h=d17//100%10

    chiffres[h] =False
    ##print(d17)
    ##print(chiffres)
    ## si il y des doublons...
    if(h==i or j==h or i==j):
        #print(d17)
        continue
    else:
        pot13=check(h*10+i,13)
        if len(pot13)>0:
            #print(d17)
            #print(pot13)
            for p13 in pot13:
                if p13 in [i,j,h]: continue
                pot11=check(p13*10+h,11)
                if len(pot11)>0:
                    #print('pot11 %i'%len(pot11))
                    for p11 in pot11:
                        if p11 in [h,j,i,p13]: continue
                        pot7=check(p11*10+p13,7)
                    ##print('pot7 %i'%len(pot7))
                        if len(pot7)>0:

                            for p7 in pot7:
                                if p7 in [h,j,i,p13,p11]: continue
                                pot5=check(p7*10+p11,5)
                                if len(pot5)>0:
                                    for p5 in pot5:
                                        if p5 in [h,j,i,p13,p11,p7]: continue
                                        pot3=check(10*p5+p7,3)
                                        if len(pot3)>0:
                                            for p3 in pot3:
                                                if p3 in [h,j,i,p13,p11,p7,p5]: continue
                                                pot2=check(p3*10+p5,2)
                                                if len(pot2)>0:
                                                    for p2 in pot2:
                                                        if p2 in [h,j,i,p13,p11,p7,p5,p3]: continue
                                                        pot1=check(p2*10+p3,1)
                                                        for p1 in pot1:
                                                            if p1 in [h,j,i,p13,p11,p7,p5,p3,p2]: continue
                                                            print('%i%i%i%i%i%i%i%i%i%i'%(p1,p2,p3,p5,p7,p11,p13,h,i,j))


