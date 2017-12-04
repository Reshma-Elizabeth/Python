'''
Name:Reshma
Description:prob set 2
Question no:1
'''
try:
  def gcd(a,b):
    if(b==0):
      print "GCD is "+str(a)
    elif((a%b)==0):
      print "GCD is "+str(b)
    else:
      r=a%b
      gcd(b,r)
  a=int(raw_input("enter a number"))
  b=int(raw_input("enter another number"))
  gcd(a,b)
except Exception as e:
  print e


    