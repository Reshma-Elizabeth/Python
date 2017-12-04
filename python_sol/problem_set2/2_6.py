'''
Name:Reshma
Description:prob set 2
Question no:6
'''
try:
  def findAnEven(l):
    for i in l:
      j=int(i)
      if(j%2==0):
        return j
        break
  l=raw_input("enter a list of integers").split(' ')
  print "the first even number is "+str(findAnEven(l))
except Exception as e:
  print e