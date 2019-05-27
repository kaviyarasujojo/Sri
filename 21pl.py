a=[]
b=[]
for i in range(3):
    c,d=input().split()
    a.append(c)
    b.append(d)
if a.count(a[0])==3 or b.count(b[0])==3:
    print("yes")
else:
    print("no")
