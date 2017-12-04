'''
Name:Reshma
Description:prob set 1
Question no:2
'''
try:
  def right_justify(s):
    s1=s.rjust(70)
    print(s1)
  s=raw_input("enter a string")
  right_justify(s)
except Exception as e:
  print e


