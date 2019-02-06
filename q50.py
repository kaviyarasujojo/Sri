a=int(input())
b=True
for i in range(0,a):
	b=2**i
	if (b==a):
		b=False
		break
if (b==False):
	print("yes")
else:
	print("no")
