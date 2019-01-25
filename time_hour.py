a,b=int(input()),int(input())
c,d=int(input()),int(input())
e=(a*60)+b
f=(c*60)+d
g=abs(e-f)
h=g%60
i=g//60
print(i,h)
