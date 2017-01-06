#usr/bin/python




def fun(n):
    if n==1: return 1
    if n==89: return 89
    s=list('%s'%(n,))
    
    tmp=0
    for c in s:
        
        tmp += (int(c)*int(c))
    #print tmp
    return fun(tmp)
    
def classer(tchiffres,classe):
    tchiffres.sort()
    tchiffres.reverse()
    tmp=0
    for c in tchiffres:
        if not int(c): break ## on a atteint 0
        tmp += (int(c)*int(c))
    if tmp not in classe.keys():
        typ=fun(tmp)
        classe[tmp]={}
        classe[tmp]["t"]=typ
        classe[tmp]['n']=0
    
        
    classe[tmp]['n']+=1
import sys
if __name__=='__main__':
    print fun(44)
    classe={}
    for i in range(1,10000000):
        if i%10000==0:
            sys.stdout.write('.%s'%(i,))
            sys.stdout.flush()
        classer(list('%s'%(i,)),classe)
    # print classe
    resultat=0
    for clef in classe.keys():
        if classe[clef]['t']==89: resultat += classe[clef]['n']

    print resultat,len(classe.keys())
