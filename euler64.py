#/usr/bin/python




def cont_frac(n):
    """ calculer la racine de n en fraction continue,
    Renvoie un tableau [a,[a,bc]] avec le cycle.
    """

    ## trouver le partie entiere de racine(n)
    for sq in squares:
        if sq >n:
            break
    ent=squares.index(sq)-1
    print ent
    denom=n-ent*ent
    print denom
    

if __name__=='__main__':
    global squares
    squares=[n*n for n in range(10000)]
    cont_frac(17)
    pass
