'''
Name:Reshma
Description:prob set 2
Question no:4
'''
try:
  def bin_to_dec(bin):
    dec=0
    for digit in bin:
      dec = dec*2 + int(digit)
    return dec
  bin=raw_input("enter the binary value ")
  d=bin_to_dec(bin)
  print "decimal equivalent is "+str(d)
except Exception as e:
  print e


    