a=int(input())
b=input().split()
c=''
b.sort(key=int)
for i in range(len(b)-1):
	c+=b[i]+" "
print(c+b[-1])
