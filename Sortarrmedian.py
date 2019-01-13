a=int(input())
b=1
c=[]
while (b<=a):
	d=int(input())
	c.append(d)
	b=b+1
	c.sort()
print(c[int(a/2)])
