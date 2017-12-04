'''
Name:Reshma
Description:prob set 2
Question no:8
'''
import math
try:
  def eval_loop(s):
    last=0
    e=eval('%s' % s)
    last=last + e
    print e
    a=raw_input("do u want to evaluate or else type done?")
    if(a=='done'):
      print "the value of the last expression evaluated "+str(last)
    else:
      eval_loop(a)
  s=raw_input("Enter the input:")
  
  eval_loop(s)
except Exception as e:
  print e
