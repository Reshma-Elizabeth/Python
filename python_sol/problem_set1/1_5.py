'''
Name:Reshma
Description:prob set 1
Question no:5
'''
from __future__ import division
import math
try:
  n=int(raw_input("enter an integer"))
  sq=math.sqrt(n)
  pwr=n/sq
  if((pwr<6)&(pwr>0)):
    if((math.pow(sq,pwr))==n):
      print "square root " +str(sq)
      print "power " +str(pwr)
    else:
      print "power multiplied by square root doesnt give the entered number"
  else:
    print "power is not in the range"
except Exception as e:
  print e


    