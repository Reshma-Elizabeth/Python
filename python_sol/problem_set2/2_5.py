'''
Name:Reshma
Description:prob set 2
Question no:5
'''
try:
  def sumDigits(s):
    sum=0
    for i in s:
      if(i.isdigit()):
        sum=sum+int(i)
    print "sum is "+str(sum)
  s=raw_input("enter a string")
  sumDigits(s)
except Exception as e:
  print e