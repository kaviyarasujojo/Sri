a=int(input())
d=0
m=1
n=a+1
c=1
for x in range(m,n,1):
    b=a%c
    if(b==0):
        d=d+1
    c=c+1
if(d==2):
   print("yes")
else:
   print("no")
