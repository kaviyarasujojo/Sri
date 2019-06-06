a,b=input().split()
for x in range(int(a)+1,int(b)):
    d=0
    e=x
    while (e!=0):
        c=int(e%10)
        f=int(e/10)
        d=d+(c*c*c)
        e=f
    if (d==x):
        print(d)

