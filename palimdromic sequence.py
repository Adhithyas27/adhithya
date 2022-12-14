def palindrome(a):
     return a==a[::-1]
a=str(input("enter the word"))
s=palindrome(a)
if s:
   print("it is the palindromic sequence")
else:print("it is not a palindromic sequence") 
