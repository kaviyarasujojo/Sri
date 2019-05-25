a=input()
b=[]
for i in a:
    b.append(i)
b[0]=b[0].upper()
for i in range(1,len(b)):
    if b[i]==" ":
        b[i+1]=b[i+1].upper()
        continue
    elif b[i].isupper() and b[i-1]!=" ":
        b[i]=b[i].lower()
c=''
for i in range(len(b)):
    c+=b[i]
print(c)
