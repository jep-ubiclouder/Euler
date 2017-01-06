#!/usr/bin/python

from math import *
import time
import sys



def carteseule(main):
    colors= [couleurs.index(c[1]) for c in main]
    values= [valeurs.index(c[0]) for c in main]
    
    return main[values.index(max(values))]

def paire(main):
    colors= [couleurs.index(c[1]) for c in main]
    values= [valeurs.index(c[0]) for c in main]

    for v in values:
        pass
def num2carte(num):

    (q,r)=divmod(num,13)
    return [valeurs[r],couleurs[q]]

def carte2num(carte):
    mult=couleurs.index(carte[1])
    reste=valeurs.index(carte[0])
    return mult*13+reste
    

if __name__=='__main__':
    global couleurs, valeurs
    couleurs=['S','H','D','C']
    valeurs=list('23456789TJQKA')

    print carte2num('2S')
    print carte2num('AC')
    main=['2S','AC','2C','AC','QD']
    print carteseule(main)
    print paire(main)
