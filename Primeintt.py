a=int(input())
b=int(input())
for x in range(a+1,b):
    d=1
    g=0
    while d is not b:
        f=x%d
        d=d+1
        if f==0:
            g=g+1
    if g==2:
        print(x)


