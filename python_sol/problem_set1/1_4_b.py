'''
Name:Reshma
Description:prob set 1
Question no:4.a
'''
from __future__ import division
try:
  def cost():
    c=0
    cp=float(raw_input("enter the cover price of the book"))
    d=float(raw_input("enter the discount % for the book"))
    sc1=float(raw_input("enter the shipping cost for first copy"))
    sc2=float(raw_input("enter the shipping cost for additional copy"))
    n=int(raw_input("enter the no. of copies"))
    if(n==1):
      c=c+cp*(d/100)*sc1
    else:
      c=c+(cp*(d/100)*sc2*n)
    print "the wholesale cost is " + str(c)
  cost()
except Exception as e:
  print e


