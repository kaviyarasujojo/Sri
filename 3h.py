a=int(input())
b=input().split()
c=[]
d=''
for i in range(len(b)):
    if i==int(b[i]):
        c.append(i)
for i in range(len(c)-1):
    d+=str(c[i])+" "
print(d+str(c[-1]))
