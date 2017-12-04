try:
  print "enter 10 numbers"
  max=None
  for i in range(0,10):
    n=int(raw_input())
    for j in range(0,10):
      if(n%2!=0):
        if(n>max):
          max=n
  if(max is None):
    print "no odd numbers were there"
  print "largest odd number is "+str(max)
except Exception as e:
  print e