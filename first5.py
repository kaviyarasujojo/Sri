a=int(input())
b=[]
c=''
for i in range(1,6):
    b.append(a*i)
for i in range(len(b)-1):
    c+=str(b[i])+" "
print(c+str(b[-1]))
