a=int(input())
c=0
e=a
while e>0:
    b=e%10
    c=c+(b*b*b)
    d=int(e/10)
    e=d
if (c==a):
    print("YES")
else:
    print("NO")
