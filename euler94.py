
lesplus=(16, 240, 3360, 46816, 652080, 9082320,126500416)
lesmoins=( 5, 65, 901, 12545, 174725, 2433601, 33895685)
res=0

for  m in lesmoins:
    
    res +=(3*m+1)
for p in lesplus:
    res+=(3*p+2)
    
## http://www.research.att.com/~njas/sequences/A103974

print res
