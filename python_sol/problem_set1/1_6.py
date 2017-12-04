'''
Name:Reshma
Description:prob set 1
Question no:6
'''
try:
  print "Enter a sequence of decimal numbers separated by commas"
  s=raw_input()
  s.split(',')
  sum=0
  for i in s.split(','):
     sum=sum+float(i)
  print "sum of the numbers is "+str(sum)
except Exception as e:
  print e


    