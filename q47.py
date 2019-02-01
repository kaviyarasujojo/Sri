a=int(input())
c=[]
for i in range(a):
    b=int(input())
    c.append(b)
c.sort()
print(c[0],c[a-1])
