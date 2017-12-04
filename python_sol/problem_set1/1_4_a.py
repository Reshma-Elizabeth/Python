'''
Name:Reshma
Description:prob set 1
Question no:4.a
'''
from __future__ import division
try:
  def volume(r):
    vol=float((4/3)*((3.14)*r*r*r))
    print "volume of sphere is " +str(vol)
  r=int(raw_input("enter the radius of the sphere "))
  volume(r)
except Exception as e:
  print e


  