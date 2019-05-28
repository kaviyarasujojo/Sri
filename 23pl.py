a,b=input().split()
c=[]
c=input().split()
d=[]
d=input().split()
x=''
for i in range(len(d)):
    c.append(d[i])
    x+=max(c,key=int)+" "
print(x)
