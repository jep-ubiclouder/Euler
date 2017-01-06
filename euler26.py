'''mathworld:
p premier 1/p a une expansion maximale <=> 10 est racine primitive ,
10**k=1 mod p pour k=p-1 et pas avant'''

import sys
premiers=[937,941,947 ,953, 967,971, 977,983 ,991, 997]
premiers.reverse()
for p in premiers:
    print p
    for i in range(2,p):
        if (10**i % p) == 1 : break
    if i==p-1:
        print p
        sys.exit()
