a=input()
b=[]
for i in a:
    b.append(i)
i=0
e=len(b)
while i<len(b):
    c=b[i]
    j=i+1
    while j<len(b):
        if c==b[j]:
            b.remove(c)
        j+=1
    d=len(b)
    i+=1
if d==e:
    print("Yes")
else:
    print("No")
