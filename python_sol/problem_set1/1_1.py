'''
Name:Reshma
Description:prob set 1
Question no:1
'''
try:
  x=int(raw_input("enter x value"))
  y=int(raw_input("enter y value"))
  z=int(raw_input("enter z value"))
  x1=x%2
  y1=y%2
  z1=z%2
  if((x1==0)&(y1==0)&(z1==0)):
    print "none of them are odd numbers"
  elif((x1!=0)&(y1!=0)&(z1!=0)):
    # if(x==y==z):
    #   print "all odd numbers are equal"
    if((x>y)&(x>z)):
      print " x is the largest odd number"
    if((y>x)&(y>z)):
      print "y is the largest odd number"
    elif((z>y)&(z>x)):
      print "z is the largest odd number"
    else:
      print "more than one odd numbers are equal"
  elif((x1!=0)&(y1!=0)&(z1==0)):
    if(x>y):
      print " x is the largest odd number"
    elif(y>x):
      print "y is the largest odd number"
    else:
      print "both odd numbers are equal"
  elif((x1!=0)&(y1==0)&(z1!=0)):
    if(x>z):
      print " x is the largest odd number"
    elif(z>x):
      print "z is the largest odd number"
    else:
      print "both odd numbers are equal"
  elif((x1==0)&(y1!=0)&(z1!=0)):
    if(y>z):
      print "y is the largest odd number"
    elif(z>y):
      print "z is the largest odd number"
    else:
      print "both odd numbers are equal"
  elif((x1==0)&(y1==0)&(z1!=0)):
    print "z is the largest odd number"
  elif((x1==0)&(y1!=0)&(z1==0)):
    print "y is the largest odd number"
  elif((x1!=0)&(y1==0)&(z1==0)):
    print "x is the largest odd number"
except Exception as e:
  print e

    
    
    

  
    
  
    