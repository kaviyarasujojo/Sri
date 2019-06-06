a=int(input())
b=input().split()
c=[]
d=''
for i in range(len(b)):
    if i==int(b[i]):
        c.append(i)
c.sort(key=int)
if len(c)>0:
    for i in range(len(c)-1):
        d+=str(c[i])+" "
    print(d+str(c[-1]))
else:
    print(-1)
