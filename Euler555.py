'''
Created on 30 mai 2016

@author: Jean-Eric Preis

1, 1, 2, 1, 3, 2, 4, 1, 5, 3, 6, 2, 7, 8, 4, 9, 1, 10, 11, 5
'''
import math
s=[ 1, 1, 2, 1, 3]
d=[0]
cpt=0
for i in s:
    if i>d[-1]:
        d.append(i)
    nextfirst=d[-1]+1
    spacesneeded= int(math.floor(math.sqrt(nextfirst)))
    for t in range(spacesneeded):
        pass
    print('n',nextfirst)
    print('s',spacesneeded)
print(d)
print(s)
