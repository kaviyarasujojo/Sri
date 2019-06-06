a,b=input().split()
c=[]
d=''
for i in range(int(a)+1,int(b)):
    if i%2==0:
        c.append(i)
for i in range(len(c)-1):
    d+=str(c[i])+" "
print(d+str(c[-1]))
