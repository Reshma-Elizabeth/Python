'''
Name:Reshma
Description:prob set 1
Question no:9
'''
try:
  def cal(width,height,delimiter):
    w=width/2
    w1=width/2.0
    h=height/3
    e=1+2*5
    d=delimiter*5
    print(w,type(w))
    print(w1,type(w1))
    print(h,type(h))
    print(e,type(e))
    print(d,type(d))
  width=int(raw_input("enter the width"))
  height=int(raw_input("enter the height"))
  delimiter=raw_input("enter the delimiter")
  cal(width,height,delimiter)
except Exception as e:
  print e


    