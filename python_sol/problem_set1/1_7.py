'''
Name:Reshma
Description:prob set 1
Question no:7
'''
try:
  def isIn(s,r):
    if((s in r) or (r in s)):
      print "true"
    else:
      print "false"
  s=raw_input("enter a string")
  r=raw_input("enter another string")
  isIn(s,r)
except Exception as e:
  print e


    