a,b=input().split()
e=[]
f=''
for i in range(int(a)+1,int(b)):
  c=1
  d=0
  while c<=i:
    if i%c==0:
      d+=1
    c+=1
  if d==2:
    e.append(i)
for i in range(len(e)-1):
  f+=str(e[i])+" "
print(f+str(e[-1]))
