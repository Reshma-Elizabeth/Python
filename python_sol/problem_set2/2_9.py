'''
Name:Reshma
Description:prob set 2
Question no:9.a
'''
from __future__ import division
import math
try:
  def NewtonSqrt(a,x):
    y=(x + (a/x))/2
    print y
  a=float(raw_input("enter the value of a"))
  x=float(raw_input("enter the value of x"))
  NewtonSqrt(a,x)
except Exception as e:
  print e
