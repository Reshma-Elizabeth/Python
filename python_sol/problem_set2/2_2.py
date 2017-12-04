'''
Name:Reshma
Description:prob set 2
Question no:2
'''
from __future__ import division
try:
  def is_power(a,b):
    d=a/b
    if((a%b==0)&(d%b==0)):
      print "true"
    else:
      print "false"
      
  a=int(raw_input("enter a number"))
  b=int(raw_input("enter another number"))
  is_power(a,b)
except Exception as e:
  print e