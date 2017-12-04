'''
Name:Reshma
Description:prob set 1
Question no:4.c
'''
from __future__ import division
try:
  t=float(raw_input("enter the starting time"))
  t1=t*60
  easy=int(raw_input("enter the miles travelled in easy pace"))
  temp=int(raw_input("enter the miles travelled in tempo pace"))
  tot=((easy*(8/15))+(temp*(7/12)))*60
  time=float((tot+t)/60)
  print "time when you reach home "+str(time)
except Exception as e:
  print e