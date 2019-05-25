a=input()
b=[]
c=''
for i in a:
    b.append(i)
for i in range(0,len(a),1):
    if i%2==0:
        b[i]=a[i+1]
    if i%2==1:
        b[i]=a[i-1]
for i in range(len(b)):
    c+=b[i]
print(c)
