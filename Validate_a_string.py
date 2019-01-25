a=input()
try:
   if (int(a)<=0 or int(a)>=0):
       print("Yes")
except ValueError:
   print("No")
 
