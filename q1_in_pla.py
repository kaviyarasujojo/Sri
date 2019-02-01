a=input()
b=[]
c=""
for i in a:
     b.append(i)
d=len(a)
for y in range(d):
       c=c+b[d-1]
       d-=1
print(c)
