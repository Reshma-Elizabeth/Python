'''
Name:Reshma
Description:prob set 2
Question no:7
'''
try:
  def isPalindrome(s):
    return True if len(s) < 2 else (s[0] == s[-1]) and isPalindrome(s[1:-1])
  s=raw_input("enter a string")
  print isPalindrome(s)
except Exception as e:
  print e