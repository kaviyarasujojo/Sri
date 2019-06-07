a=int(input())
b=input().split()
c=0
d=[]
e=[]
f=''
for i in b:
  for y in i:
    c+=ord(y)
  d.append(c)
  c=0
i=0
while i<len(b):
  e.append(b[d.index(min(d,key=int))])
  b.pop(d.index(min(d,key=int)))
  d.pop(d.index(min(d,key=int)))
  i+=1
for i in range(len(e)):
  f+=e[i]+" "
if b!=[]:
  print(f+b[0])
else:
  print(f)
