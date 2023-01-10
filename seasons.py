month=input("Enter the month")
date=int(input ("Enter the date"))
if month in ("january", "february", "march"):
      print ("Summer season")
elif month in ("April","may","June"):
       print ("Spring season")
elif month in ("july", "august", "September"):
       print ("Autumn season")
else:
       print ("winter season")

if(month=="march") and (date>20):
      print ("Summerseason")
elif (month=="june") and (date>21):
      print ("Spring season")
elif (month=="september") and (date>22):
      print ("Autumn season")
elif (month=="December") and (date>21):
      print("winter season") 
