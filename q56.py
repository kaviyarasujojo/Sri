a=input()
b=True
for i in a:
	try:
		if(int(i)>=0 or int(i)<=0):
			b=True
		else:
			b=False
			break
	except ValueError:
		if(i>='a' or i<='z'):
			b=True
		else:
			b=False
			break
if(b==True):
	print("Yes")
else:
	print("No")
