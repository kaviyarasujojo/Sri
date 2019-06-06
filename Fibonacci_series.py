a=int(input())
i=0
b=1
c=0
e=1
d=[]
f=''
while i<a:
	d.append(e)
	e=b+c
	c=b
	b=e
	i+=1
for i in range(len(d)-1):
	f+=str(d[i])+" "
print(f+str(d[-1]))
