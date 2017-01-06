#!/usr/bin/python

from __future__ import division
import copy
import sys
from types import IntType,FloatType,LongType,ListType,TupleType,InstanceType,ClassType

# set error output to stdout instead
#__errout = sys.stderr
__errout = sys.stdout

#
# Define class contfrac
# Continued Fraction object version 1
#
class contfrac:

  def __init__(self,numerator,denominator=0,limit=256,epsilon=2e-9):
    self.classname="contfracv1"
    # if called by A=contfrac(3.1416)
    if denominator==0:
      if type(numerator)==IntType or type(numerator)==LongType:
        self.num=numerator
        self.den=1
        self.cf=[numerator]
      elif type(numerator)==FloatType:
        self.cf = decimal2contfrac(numerator,limit,epsilon)
        (self.num,self.den) = contfrac2rational(self.cf)
      elif type(numerator)==ListType:
        self.cf=copy.copy(numerator)
        self.num,self.den=contfrac2rational(numerator)
      elif is_contfrac(numerator):
        self.num=numerator.num
        self.den=numerator.den
        self.cf=copy.copy(numerator.cf)
      else:
        # if all else fails its the devil's number
        self.num=666
        self.den=1
        self.cf=[666] 
    # if called by A=(2,3)
    else:
      self.cf = rational2contfrac(long(numerator),long(denominator))
      (self.num,self.den) = contfrac2rational(self.cf)

  def __len__(self):
    return len(self.cf)



def lid(cfobj):
  return lazy_identity(cfobj)

#
# Define class lazy_identity
# Lazy connector for contfrac objects
#
class lazy_identity:

  def __init__(self,cf):
    self.classname="lazy_identity"
    self.cfobj=cf
    self.n=0
    self.a=0
    self.b=1
    self.c=1
    self.d=0

  def egest(self,debugflag=False):
    # First check if we can egest
    # if we can then egest a digit
    # otherwise loop until we can
    if debugflag : print >> __errout,"a=%d,b=%d,c=%d,d=%d" % (self.a,self.b,self.c,self.d) 
    while 1 :
      if self.c == 0 and self.d == 0 :
        break
      if self.c <> 0 and self.d <> 0 and (self.a//self.c) == (self.b//self.d) :
        if debugflag : print >> __errout,"We can egest"
        break
      # Now we must ingest one term from cfobj
      if debugflag : print >> __errout,"n=%d len(cfobj)=%d" % (self.n,len(self.cfobj))
      if self.n < len(self.cfobj) :
        p=self.cfobj.cf[self.n]
        if debugflag : print >> __errout,"term ingested is ",p
        self.n=self.n+1
        # Now calculate the new a,b,c,d
        self.a,self.b,self.c,self.d=self.b,self.a+self.b*p,self.d,self.c+self.d*p
      else :
        if debugflag : print >> __errout,"term ingested is INF"
        self.n=self.n+1
        self.a,self.b,self.c,self.d=self.b,self.b,self.d,self.d
      if debugflag : print >> __errout,"after ingestion a=%d,b=%d,c=%d,d=%d" % (self.a,self.b,self.c,self.d) 
    # out of the while loop
    if self.c== 0 and self.d == 0 :
      if debugflag : print >> __errout,"egest the number INF"
      return 'INF'
    else:
      q=self.a//self.c
      if debugflag : print >> __errout,"egest the number ",q
      # Now calculate the new a,b,c,d
      self.a,self.b,self.c,self.d=self.c,self.d,self.a-self.c*q,self.b-self.d*q
      if debugflag : print >> __errout,"after egestion a=%d,b=%d,c=%d,d=%d" % (self.a,self.b,self.c,self.d) 
      return q
      

#
# Define class lazy_rcf_4onpi
# Lazy connector for 4/pi in regular continued fractions format
# [(1,1),(3,4),(5,9),(7,16),(9,25),(11,36),...]
#        (2n+1,(n+1)^2)
#
class lazy_rcf_4onpi:

  def __init__(self):
    self.classname="lazy_rcf_4onpi"
    self.n=0

  def egest(self,debugflag=False):
    a=  self.n * 2 + 1
    b= (self.n + 1) * (self.n + 1)
    self.n = self.n + 1
    return (a,b)


#
# Define class lazy_rcf2cf
# Lazy connector for turning regular continued fractions
# into standardize continued fractions
#
class lazy_rcf2cf:

  def __init__(self,rcf):
    self.classname="lazy_rcf2cf"
    self.cfobj=rcf
    self.a=0
    self.b=1
    self.c=1
    self.d=0

  def egest(self,debugflag=False):
    # First check if we can egest
    # if we can then egest a digit
    # otherwise loop until we can
    if debugflag : print >> __errout,"a=%d,b=%d,c=%d,d=%d" % (self.a,self.b,self.c,self.d) 
    while 1 :
      if self.c == 0 and self.d == 0 :
        break
      if self.c <> 0 and self.d <> 0 and (self.a//self.c) == (self.b//self.d) :
        if debugflag : print >> __errout,"We can egest"
        break
      # Now we must ingest one term from cfobj
      (p,q)=self.cfobj.egest()
      if debugflag : print >> __errout,"term ingested is ",p
      # Now calculate the new a,b,c,d
      self.a,self.b,self.c,self.d=self.b*q,self.a+self.b*p,self.d*q,self.c+self.d*p
      if debugflag : print >> __errout,"after ingestion a=%d,b=%d,c=%d,d=%d" % (self.a,self.b,self.c,self.d) 
    # out of the while loop
    if self.c== 0 and self.d == 0 :
      if debugflag : print >> __errout,"egest the number INF"
      return 'INF'
    else:
      q=self.a//self.c
      if debugflag : print >> __errout,"egest the number ",q
      # Now calculate the new a,b,c,d
      self.a,self.b,self.c,self.d=self.c,self.d,self.a-self.c*q,self.b-self.d*q
      if debugflag : print >> __errout,"after egestion a=%d,b=%d,c=%d,d=%d" % (self.a,self.b,self.c,self.d) 
      return q
      

#
# Define class lazy_decimal
# Lazy connector for contfrac objects
#
class lazy_decimal:

  def __init__(self,lazycf):
    self.classname="lazy_decimal"
    self.cfobj=lazycf
    self.a=0
    self.b=1
    self.c=1
    self.d=0

  def egest(self,debugflag=False):
    # First check if we can egest
    # if we can then egest a digit
    # otherwise loop until we can
    if debugflag : print >> __errout,"a=%d,b=%d,c=%d,d=%d" % (self.a,self.b,self.c,self.d) 
    while 1 :
      if self.c == 0 and self.d == 0 :
        break
      if self.c <> 0 and self.d <> 0 and (self.a//self.c) == (self.b//self.d) :
        if debugflag : print >> __errout,"We can egest"
        break
      # Now we must ingest one term from cfobj
      p=self.cfobj.egest()
      if p == 'INF' :
        if debugflag : print >> __errout,"term ingested is INF"
        self.a,self.b,self.c,self.d=self.b,self.b,self.d,self.d
      else :
        if debugflag : print >> __errout,"term ingested is ",p
        # Now calculate the new a,b,c,d
        self.a,self.b,self.c,self.d=self.b,self.a+self.b*p,self.d,self.c+self.d*p
      if debugflag : print >> __errout,"after ingestion a=%d,b=%d,c=%d,d=%d" % (self.a,self.b,self.c,self.d) 
    # out of the while loop
    if self.c== 0 and self.d == 0 :
      if debugflag : print >> __errout,"egest the number INF"
      return 'INF'
    else:
      r=self.a//self.c
      if debugflag : print >> __errout,"egest the number ",r
      # Now calculate the new a,b,c,d
      self.a,self.b,self.c,self.d=self.c,self.d,self.a-self.c*r,self.b-self.d*r
      if debugflag : print >> __errout,"after egestion a=%d,b=%d,c=%d,d=%d" % (self.a,self.b,self.c,self.d) 
      # Now calculate the egestion of r2=0 and s2=10
      # new_a = c * s2
      # new_b = d * s2
      # new_c = a - c * r2
      # new_d = b - d * r2
      self.a,self.b,self.c,self.d=self.c*10,self.d*10,self.a,self.b 
      if debugflag : print >> __errout,"after renormalisation a=%d,b=%d,c=%d,d=%d" % (self.a,self.b,self.c,self.d) 
      return r
      

#
# Define class lazy_base
# Lazy base for lazy operators
#
class lazy_base:

  def egest(self,debugflag=False):
    # First check if we can egest
    # if we can then egest a term
    # otherwise loop until we can
    if debugflag : print >> __errout,"a=%d,b=%d,c=%d,d=%di,e=%d,f=%d,g=%d,h=%d" % (self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h) 
    while 1 :
      self.count= self.count + 1
      if self.e == 0 and self.f == 0 and self.g == 0 and self.h == 0 :
        # We need to return INF
        break
      if self.e <> 0 :
        Zoo= self.a // self.e
      else:
        Zoo='INF'
      if self.g <> 0 :
        Zoi= self.c // self.g
      else:
        Zoi='INF'
      if self.f <> 0 :
        Zio= self.b // self.f
      else:
        Zio='INF'
      if self.h <> 0 :
        Zii= self.d // self.h
      else:
        Zii='INF'
      if debugflag : print >> __errout,"Zoo=",Zoo," Zoi=",Zoi," Zio=",Zio," Zii=",Zii
      if Zoo <> 'INF' and Zoo == Zoi and Zoi == Zio and Zio == Zii :
        if debugflag : print >> __errout,"We can egest"
        break
      # Now we must decide which lazy input to ingest from
      if Zio == 'INF' or Zoo == 'INF' :
        alpha='INF'
      else:
        alpha=abs(Zio - Zoo)
      if Zoi == 'INF' or Zoo == 'INF' :
        beta='INF'
      else:
        beta=abs(Zoi - Zoo)
      if debugflag : print >> __errout,"alpha=",alpha," beta=",beta
      if alpha=='INF' and beta=='INF' :
        if self.count % 2 == 0 :
          target='X'
        else:
          target='Y'
      elif alpha=='INF' and beta<>'INF' :
        target='X'
      elif beta=='INF' and alpha<>'INF' :
        target='Y'
      elif alpha > beta :
        target='X'
      else :
        target='Y'
      # Now we must ingest one term from cfobj
      if target=='X' :
        p=self.X.egest()
        if p == 'INF' :
          if debugflag : print >> __errout,"term X ingested is INF"
          self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h=self.b,self.b,self.d,self.d,self.f,self.f,self.h,self.h
        else :
          if debugflag : print >> __errout,"term X ingested is ",p
          # Now calc the new a b c d e f g h 
          self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h=self.b,self.a + self.b*p,self.d,self.c + self.d * p,self.f,self.e + self.f * p,self.h,self.g + self.h*p
      else :
        p=self.Y.egest()
        if p == 'INF' :
          if debugflag : print >> __errout,"term Y ingested is INF"
          self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h=self.c,self.d,self.c,self.d,self.g,self.h,self.g,self.h
        else :
          if debugflag : print >> __errout,"term Y ingested is ",p
          # Now calc the new a b c d e f g h 
          self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h=self.c,self.d,self.a+self.c*p,self.b+self.d*p,self.g,self.h,self.e+self.g*p,self.f+self.h*p
      # After ingestion
      if debugflag : print >> __errout,"after ingestion a=%d,b=%d,c=%d,d=%d,e=%d,f=%d,g=%d,h=%d" % (self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h) 
    # out of the while loop
    if self.e == 0 and self.f == 0 and self.g == 0 and self.h == 0 :
      if debugflag : print >> __errout,"egest the number INF"
      return 'INF'
    else:
      if debugflag : print >> __errout,"egest the number ",Zoo
      # Now calculate the new a,b,c,d,e,f,g,h
      self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h=self.e,self.f,self.g,self.h,self.a-self.e*Zoo,self.b-self.f*Zoo,self.c-self.g*Zoo,self.d-self.h*Zoo
      if debugflag : print >> __errout,"after egestion a=%d,b=%d,c=%d,d=%d,e=%d,f=%d,g=%d,h=%d" % (self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h) 
      return Zoo
    

#
# Define class lazy_add
# Lazy addition for lazy objects
#
class lazy_add(lazy_base):

  def __init__(self,XX,YY):
    self.classname="lazy_add"
    self.count=0
    self.X=XX
    self.Y=YY
    self.a=0
    self.b=1
    self.c=1
    self.d=0
    self.e=1
    self.f=0
    self.g=0
    self.h=0


#
# Define class lazy_sub
# Lazy subtraction for lazy objects
#
class lazy_sub(lazy_base):

  def __init__(self,XX,YY):
    self.classname="lazy_sub"
    self.count=0
    self.X=XX
    self.Y=YY
    self.a=0
    self.b=1
    self.c=-1
    self.d=0
    self.e=1
    self.f=0
    self.g=0
    self.h=0


#
# Define class lazy_mul
# Lazy multiplication for lazy objects
#
class lazy_mul(lazy_base):

  def __init__(self,XX,YY):
    self.classname="lazy_mul"
    self.count=0
    self.X=XX
    self.Y=YY
    self.a=0
    self.b=0
    self.c=0
    self.d=1
    self.e=1
    self.f=0
    self.g=0
    self.h=0


#
# Define class lazy_div
# Lazy division for lazy objects
#
class lazy_div(lazy_base):

  def __init__(self,XX,YY):
    self.classname="lazy_div"
    self.count=0
    self.X=XX
    self.Y=YY
    self.a=0
    self.b=1
    self.c=0
    self.d=0
    self.e=0
    self.f=0
    self.g=1
    self.h=0



if __name__ == '__main__':
  print "======================================="
  print "Pi = 4 div 4/pi"
  print " "
  print "V = lazy_rcf2cf of lazy_rcf_4onpi"
  print "A = lazy_decimal of ( lazy(4) lazy_div  V )"
  print "Now display value of A one digit at a time"
  rpi=lazy_rcf_4onpi()
  V=lazy_rcf2cf(rpi)
  A=lazy_decimal(lazy_div(lid(contfrac(4)),V))
  while 1:
    digit=A.egest()
    sys.stdout.write(str(digit))
    sys.stdout.flush()
  

