a=int(input())
b=1
c=[]
while (b<=a):
	d=int(input())
	c.append(d)
	b=b+1
for i in range(0,b-1):
	print(c[i],i)
	
