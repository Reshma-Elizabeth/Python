'''
Name:Reshma
Description:prob set 2
Question no:3
'''
from __future__ import division
try:
  def factI(n):
    f=1
    if((n==1) or (n==0)):
      print "factorial using iterative implementation is "+str(1)
    else:
      while(n>0):
        f=f*n
        n=n-1
      print "factorial using iterative implementation is " +str(f)  
  def factR(n):
    if((n==1) or (n==0)):
      return 1
    else:
      return n*factR(n-1)
  n=int(raw_input("enter a number"))
  n1=factR(n)
  print "factorial using recursion is "+str(n1)
  factI(n)
except Exception as e:
  print e


    