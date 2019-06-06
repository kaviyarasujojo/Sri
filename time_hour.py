a,b=input().split()
c,d=input().split()
e=(int(a)*60)+int(b)
f=(int(c)*60)+int(d)
g=abs(e-f)
h=g%60
i=g//60
print(i,h)
