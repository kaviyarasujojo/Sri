a=int(input())
b=int(input())
c=1
d=0
m=a+1
for x in range(m,b,1):
     while (c<=x):
         e=x%c
         if (e==0):
            d=d+1
         c=c+1
         if (d==2):
             print(x)
